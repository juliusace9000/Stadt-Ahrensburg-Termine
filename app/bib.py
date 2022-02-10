from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def getTermine():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote("http://selenium:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
    driver.implicitly_wait(10)
    driver.get('https://reservation.frontdesksuite.com/ahrensburg/ahrensburg/Home/Index?pageId=10963985-24b5-4b55-9b81-a2f9c895905e&culture=de&uiCulture=de')
    driver.find_element_by_xpath("/html/body/div/main/div[2]/div[2]/div/div[2]/a").click()
    driver.find_element_by_xpath("/html/body/div/main/div[2]/div[2]/div[2]/div/a").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("./1.png")
    driver.quit()
    return True
    #time.sleep(1)
