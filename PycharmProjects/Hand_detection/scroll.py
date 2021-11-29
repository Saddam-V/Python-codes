from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
browser.close()

while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text
    if 'End of Results' in Divs:
        print 'end'
        break
    else:
        continue