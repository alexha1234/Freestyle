import tkinter

#
# INITIALIZE A NEW GUI WINDOW
#

window = tkinter.Tk()

#
# INITIALIZE SOME USER INTERFACE COMPONENTS
#

# MESSAGE

my_message = tkinter.Message(text="Hi. Welcome to the restaurant chooser!", width=1000)

# ENTRY (TEXT INPUT) WITH LABEL

my_cuisine = tkinter.Label(text="Input your desired cuisine:")
cuisine_value = tkinter.StringVar()
cuisine = tkinter.Entry(textvariable=cuisine_value)
#
my_zip = tkinter.Label(text="Input your zip code:")
zip_value = tkinter.StringVar()
zip = tkinter.Entry(textvariable=zip_value)
#

# BUTTON

def handle_button_click():
    print("------------------------------")
    print("NICE. YOU CLICKED THE BUTTON")
    print("THE ENTRY'S INPUT VALUE IS:", cuisine.get())
    print("THE ENTRY'S INPUT VALUE IS:", zip.get())

my_button = tkinter.Button(text="Click Me", command=handle_button_click)

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

cuisine.pack()
zip.pack()

my_button.pack()

window.mainloop()