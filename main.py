from tkinter import *
import calendar

# To show the given Year
def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the Year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=5, column=1, padx=20)
    gui.mainloop()

new = Tk()
new.config(background='grey')
new.title("Calender")
new.geometry("250x140")
cal = Label(new, text="Calender", bg='grey', font=("times", 28, "bold"))
year = Label(new, text="Enter Year", bg='dark grey')
year_field = Entry(new)
button = Button(new, text='Show Calender', fg='Black', bg='Blue', command=showCalender)


# Putting Widgets in position
cal.grid(row=1, column=1)
year.grid(row=2, column=1)
year_field.grid(row=3,column=1)
button.grid(row=4, column=1)
new.mainloop()