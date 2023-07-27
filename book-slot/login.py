from book import driver, url

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