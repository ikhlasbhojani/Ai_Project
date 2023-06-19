import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def send_message():
    service = Service('./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://web.whatsapp.com/')
    time.sleep(30)
    with open("num.txt", 'r') as file:
        for line in file:
            number = line.strip()
            print(number)
            message = 'This is a test message'
            url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
            driver.get(url)
            time.sleep(15)
            send_button = driver.find_element(By.CLASS_NAME, "p2rjqpw5")
            send_button.click()
            time.sleep(2)
    driver.quit()

send_message()

