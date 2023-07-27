
import time
import logging as log
from utils import get_date
from setup import driver, url
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def book(weekday, time_slot):
    weekday_index = 1 if weekday == 'Tuesday' else 3 if weekday == 'Thursday' else None
        
    if weekday is not None:
        date = get_date(weekday_index)
        print(f'Selected date is : {date}')

        driver.get(f'{url}/Views/Activities?type=l&mfu=Badminto&cid=7&crdate={date}&area=SpHall&timer=true')
        time_alert = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'ToDecide')))
        if time_alert is not None:
            driver.find_element(By.CSS_SELECTOR, '#ToDecide > div > div > div.modal-footer > button').click()
        
        try:
            timetable = driver.find_element(By.ID, 'timetable_Days_Day')
            desired_time_slot = driver.find_element(By.ID, time_slot)
            
            if desired_time_slot is not None:
                driver.execute_script('arguments[0].scrollIntoView();', desired_time_slot)
            
            time.sleep(10)
        except NoSuchElementException as e:
            log.error(f'Unable to locate an element: {e.msg}') 
    