from selenium import webdriver
from bot import time
import bot
from bot import login
from bot import google_meet_setup


vaibhav = login("vaibhavtarun52@gmail.com","")
vaibhav.sign_in()
vaibhav.loginID()
time.sleep(1)
vaibhav.next1_click()
vaibhav.password_enter()
time.sleep(1)
vaibhav.next2_click()
vaibhav.google_meet()
vaibhav.google_meet_enter()
vaibhav_set = google_meet_setup("yes")
vaibhav_set.new_meeting()
time.sleep(5)


time.sleep(10)
