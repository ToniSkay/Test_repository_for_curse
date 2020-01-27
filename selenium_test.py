
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_tag_name('input')
	input1.send_keys('Anton')

	input2 = browser.find_element_by_name('last_name')
	input2.send_keys('Chuevskij')

	input3 = browser.find_element_by_class_name('form-control.city')
	input3.send_keys('Minsk')

	input4 = browser.find_element_by_id('country')
	input4.send_keys('Belarus')

	#browser.execute_script("window.scrollBy(0, 200);")

	button = browser.find_element_by_css_selector('button.btn')
	button.click()

finally:
	time.sleep(30)
	browser.quit()