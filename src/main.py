from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 

print(os.getcwd())
dir_path = os.path.dirname(os.path.realpath(__file__))
fire_fox_driver_dir = os.path.join(dir_path, "..", "driver", "geckodriver")
print(dir_path, fire_fox_driver_dir)
driver = webdriver.Firefox(executable_path=fire_fox_driver_dir)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()