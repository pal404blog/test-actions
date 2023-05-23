from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)
for x in range(181):
    driver.get('https://charusat.edu.in:912/UniExamResult/frmUniversityResult.aspx') # Open Quora website

    a1 = driver.find_element('xpath','//*[@id="ddlInst"]') # HTML tag element for email field
    drop = Select(a1)
    drop.select_by_visible_text('CSPIT')

    a2 = driver.find_element('xpath','//*[@id="ddlDegree"]') # HTML tag element for password field
    drop = Select(a2)
    drop.select_by_visible_text('BTECH(CE)') # Login password

    a3 = driver.find_element('xpath','//*[@id="ddlSem"]') # HTML tag element for password field
    drop = Select(a3)
    drop.select_by_visible_text('3')

    a4 = driver.find_element('xpath','//*[@id="ddlScheduleExam"]') # HTML tag element for password field
    drop = Select(a4)
    drop.select_by_visible_text('NOVEMBER 2022')

    a5 = driver.find_element('xpath','//*[@id="txtEnrNo"]') # HTML tag element for password field
    
    if x< 154:
        if x < 100:
            if x < 10:
                a5.send_keys('21CE00'+ str(x+1) )
            else:
                a5.send_keys('21CE0'+ str(x+1) )
        
        else :
            a5.send_keys('21CE'+ str(x+1) )
    else:
        a5.send_keys('D22CE1'+ str(x+1) )
    # Diploma rolls

    

    button = driver.find_element('xpath','//*[@id="btnSearch"]') # HTML tag element for button

    button.click()
    WebDriverWait(driver, timeout=100)
    try:
        # driver.wait(button.get_attribute("Processing.."))
        b1 = driver.find_element('xpath','/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[1]')
        b2 = driver.find_element('xpath','//*[@id="uclGrd1_lblStudentName"]')
        
        b3 = driver.find_element('xpath','/html/body/form/div[3]/div/div/table[4]/tbody/tr[1]/td[4]')
        b4 = driver.find_element('xpath','//*[@id="uclGrd1_lblSGPA"]')
        b5 = driver.find_element('xpath','/html/body/form/div[3]/div/div/table[3]/tbody/tr[1]/td[4]')
        b6 = driver.find_element('xpath','//*[@id="uclGrd1_lblExamNo"]')

        f = open("results.txt", "a")
        f.write(b1.text + ":" + b2.text + "\n" + b5.text + ":" + b6.text + "\n" + b3.text + ":" + b4.text +"\n \n")
        f.close()
    except:
        print("Id not found " + str(x+1))
