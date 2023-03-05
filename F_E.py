import tkinter as tk
from tkinter import ttk

import Open_API


class optionFrame:
    def __init__(self, r):
        self.root = r

    def show_output(self, label_text, text_entry, dropdown_entry, frame):
        print("done")
        label1_2 = tk.Label(frame, text=Open_API.generate_text_on_topic(text_entry.get(), dropdown_entry.get()))
        label1_2.pack(pady=10)

    def construct(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        # Create a frame for the first tab
        frame1 = tk.Frame(notebook)
        notebook.add(frame1, text="Generate Information")

        # Add widgets to the first tab
        label1_1 = tk.Label(frame1, text="Explain")
        label1_1.pack(pady=10)

        user_entry1 = tk.StringVar(frame1)
        entry1 = tk.Entry(frame1, textvariable=user_entry1)
        entry1.pack()

        options = [
            "in simple terms.",
            "in detail with definitions.",
            "to me like I'm a kindergartener."
        ]

        dropdown1_text = tk.StringVar(frame1)
        dropdown1_text.set(options[0]) # default

        dropdown1 = tk.OptionMenu(frame1, dropdown1_text, *options)
        dropdown1.pack()

        button1 = tk.Button(frame1, text="Lets go!", command=lambda: self.show_output(user_entry1,
                                                                                     dropdown1_text, frame1))
        button1.pack(pady=10)
        ##############################################################################
        # Create a frame for the second tab
        frame2 = tk.Frame(notebook)
        notebook.add(frame2, text="Generate Social Media Post")

        # Add widgets to the second tab
        label2 = tk.Label(frame2, text="This is Tab 2!")
        label2.pack(pady=10)

        button2 = tk.Button(frame2, text="Lets go!")
        button2.pack(pady=10)

        # Create a frame for the third tab
        frame3 = tk.Frame(notebook)
        notebook.add(frame3, text="Tab 3")

        # Add widgets to the third tab
        label3 = tk.Label(frame3, text="This is Tab 3!")
        label3.pack(pady=10)

        button3 = tk.Button(frame3, text="Lets go!")
        button3.pack(pady=10)


root = tk.Tk()

o = optionFrame(root)
o.construct()

root.mainloop()
