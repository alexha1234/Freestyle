

from yelpapi import YelpAPI
from PIL import ImageTk, Image
import os
from dotenv import load_dotenv
import tkinter

load_dotenv()
api_key = os.getenv("api_key", default="OOPS, please set env var called 'SENDGRID_API_KEY'")


#
# INITIALIZE A NEW GUI WINDOW
#
# help from https://www.tutorialspoint.com/python/tk_message.htm 
window = tkinter.Tk()
window.geometry("620x570")
window.title('Yelp Me Pick') # window title and size

#
# INITIALIZE SOME USER INTERFACE COMPONENTS
#
# logo image in window
image = Image.open("images/yelp.jpeg")
tkpi = ImageTk.PhotoImage(image)
label_image = tkinter.Label(window, image=tkpi)
label_image.image = tkpi
label_image.place(x=0,y=100)

# MESSAGE

my_message = tkinter.Message(text="Hi, welcome to the 'Yelp Me Pick' restaurant chooser!\n Please input your cuisine preference followed by your zipcode.", justify = 'center' , width=1000)


# ENTRY (TEXT INPUT) WITH LABEL

my_cuisine = tkinter.Label(text="Input your desired cuisine:")
cuisine_value = tkinter.StringVar()
cuisine_entry = tkinter.Entry(textvariable=cuisine_value)
#
my_zip = tkinter.Label(text="Input your zip code:")
zip_value = tkinter.StringVar()
zip_code_entry = tkinter.Entry(textvariable=zip_value)
#

def addToScreen(output):
    results = tkinter.Label(text=output, width=1000, bg="#000", fg="#fff")
    results.pack()

# BUTTON

def handle_button_click():
    print(zip_code_entry.get())
    print(cuisine_entry.get())
    zip_code = zip_code_entry.get()
    cuisine = cuisine_entry.get()
    with YelpAPI(api_key) as yelp_api:
        search_results = yelp_api.search_query(location = zip_code, term = cuisine, sort_by= 'rating', limit = 5, radius=2000)
    for business in search_results['businesses']:
        address_line1 = business['location']['display_address'][0]
        address_line2 = business['location']['display_address'][1]
        address = address_line1 + ", " + address_line2
        output1 = str("Name: " + str(business['name'])),
        output2 = str("Address: " + address)
        output3 = str("Rating: " + str(business['rating']))
        print(output1, output2, output3)
        addToScreen(output1)
        addToScreen(output2)
        addToScreen(output3)
        addToScreen(" ")


my_button = tkinter.Button(text="Submit", command=handle_button_click)

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

cuisine_entry.pack()
zip_code_entry.pack()

my_button.pack()

window.mainloop()