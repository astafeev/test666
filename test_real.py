from selenium import webdriver
import time

class Test2():
    def test_test1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com")
        x = driver.find_element_by_name("q")
        x.send_keys("Влад Паламарчук")
        x.submit()
        time.sleep(3)
        driver.quit()

    def test_test2(self):
        driver = webdriver.Chrome()
        driver.get("https://ukr.net")
        time.sleep(3)
        driver.quit()
