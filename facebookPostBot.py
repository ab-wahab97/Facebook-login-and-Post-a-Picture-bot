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
from tkinter import *





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
    path1=path.replace('/','//')
    print(path1)


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
            time.sleep(20)
            

        except:
            print('there was an error uploading the picture')    

    login(email,password1)
    Post(caption1,path)        



#GUI    

root = tk.Tk()
root.title("Facebook Bot")
root.iconbitmap('C:\\Users\\zarwa\\Desktop\\currently working\\icon.ico')

photo=PhotoImage(file='C:\\Users\\zarwa\\Desktop\\currently working\\logo1.png')

logo_label=tk.Label(image=photo,background='#1877F2')
logo_label.pack(side=TOP)


# Set the window size and make labels bold
root.geometry("610x370")
root.config(bg='#1877F2')
bold_font = ("TkDefaultFont", 10, "bold")
root.resizable(False,False)

# Create a big label at the top
title_label = tk.Label(root, text="FACEBOOK BOT",bg="black",fg="white", font=("TkDefaultFont", 14, "bold"))
title_label.pack(pady=10)

# Create a frame for better organization and fill the window
frame = tk.Frame(root,bg='#1877F2', padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Labels and entry fields with larger font
tk.Label(frame, text="Email:", font=bold_font,relief=RAISED).grid(row=0, column=0, sticky="w",)
email_entry = tk.Entry(frame, font=bold_font,width=50,bd=3)
email_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

tk.Label(frame, text="Password:", font=bold_font,relief=RAISED).grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(frame, show="*", font=bold_font,width=50,bd=3)
password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Label(frame, text="Caption:", font=bold_font,relief=RAISED).grid(row=2, column=0, sticky="w")
caption_entry = tk.Entry(frame, font=bold_font,width=50,bd=3)
caption_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(frame, text="Image Path:", font=bold_font,relief=RAISED).grid(row=3, column=0, sticky="w")
path_entry = tk.Entry(frame, font=bold_font,width=50,bd=3)
path_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

browse_button = tk.Button(frame, text="Browse",bg='yellow',width=12,font=("TkDefaultFont", 10, "bold"), command=open_file_dialog)
browse_button.grid(row=3, column=2, padx=10, pady=5)

run_button = tk.Button(frame, text="Run",font=("TkDefaultFont", 10, "bold"),fg='black',bg='light green',width=20, command=run)
run_button.grid(row=4, columnspan=3, padx=10, pady=10)

title_label = tk.Label(frame, text="By Abdul Wahab",bg="#1877F2",fg="white", font=("TkDefaultFont", 8, "bold"))
title_label.grid(row=5,columnspan=3,sticky=E,pady=10)

root.mainloop()
