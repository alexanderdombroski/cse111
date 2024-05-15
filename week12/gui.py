from tkinter import *
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius


def main():
    gui = Tk()
    
    frm_main = Frame(gui)
    gui.title("Circle Calculater")
    frm_main.pack(padx=4, pady=3, fill=BOTH, expand=1)

    populate_window(frm_main)

    gui.mainloop()

def populate_window(frame):
    area_label = Label(frame, text="?? square units") # makes label object
    radius_input = Entry(frame) # makes input object
    
    def clear(): # This function needs to be before the button that calls it, but after the area_label and radius input
        area_label.config(text="?? square units") # clears the label
        radius_input.delete(0, END) # clears the input
    
    clear_button = Button(frame, text="Clear", command=clear) # makes button object

    def calculate(event):
        try:
            float(radius_input.get())
        except:
            area_label.config(text="Not a number")
        else:
            area = calculate_circle_area(float(radius_input.get()))
            area_label.config(text=f"{area:.2f} square units")
    
    """ When binding to a key release, the related function will always run with an event parameter, so 
    calculate() needs an event parameter for it to function properly, even though it is not used.""" 
    radius_input.bind("<KeyRelease>", calculate)

    # grid section
    radius_input.grid(row=0,column=0)
    area_label.grid(row=0,column=1)
    clear_button.grid(row=1,column=0)


if __name__ == "__main__":
    main()