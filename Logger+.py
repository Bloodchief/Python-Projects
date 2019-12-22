import sys
import pysnow
from tkinter import *
from tkinter import messagebox

#REST API
#Need to install requests package for python
import requests

# Set the request parameters
url = 'https://vology.service-now.com/api/now/table/problem?sysparm_limit=1/'

# Eg. User name="username", Password="password" for this code sample.
user = 'mbarber@vology.com'
pwd = 'xxx'

# Set proper headers
headers = {"Accept":"application/xml"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers)


# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
    exit()

# Decode the XML response into a dictionary and use the data
print(response.content)


#Begin GUI
##root = Tk()
#name of the GUI is set as root

##root.title('logger+')
#sets title for program

##root.geometry("500x500")
#defines the default window wize at 500x500

##helloLab = Label(text="logger+")
##helloLab.pack()
#label for object



##def passResetButton():
    ##messagebox.showinfo("Success","Password has been reset.")
#defines a button, first is title, then contents on messagebox

##B = Button(root, text="Password Reset", command = passResetButton)
##B.pack()
#creates the actual button and calls back to the function passResetButton

##root.mainloop()
