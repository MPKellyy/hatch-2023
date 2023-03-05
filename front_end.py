import tkinter as tk
import tkinter.ttk as ttk




def print_selection():
    selected_option = var.get()
    print(f"You selected {selected_option}.")

def button1_clicked():
    print("Button 1 clicked.")

def button2_clicked():
    print("Button 2 clicked.")
    frame1.pack_forget()

root = tk.Tk()
root2 = tk.Tk()


frame1 = tk.Frame(master=root2, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=root2, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=root2, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


window_text = tk.Label(text="Click the buttons, if you dare",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black)
    width=1000,
    height=10)
window_text.pack()

# Create a variable to hold the selected option
var = tk.StringVar(root)

# Create a list of options for the drop-down menu
options = ["Option 1", "Option 2", "Option 3"]

# Set the default selected option
var.set(options[0])

# Create the drop-down menu
drop_down_menu = tk.OptionMenu(root, var, *options)

# Create a button to print the selected option
print_button = tk.Button(root, text="Print Selection", command=print_selection)

# Create two buttons
button1 = tk.Button(root, text="Button 1", command=button1_clicked,
    width=25,
    height=5,
    bg="purple",
    fg="yellow",)
button2 = tk.Button(root, text="Button 2", command=button2_clicked,
    width=25,
    height=5,
    bg="black",
    fg="yellow",)

# Add the drop-down menu, print button, and buttons to the root window
drop_down_menu.pack()
print_button.pack()
button1.place(x=400, y=50) # use .place instead of .pack() to specify location
button2.place(x=1000, y=50)

# requests user input
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

root.mainloop()



