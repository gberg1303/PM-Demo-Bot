from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import names

# Create Random Names
RealName = names.get_full_name()
PlayerName = RealName[:10].replace(" ", "")
email = RealName.replace(" ", "") + "@gmail.com"
password = "PaSsWoRd12345!"
location = "Dresden 1945"

class PM_Demo_Bot():

    # Open the Web Driver 
    def __init__(self):
        self.driver = webdriver.Firefox()

    # Go to the Web Page
    def Fuck_Zach_Friends(self):
        self.driver.get('https://pm-demo.com/')

        # Move to Create Account Page
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="li_createbtn"]'))).click()

        # Create the New Random Account
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/input'))).send_keys(PlayerName) #Player Name
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/input'))).send_keys(RealName) #Real Name
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[7]/div[2]/input'))).send_keys(email) #Email
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/input'))).send_keys(location) #location
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[6]/div[2]/input'))).send_keys(password) #Password1
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[6]/div[4]/input'))).send_keys(password) #Password2
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[9]/button'))).click() # Create Account
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[2]/div[2]/button'))).click() # Okay

        # Login to the New Account
        #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[18]/div[2]/div[2]/input'))).send_keys(PlayerName) #Player Name
        #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[18]/div[2]/div[4]/input'))).send_keys(password) #Password
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[18]/div[2]/div[11]/button'))).click() # Create Account

        # Get into a Game
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[17]/div[11]/ul/li[2]'))).click() # Navigate to Ring Games
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[17]/div[11]/div[2]/div[1]/div[2]/div[1]/div[1]'))).click() # Navigate to NL_Holdem
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[17]/div[11]/div[2]/div[4]/button'))).click() # Join NL Holdem
    
    # Take a Seat that the Table
    def Take_A_Seat(self):
        try:
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[40]/div[3]'))).click() # Seat 1
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
        except Exception: 
            try:
                WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[51]/div[3]'))).click()# Seat 2
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
            except Exception:
                try:
                    WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[62]/div[3]'))).click()# Seat 3
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                except Exception:
                    try:
                        WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[73]/div[3]'))).click()# Seat 4
                        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                    except Exception:
                        try:
                            WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[84]/div[3]'))).click()# Seat 5
                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                        except Exception:
                            try:
                                WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[95]/div[3]'))).click()# Seat 6
                                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                            except Exception:
                                try:
                                    WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[106]/div[3]'))).click()# Seat 7
                                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                                except Exception:
                                    try:
                                        WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                                        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[117]/div[3]'))).click()# Seat 8
                                        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                                        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                                    except Exception:
                                        try:
                                            WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[128]/div[3]'))).click()# Seat 9
                                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
                                        except Exception:
                                            WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[64]/div[2]/div[5]/button'))).click() # Click Okay
                                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[139]/div[3]'))).click()# Seat 10
                                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[4]/div[2]/div[1]'))).click() # Click Max Buy-In
                                            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[58]/div[2]/div[8]/button'))).click() # Click Okay
    # Define Shove
    def Shove(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[23]/div[1]/input'))).send_keys("10000") # Input Max Bid
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[26]/button'))).click() # Bid
            
    # Define Call
    def Call(self):
        WebDriverWait(self.driver,1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[25]/button'))).click() # Call
    
    # Buy Back
    def Buy_Back(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[68]/div[2]/div[2]/button'))).click() # Click Okay
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[2]'))).click() # Click Menu
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[2]/ul/li[6]'))).click() # Click Add More Chips
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[56]/div[2]/div[2]/div[2]/div[1]'))).click() # Click Max Chips
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[56]/div[2]/div[5]/button'))).click() # Click Okay
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[2]/input'))).send_keys("Get ready to give me my money back!") # Input Max Bid
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[3]/button'))).click() # Bid

    # Add an Introduction to the Bot
    def Introduction(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[2]/input'))).send_keys("How about a nice game of shovers?") # Input Max Bid
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[55]/div[5]/div[3]/button'))).click() # Bid


    def Play(self):
        while True:
            try:
                self.Shove()
            except Exception:
                try:
                    self.Call()
                except Exception:
                    try:
                        self.Buy_Back()
                    except Exception:
                        self.Play()
        
bot = PM_Demo_Bot()
bot.Fuck_Zach_Friends()
bot.Take_A_Seat()
bot.Introduction()
bot.Play()