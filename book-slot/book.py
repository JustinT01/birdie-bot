
import time, datetime
import logging as log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://eleisure.sportsoft.co.uk/cgrs'
username, password, authenticated = None, None, None


driver = webdriver.Chrome()
driver.maximize_window()


def login():
    driver.get(f'{url}/Account/login')
    username = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'MainContent_SSLogin_txtUserName')))
    
    username.clear()
    username.send_keys('Jt@castlegreen')
    driver.implicitly_wait(1)

    password = driver.find_element(By.ID, 'MainContent_SSLogin_txtPassword')
    password.clear()
    password.send_keys('Jt7977')
    driver.implicitly_wait(1)
    
    login = driver.find_element(By.ID, 'MainContent_SSLogin_btnLogin')
    login.click()
    # authenticated = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located((By.ID, 'RequestAuthenticate')))
    # return authenticated


def book(weekday, time_slot):
    weekday_index = 1 if weekday == 'Tuesday' else 3 if weekday == 'Thursday' else None
        
    if weekday is not None:
        date = get_date(weekday_index)
        print(f'Selected date is : {date}')

        driver.get(f'{url}/Views/Activities?type=l&mfu=Badminto&cid=7&crdate={date}&area=SpHall&timer=true')
        
        time_alert = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'ToDecide')))
        
        if time_alert is not None:
            driver.find_element(By.CSS_SELECTOR, '#ToDecide > button').click()

        timetable = driver.find_element(By.ID, 'timetable_Days_Day')
        desired_time_slot = driver.find_element(By.ID, time_slot)
        
        if desired_time_slot is not None:
            driver.execute_script('arguments[0].scrollIntoView();', desired_time_slot)
        
        time.sleep(10)


def get_date(weekday_index):
    current_date = datetime.datetime.now()
    
    if current_date.weekday() == 1 or current_date.weekday() == 3:
        return current_date.strftime("%d/%m/%Y")
    
    # Finding delta days
    days_delta = weekday_index - current_date.weekday()
    if days_delta <= 0: days_delta += 7
    
    # adding days to required result
    date = current_date + datetime.timedelta(days_delta)
    date = date.strftime("%d/%m/%Y")
    
    return date
    

# User flow 
login()
log.info('🚀 Successfully signed in !!!')

book('Tuesday', "0600")
book('Tuesday', "0700")

book('Thursday', "0600")
book('Thursday', "0700")


    