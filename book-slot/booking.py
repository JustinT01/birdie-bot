import time
import logging as log
from utils import get_date
from setup import driver, url
from config import total_slots_to_book
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def book(weekday, time_slot):
    weekday_index = 1 if weekday == 'Tuesday' else 3 if weekday == 'Thursday' else None
        
    if weekday is not None:
        date = get_date(weekday_index)
        
        driver.get(f'{url}/Views/Activities?type=l&mfu=Badminto&cid=7&crdate={date}&area=SpHall&timer=true')
        time.sleep(3)

        time_alert = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#ToDecide')))
        if time_alert is not None:
            driver.find_element(By.CSS_SELECTOR, '#ToDecide > div > div > div.modal-footer > button').click()
            
        try:
            timetable = driver.find_element(By.ID, 'timetable_Days_Day')
            desired_time_slot = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, time_slot)))
            if desired_time_slot is not None:
                time.sleep(1)
                driver.execute_script('arguments[0].scrollIntoView();', desired_time_slot)
            
                book_btns = driver.find_elements(By.ID, 'btnBook')
                
                for book_btn in book_btns:
                    # //*[@id="timetable_Days_Day"]/div[2]/div/div[1]/div[1]/p/text()[2]
                    book_btn_parent = book_btn.find_element(By.XPATH, '../../../../../../div/div')
                    if book_btn_parent.get_attribute("id") == time_slot:
                        selected_book_btn = book_btn
                
                print('INFO: Ready to book.')
                time.sleep(5)
                selected_book_btn.click()
                time.sleep(5)
            else:
                print(f'ERROR: Unable to find {desired_time_slot} time slot. Continuing with next steps')
                
            # Wait for the booking confirmation alert and proceed
            confirm_alert = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'BookMessagemodalContent')))
            if confirm_alert is not None:
                driver.find_element(By.ID, 'BMbtnAgree').click()
                print(f'INFO: Successfully added slot: {time_slot} to the cart.')
                time.sleep(1)
            else:
                print('ERROR: Unable to find confirmation alert when expected.')
             
            # TODO: This logic is to handle the checkout alert   
            # checkout_alert =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dialog_Cart')))
            # if checkout_alert is not None:
            #     driver.find_element(By.CSS_SELECTOR, '#dialog_Cart > div > div > div.modal-footer > button.btn.btn-default.btn-md').click()
            #     time.sleep(1)
            # else:
            #     print('ERROR: Unable to find checkout alert when expected.')            
        except NoSuchElementException as e:
            log.error(f'ERROR: Unable to locate the following element: {e.msg}') 
            
            
            
def checkout():
    driver.get(f'{url}/ChooseTenderType')
    print(f'INFO: Loading shopping cart.')
    driver.get(f'{url}/ChooseTenderType')

    time.sleep(1)
    
    # TODO// Below logic is to handle unexpected error
    # unexpected_error_alert = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'alert_messageDIV')))
    # if unexpected_error_alert is not None:
    #     print('ERROR: Unexpected error found (might be a genuine issue with the portal). Redirecting to the home page')            
    #     driver.find_element(By.ID, 'alert_btnOK').click()
        
    driver.switch_to.parent_frame()
    checkout_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary'))) 
    if checkout_btn is not None:
        checkout_btn.click()
        time.sleep(1)
    else:
        card_pay_btn =  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'btnStripe')))
        if card_pay_btn is not None:
            card_pay_btn.click()
            time.sleep(1)
    
    print(f'INFO: Successfully reached stripe payment gateway.')

        
    
    
    