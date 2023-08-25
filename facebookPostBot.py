import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui





def open_file_dialog():
    file_path = filedialog.askopenfilename()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, file_path)


def run():
    global email,password1,caption1,path
    email = email_entry.get()
    password1 = password_entry.get()
    caption1 = caption_entry.get()
    path = path_entry.get()


    # script_path = 'Selenium_script.py'

    # with open(script_path, 'r') as file:
    #  script_code = file.read()

    # try:
    #  exec(script_code)
    # except Exception as e:
    #  print(f"Error running {script_path}: {e}")
    chrome_options1 = Options()
    chrome_options1.add_argument("--disable-notifications")
    
    s = Service('C:\\Users\\zarwa\\Desktop\\MYPROGRAMS\\SELENIUM\\chromedriver.exe')
    driver = webdriver.Chrome(service=s,options=chrome_options1)

# Navigate to Facebook
    driver.get("https://www.facebook.com/")
    def login(email,password1):
        try:
        # Wait for the phone number input field to appear
         phone_number = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'email'))  # Use a more stable locator
         )
         phone_number.send_keys(email)

        # Locate and fill the password field
         password = driver.find_element(By.ID, 'pass')  # Use a more stable locator
         password.send_keys(password1)

        # Click the login button
         login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'login'))  # Use a more stable locator
         )
         login_button.click()
        # input()
        # time.sleep(11)
        # pyautogui.press('Tab')


        # pyautogui.press('Enter')
        except:
         print('there was an error login into facebook')


    def Post(caption1,path):
        try:

    
            btnplus=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'''/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[3]/div[2]/span/div''')))
            btnplus.click()

            btnpost=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'''/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]''')))
            btnpost.click()

            try:

                btn3=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div/div/i''')))
                btn3.click()

                btn4=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div''')))
                btn4.click()
            except :
                pass 

            caption=driver.find_element(By.XPATH,"""/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/p""")   
            caption.send_keys(caption1)

            btnadd=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'''/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div/span''')))

            btnadd.click()

            btnPV=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'''/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/span''')))
            btnPV.click()

        
        
        
            upload_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
            upload_input.send_keys(path)
            time.sleep(5) # this is mandatory while doing some thing with bot


            btnPost=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'''/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div''')))
            btnPost.click()
            time.sleep(30)
                


        # btnpost.send_keys(Keys.ENTER)




        except:
            print('there was an error uploading the picture')    

    login(email,password1)
    Post(caption1,path)        



    

# Create the main window
root = tk.Tk()
root.title("Facebook Selenium Automation")

# Create labels and entry fields
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Use 'show' to hide the password
password_entry.pack()

caption_label = tk.Label(root, text="Caption:")
caption_label.pack()
caption_entry = tk.Entry(root)
caption_entry.pack()

path_label = tk.Label(root, text="Image Path:")
path_label.pack()
path_entry = tk.Entry(root)
path_entry.pack()



browse_button = tk.Button(root, text="Browse",command=open_file_dialog)
browse_button.pack()

run_button = tk.Button(root, text="Run Selenium Script", command=run)
run_button.pack()

root.mainloop()



