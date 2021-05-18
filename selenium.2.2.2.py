from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/selects2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1")
    x = x.text
    y = browser.find_element_by_id("num2")
    y = y.text
    z = int(x) + int(y)
    s = "[value='" + str(z) + "']"
    
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(s).click()
    
    button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
