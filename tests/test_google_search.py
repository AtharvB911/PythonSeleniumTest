from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins Selenium Test")
    search_box.send_keys(Keys.RETURN)

    # Wait until the title contains the search term
    WebDriverWait(driver, 10).until(EC.title_contains("Jenkins"))

    assert "Jenkins" in driver.title

    driver.quit()
