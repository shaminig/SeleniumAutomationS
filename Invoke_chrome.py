from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.geeksforgeeks.org/python-programming-language/?ref=shm")
driver.back()
driver.forward()
driver.refresh()
driver.minimize_window()
driver.close()