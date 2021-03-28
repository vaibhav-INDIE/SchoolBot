from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


PATH = "C:\Program Files (x86)\chromedriver.exe"
brower = webdriver.Chrome(PATH) 
brower.get("https://www.google.com/")


class login():
    def __init__(self,username,password):
        self.username = username
        self.password = password


    def sign_in(self):
        search = brower.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[2]/div[2]")
        search.click()


    def loginID(self):
        login = brower.find_element_by_id("identifierId")
        login.click()
        login.send_keys(self.username)

    def next1_click(self):
        try:
            next1 = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"))
            )
            next1.click()
        except:
            brower.quit()

    def password_enter(self):
        try:
            passworduser = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"))
            )
            passworduser.send_keys(self.password)
        except:
            brower.quit()


    def next2_click(self):
        try:
            next2 = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"))
            )
            next2.click()
        except:
            brower.quit()

    def google_meet(self):
        try:
            search_google = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input"))
            )
            search_google.send_keys("google meet")
            search_google.send_keys(Keys.RETURN)
        except:
            brower.quit()

    def google_meet_enter(self):
        try:
            google_meet = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/a/h3"))
            )
            google_meet.click()

        except:
            brower.quit()


class google_meet_setup(): 
    

    def __init__(self,allow):
        self.allow = allow


    def new_meeting(self):
        if (self.allow == "yes"):
            try:
                button_new = WebDriverWait(brower, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/button/div[2]"))
                )
                button_new.click()

            except:
                brower.quit()


            try:
                button2 = WebDriverWait(brower, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/div/ul/li[2]"))
                )
                button2.click()
            except:
                brower.quit()
    def english(self):
        try:
            English = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz/div[1]/div[2]/div/div[1]/div[3]/div[2]/div[1]/label/input"))
            )
            English.click()
            English.send_keys("vemykcoroz")
            English.send_keys(Keys.RETURN)

        except:
            brower.quit()

    def apps(self):
        try:
            apps = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header/div[1]/div/div[1]/div[1]/div/div/a/svg/path"))
            )
            apps.click()
        except:
            brower.quit()

    def calender(self):
        try:
            calender = WebDriverWait(brower, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/c-wiz/div/div/c-wiz/div/div/ul[1]/li[12]/a/div[5]/span"))
            )
            calender.click()
        except:
            brower.quit()

