import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create a frame for the first tab
frame1 = tk.Frame(notebook)
notebook.add(frame1, text="Generate Information")

# Add widgets to the first tab
label1 = tk.Label(frame1, text="Explain")
label1.pack(pady=10)

button1 = tk.Button(frame1, text="Click me!")
button1.pack(pady=10)
##############################################################################
# Create a frame for the second tab
frame2 = tk.Frame(notebook)
notebook.add(frame2, text="Generate Social Media Post")

# Add widgets to the second tab
label2 = tk.Label(frame2, text="This is Tab 2!")
label2.pack(pady=10)

button2 = tk.Button(frame2, text="Click me!")
button2.pack(pady=10)

# Create a frame for the third tab
frame3 = tk.Frame(notebook)
notebook.add(frame3, text="Tab 3")

# Add widgets to the third tab
label3 = tk.Label(frame3, text="This is Tab 3!")
label3.pack(pady=10)

button3 = tk.Button(frame3, text="Click me!")
button3.pack(pady=10)

root.mainloop()
