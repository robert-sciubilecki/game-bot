from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

consent = driver.find_element(By.CLASS_NAME, value='fc-cta-consent').find_element(By.TAG_NAME, value='p')
consent.click()
time.sleep(1)
language = driver.find_element(By.ID, value='langSelect-EN')
language.click()
time.sleep(2)

# I was planning on limiting runtime, but now I don't know. We'll see
# timeout = time.time() + 30

cookie = driver.find_element(By.ID, value='bigCookie')
products = driver.find_elements(By.CLASS_NAME, value='product')
time_start = time.time()
gap = 5
max_buy = 3
action = ActionChains(driver)

while True:
    cookie.click()

    if time.time() > time_start + gap:
        if gap > 5:
            upgrade = driver.find_element(By.ID, value=f'upgrade0')
            if 'enabled' in upgrade.get_attribute('class'):
                action.move_to_element(upgrade).click().perform()
        for product in products[::-1]:
            if 'enabled' in product.get_attribute('class'):
                count = product.find_element(By.CLASS_NAME, value='owned').text
                if not count:
                    product.click()
                    max_buy += 2
                elif int(count) < max_buy:
                    product.click()
        gap += 5
