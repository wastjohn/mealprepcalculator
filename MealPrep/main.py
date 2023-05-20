"""
File: main.py

This file contains the script for the meal prep shopping list calculator.

Spring 2023
Author: Will St. John
"""
# import modules
import tkinter as tk
from tkinter import filedialog

# main gui
class calendar:
    def __init__(self) -> None:
        self.rootwin = tk.Tk()
        self.rootwin.title('One Week Meal Prep Shopping List Calculator')

        # information frame
        self.infoframe = tk.Frame()
        self.infoframe.pack()

        # week frame
        self.weekframe = tk.Frame()
        self.weekframe.pack(fill=tk.BOTH, expand=True)

        # inventory frame
        self.inventory = tk.Frame()
        self.inventory.pack(fill=tk.BOTH, expand=True)
        self.inventory_list = {}

        # shoppping list frame
        self.sl_frame = tk.Frame()
        self.sl_frame.pack()
        self.sl_list = {}

        # exit frame
        self.exitframe = tk.Frame()
        self.exitframe.pack()

        # info label and text file template example
        self.info_label = tk.Label(master=self.infoframe, text='Insert Text Files to the Associated Days')
        self.info_label.pack()
        self.example_button = tk.Button(master=self.infoframe, text='See Example Text File', command=self.show_example)
        self.example_button.pack()

        # shopping list
        self.get_list_button = tk.Button(master=self.sl_frame, text='Get Shopping List', command=self.get_shopping_list)
        self.get_list_button.pack()
        self.shopping_list = tk.Text(master=self.sl_frame, height=5)
        self.shopping_list.pack(fill=tk.BOTH)

        # weekday frame creation
        self.sunday = tk.Frame(master=self.weekframe, width=100, height=200, bg='red')
        self.sunday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.monday = tk.Frame(master=self.weekframe, width=100, height=200, bg='orange')
        self.monday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.tuesday = tk.Frame(master=self.weekframe, width=100, height=200, bg='yellow')
        self.tuesday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.wednesday = tk.Frame(master=self.weekframe, width=100, height=200, bg='green')
        self.wednesday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.thursday = tk.Frame(master=self.weekframe, width=100, height=200, bg='blue')
        self.thursday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.friday = tk.Frame(master=self.weekframe, width=100, height=200, bg='purple')
        self.friday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.saturday = tk.Frame(master=self.weekframe, width=100, height=200, bg='violet')
        self.saturday.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # weekday labels and buttons
        self.sunday_label = tk.Label(master=self.sunday, text='Sunday')
        self.sunday_label.pack(fill=tk.X)
        self.sunday_button = tk.Button(master=self.sunday, text='Insert txt file', command=self.select_file_sunday)
        self.sunday_button.pack(fill=tk.X, pady=10)
        self.sunday_desc = tk.Label(master=self.sunday, text='')
        self.sunday_desc.pack(fill=tk.X)

        self.monday_label = tk.Label(master=self.monday, text='Monday')
        self.monday_label.pack(fill=tk.X)
        self.monday_button = tk.Button(master=self.monday, text='Insert txt file', command=self.select_file_monday)
        self.monday_button.pack(fill=tk.X, pady=10)
        self.monday_desc = tk.Label(master=self.monday, text='')
        self.monday_desc.pack(fill=tk.X)

        self.tuesday_label = tk.Label(master=self.tuesday, text='Tuesday')
        self.tuesday_label.pack(fill=tk.X)
        self.tuesday_button = tk.Button(master=self.tuesday, text='Insert txt file', command=self.select_file_tuesday)
        self.tuesday_button.pack(fill=tk.X, pady=10)
        self.tuesday_desc = tk.Label(master=self.tuesday, text='')
        self.tuesday_desc.pack(fill=tk.X)

        self.wednesday_label = tk.Label(master=self.wednesday, text='Wednesday')
        self.wednesday_label.pack(fill=tk.X)
        self.wednesday_button = tk.Button(master=self.wednesday, text='Insert txt file', command=self.select_file_wednesday)
        self.wednesday_button.pack(fill=tk.X, pady=10)
        self.wednesday_desc = tk.Label(master=self.wednesday, text='')
        self.wednesday_desc.pack(fill=tk.X)

        self.thursday_label = tk.Label(master=self.thursday, text='Thursday')
        self.thursday_label.pack(fill=tk.X)
        self.thursday_button = tk.Button(master=self.thursday, text='Insert txt file', command=self.select_file_thursday)
        self.thursday_button.pack(fill=tk.X, pady=10)
        self.thursday_desc = tk.Label(master=self.thursday, text='')
        self.thursday_desc.pack(fill=tk.X)

        self.friday_label = tk.Label(master=self.friday, text='Friday')
        self.friday_label.pack(fill=tk.X)
        self.friday_button = tk.Button(master=self.friday, text='Insert txt file', command=self.select_file_friday)
        self.friday_button.pack(fill=tk.X, pady=10)
        self.friday_desc = tk.Label(master=self.friday, text='')
        self.friday_desc.pack(fill=tk.X)

        self.saturday_label = tk.Label(master=self.saturday, text='Saturday')
        self.saturday_label.pack(fill=tk.X)
        self.saturday_button = tk.Button(master=self.saturday, text='Insert txt file', command=self.select_file_saturday)
        self.saturday_button.pack(fill=tk.X, pady=10)
        self.saturday_desc = tk.Label(master=self.saturday, text='')
        self.saturday_desc.pack(fill=tk.X)

        # inventory textbox and button
        self.inventory_label = tk.Label(master=self.inventory, text='Input items already at home')
        self.inventory_label.pack()
        self.inventory_text = tk.Text(master=self.inventory, height=5)
        self.inventory_text.pack()
        self.inventory_button = tk.Button(master=self.inventory, text='Add to inventory', command=self.get_inventory)
        self.inventory_button.pack()


        # exit button
        self.exit_button = tk.Button(master=self.exitframe, text='Exit', command=exit)
        self.exit_button.pack(side=tk.BOTTOM)

    # select files when a button is pressed
    def select_file_sunday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.sunday_desc.config(text=desc)
    
    def select_file_monday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.monday_desc.config(text=desc)
    
    def select_file_tuesday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.tuesday_desc.config(text=desc)
    
    def select_file_wednesday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.wednesday_desc.config(text=desc)
    
    def select_file_thursday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.thursday_desc.config(text=desc)
    
    def select_file_friday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.friday_desc.config(text=desc)
    
    def select_file_saturday(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        ingredients = self.printIng(self.filename)
        desc = ''
        for i in ingredients:
            desc += i + '\n'
            if i not in self.sl_list:
                self.sl_list[i] = 1
            else:
                self.sl_list[i] += 1
        self.saturday_desc.config(text=desc)

    # example text file
    def show_example(self):
        self.example_window = tk.Toplevel()
        self.label = tk.Label(self.example_window, text='Meal Name: Blah Blah Blah\nIngredients:\n-asdf\n-asdf\n-asdf\nDirections:\n1\tasdf\n2\tasdf')
        self.label.pack(side=tk.LEFT)

    # starting the gui
    def run(self):
        self.rootwin.mainloop()

    # exiting the gui
    def exit(self):
        self.rootwin.destroy()

    # printing the ingredients
    def printIng(self, filepath: str):
        # open the file and read the lines
        file = open(filepath, 'r')
        lines = file.readlines(0)

        # reomove new lines
        while '\n' in lines:
            lines.remove('\n')

        # find the ingredients
        start = lines.index('Ingredients:\n')
        stop = lines.index('Directions:\n')
        ingredients = lines[start+1:stop]

        # making the ingredients more readable
        ingred = []
        for item in ingredients:
            a = item.strip('- \n')
            ingred.append(a)
        file.close()

        return ingred
    
    def get_shopping_list(self):
        self.shopping_list.delete('1.0', 'end')
        for i in self.sl_list:
            self.shopping_list.insert(tk.END, i + '\t enough for '  + str(self.sl_list[i]) + ' meal(s)\n')
        
    def get_inventory(self):
        input = self.inventory_text.get('1.0', tk.END)
        print(input)
        
    
    
    

# initialize and run a calendar gui
gui = calendar()
gui.run()

# ----------Testing Playground----------



# TODO: Look into text widget for displaying ingredients for each meal
