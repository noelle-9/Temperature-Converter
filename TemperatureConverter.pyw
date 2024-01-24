# Name: Noelle Dacayo
# Date: December 16th, 2022
# App Name: Temperature Converter
# Description: App that will convert temperatures depending on whatever the user wants to convert
# hi hi (^^ )/

# Imports
from tkinter import * # Import the tkinter module
from tkinter.ttk import * # Replaces the W95 look with a modern one
from tkinter import messagebox # Pop-up message

# CONSTANTS
# ------------------------------------------------------------------------------------------------------------------------------------
CONVERT = ("Celsius", "Farenheit", "Kelvin")


# Defining functions
# ------------------------------------------------------------------------------------------------------------------------------------
# Conversion calculations
# This is a massive block and it's super janky. I don't have the time to try fix it if there was a way to shorten this so it's staying janky haha
def converting():
    # Tries to convert the user's input into a float
    temp = input_text.get()
    try:
        temp = float(temp)
        numeric = True
    except:
        numeric = False
    # Displays an error message if it's not a numerical input
    if numeric == False:
        messagebox.showerror(title="Error!", message="I can't convert something that isn't numeric or blank.\nI may be an all knowing bot, but I have limits too.\n")
   

    # Will only execut if input is numerical
    else:
        # User entered the same units to convert like a goof
        if unit_selection.get() and convert_selection.get() == CONVERT[0] or CONVERT[1] or CONVERT[2]:
            output_text.set(temp)
        if convert_selection.get() == CONVERT[0]:
            unit_text.set("°C")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 20:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 20:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------

        if convert_selection.get() == CONVERT[1]:
            unit_text.set("°F")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 68:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 68:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------

        if convert_selection.get() == CONVERT[2]:
            unit_text.set("°K")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 293.15:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 293.15:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------


        # celsius->fahrenheit
        if unit_selection.get() == CONVERT[0] and convert_selection.get() == CONVERT[1]:
            output_text.set((temp * 9/5) + 32)
            unit_text.set("°F")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
    
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 68:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 68:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------

        # cel->kel
        if unit_selection.get() == CONVERT[0] and convert_selection.get() == CONVERT[2]:
            output_text.set(temp + 273.15)
            unit_text.set("°K")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 293.15:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 293.15:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------

        # fahr->cel
        if unit_selection.get() == CONVERT[1] and convert_selection.get() == CONVERT[0]:
            output_text.set((temp - 32) * 5/9)
            unit_text.set("°C")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 20:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 20:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
                # ------------------------------------------------------------------------------------------------------------------------------------

        # fahr->kel
        if unit_selection.get() == CONVERT[1] and convert_selection.get() == CONVERT[2]:
            output_text.set((temp - 32) * 5/9 + 273.15)
            unit_text.set("°K")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 293.15:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 293.15:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------

        # kel->cel
        if unit_selection.get() == CONVERT[2] and convert_selection.get() == CONVERT[0]:
            output_text.set(temp - 273.15)
            unit_text.set("°C")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 20:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 20:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------

        #kel->fahr
        if unit_selection.get() == CONVERT[2] and convert_selection.get() == CONVERT[1]:
            output_text.set((temp - 273.15) * 9/5 + 32)
            unit_text.set("°F")
            # ------------------------------------------------------------------------------------------------------------------------------------
            # The cause of the size, changes the background of the app depending on the temperature
            # ------------------------------------------------------------------------------------------------------------------------------------
            wasting_time = output_text.get()
            try:
                wasting_time = float(wasting_time)
                numeric = True
            except:
                numeric = False
            if numeric == True and wasting_time < 68:
                window.configure         (bg='#00FFFF')
                output_label.configure   (background='#00FFFF')
                output_entry.configure   (background='#00FFFF')
                input_label.configure    (background='#00FFFF')
                convert_label.configure  (background='#00FFFF')

            elif wasting_time > 68:
                window.configure         (bg='#FF6400')
                output_label.configure   (background='#FF6400')
                output_entry.configure   (background='#FF6400')
                input_label.configure    (background='#FF6400')
                convert_label.configure  (background='#FF6400')
            # ------------------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------------------
# Allows the user to user to use [Enter] instead of pressing the Convert button and allows the user to use [ESC] to reset everything to default
def key_handler(event:Event):
    """
    Handles key press
    """
    if event.keysym == "Return": # R is uppercase - enter key
        converting()
    elif event.keysym == "Escape": # Esc key
        clear_click()
   
# ------------------------------------------------------------------------------------------------------------------------------------
# Defining what the [Clear] button will do when clicked
def clear_click():
    """
    Resets all the text and options back to the default setting
    """
    unit_selection.set(CONVERT[0])
    convert_selection.set(CONVERT[1])
    input_text.set("21.1")
    output_text.set("70")
    unit_text.set("°F")
    window.configure(bg="#F0F0F0")
    window.configure       (background="#F0F0F0")
    output_label.configure (background="#F0F0F0")
    output_entry.configure (background="#F0F0F0")
    input_label.configure  (background="#F0F0F0")
    convert_label.configure(background="#F0F0F0")


# Set up the window
# ------------------------------------------------------------------------------------------------------------------------------------
# Create a window
window = Tk()                                         # Create a window
window.title("Temperature Converter - Noelle Dacayo") # Changes the title
window.iconbitmap("temp.ico")                         # Changes the window's icon
window.resizable(width=False, height=False)           # Not resizable
window.bind("<Key>", key_handler)                     # Allows key presses


# ------------------------------------------------------------------------------------------------------------------------------------
# Create a frame - Will hold all the other widgets
input_frame = Frame()
mid_frame = Frame()
output_frame = Frame()

# ------------------------------------------------------------------------------------------------------------------------------------
# Input
input_text = Variable()
input_text.set("21.1")
input_label = Label(input_frame, font="Onyx 25", text="Temperature Converter")
input_entry = Entry(input_frame, font="Onyx 17", justify=CENTER, textvariable=input_text, width=25)

# ------------------------------------------------------------------------------------------------------------------------------------
# Dropdown
unit_selection = Variable() 
unit_selection.set(CONVERT[0])
unit_combobox = Combobox(mid_frame, values=CONVERT, width=35, textvariable=unit_selection, state="readonly")
convert_selection = Variable() 
convert_selection.set(CONVERT[1])
convert_combobox = Combobox(mid_frame, values=CONVERT, width=35, textvariable=convert_selection, state="readonly")
convert_label = Label(mid_frame, font="Onyx 25", text="                    To", width=29)


# ------------------------------------------------------------------------------------------------------------------------------------
# Button
convert_button = Button(mid_frame, text="Convert", width=15, command=converting)
clear_button = Button(mid_frame, text="Clear", command=clear_click)


# ------------------------------------------------------------------------------------------------------------------------------------
# Output
output_text = Variable()
output_text.set("70")
output_label = Label(output_frame, font="Onyx 25", text="                The Temperature is", width=38)
output_entry = Entry(output_frame, font="Onyx 55", justify=CENTER, state="readonly", textvariable=output_text, width=10)
# 
unit_text = Variable()
unit_text.set("°F")
unit_entry = Entry(output_frame, font="Onyx 55", justify=CENTER, state="readonly", textvariable=unit_text, width=4)


# Pack pack pack pack pack
# ------------------------------------------------------------------------------------------------------------------------------------
input_frame.pack(side="left", padx=10,pady=(10, 50))
output_frame.pack(side="right", padx=10, pady=(10, 40))
mid_frame.pack(padx=10,pady=(50, 20))
input_label.pack(anchor=CENTER)
output_label.pack()
input_entry.pack(anchor="w")
unit_entry.pack(side="right")
output_entry.pack(side="right")
unit_combobox.pack(anchor=CENTER)
convert_label.pack(anchor=CENTER)
convert_combobox.pack(anchor=CENTER)
convert_button.pack(side="left")
clear_button.pack(side="right")



# Make the window visible
window.mainloop()

