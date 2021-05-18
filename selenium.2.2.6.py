from selenium import webdriver
import time 
import math
import os 

link = "http://suninjuly.github.io/file_input.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element_by_name("email")
    input3.send_keys("asfads@assadfafs.rt")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
