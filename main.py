from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os


class Bot:
    
    def __init__(self):
        self.chrome_path = os.getenv('CHROME_PATH')
        self.ser = Service(self.chrome_path)
        self.driver = webdriver.Chrome(service=self.ser)
        self.driver.get('https://www.linkedin.com/')
        self.job_title = 'analyst'
        self.remote_job = 'f_WT=2&' # Set to '' to remove remote filter
        
    
    def sign_in(self):
        load_dotenv()
        login_user = os.getenv('LINKEDIN_USER_NAME')
        login_pw = os.getenv('LINKEDIN_PASSWORD')
        user_entry = self.driver.find_element(By.ID, 'session_key')
        pw_entry = self.driver.find_element(By.ID, 'session_password')
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, '#main-content > section.section.min-h-\[560px\].flex-nowrap.pt-\[40px\].babybear\:flex-col.babybear\:min-h-\[0\].babybear\:px-mobile-container-padding.babybear\:pt-\[24px\] > div > div > form > button')
        user_entry.send_keys(login_user)
        pw_entry.send_keys(login_pw)
        sign_in_button.click()
        
    
    def job_page_setup(self):
        self.driver.get(f'https://www.linkedin.com/jobs/search/?currentJobId=3237829250&distance=25&f_AL=true&f_E=2&{self.remote_job}geoId=103644278&keywords={self.job_title}')
        
    
    def apply(self):
        time.sleep(5)
        html_list = self.driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
        jobs = html_list.find_elements(By.CLASS_NAME, 'disabled ember-view job-card-container__link job-card-list__title')
        apply_button = self.driver.find_element(By.CLASS_NAME, 'artdeco-button__text')
        for job in jobs:
            if jobs[job].is_displayed():
                job.click()
                apply_button.click()
            

if __name__ == "__main__":
    bot = Bot()
    bot.sign_in()
    bot.job_page_setup()
    bot.apply()