from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins Selenium Test")
    search_box.submit()
    assert "Jenkins" in driver.title
    driver.quit()
