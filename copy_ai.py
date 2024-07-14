from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
def generate_copies(text):

    email_subject = text
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9221")
    driver = webdriver.Chrome(options=chrome_options)
    # print(driver.window_handles)
    # exit()
    driver.switch_to.window("BE7EE415BC073A004DBCA39100232D42")
    # driver.get('https://chatgpt.com')
    driver.find_element(By.CSS_SELECTOR, "textarea#prompt-textarea").send_keys("Can you generate 3 different copies of the email subject below: " + email_subject)
    time.sleep(0.4)
    driver.find_element(By.CSS_SELECTOR, 'button[data-testid="fruitjuice-send-button"]').click()
    time.sleep(5)
    results = driver.find_elements(By.CSS_SELECTOR, "div.w-full.text-token-text-primary ol")[-1]
    output = []
    for result in results.find_elements(By.CSS_SELECTOR, "li"):
        output.append(result.text)

    return output
if __name__ == '__main__':
    print(generate_copies("get good at fortnite batle royale"))

# elem = driver.find_element(By.CSS_SELECTOR, "div#cta75070")

# driver.execute_script("document.querySelector('div#cta75070').style.display = 'block;'")
# driver.execute_script("window.scroll(0,600)")

# driver.find_element(By.CSS_SELECTOR, 'input[name="topic"]').send_keys(email_subject)
# try:
#     driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
# except:
#     pass
# driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').click()
# try:
#     driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
# except:
#     pass
# driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("company_name")
# try:
#     driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
# except:
#     pass
# driver.find_element(By.CSS_SELECTOR, 'select[name="tone"]').click()
# try:
#     driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
# except:
#     pass
# driver.find_element(By.CSS_SELECTOR, 'option[value="Convincing"]').click()
# try:
#     driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
# except:
#     pass
# driver.find_element(By.CSS_SELECTOR, 'option[value="Convincing"]').click()
# try:
#     driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
# except:
#     pass
# driver.find_element(By.CSS_SELECTOR, 'button#generate-button').click()
#
# while True:
#     try:
#         driver.find_element(By.CSS_SELECTOR, "div.cf-close").click()
#     except:
#         pass
#     results = driver.find_elements(By.CSS_SELECTOR, "div.suggestions div.result")
#     if results != []:
#         break
# for result in results:
#     print(result.text)
