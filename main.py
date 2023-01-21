from selenium import webdriver
from src import solveRecaptcha


driver = webdriver.Chrome()
driver.get('https://www.georgiapublicnotice.com/(S(k1pbjkizbh11lvewno4ep5d3))/Details.aspx?SID=k1pbjkizbh11lvewno4ep5d3&ID=2711377')
solveRecaptcha(driver) #FOR PREDICTION ON YOUR PC
submit_button=driver.find_element_by_id("ctl00_ContentPlaceHolder1_PublicNoticeDetailsBody1_btnViewNotice")
submit_button.click()   