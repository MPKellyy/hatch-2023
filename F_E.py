import tkinter as tk
from tkinter import ttk

import Open_API


class optionFrame:
    def __init__(self, r):
        self.root = r

    def show_output(self, text_entry, dropdown_entry, frame):
        print("done")
        label1_2 = tk.Label(frame, text=Open_API.generate_text_on_topic(text_entry.get(), dropdown_entry.get()))
        label1_2.pack(pady=10)

    def make_tab(self, tab_name, widget_text, options=None):
        # Create a frame for the second tab
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text=tab_name)

        # Add widgets to the second tab
        label = tk.Label(frame, text=widget_text)
        label.pack(pady=10)

        user_entry = tk.StringVar(frame)
        entry = tk.Entry(frame, textvariable=user_entry)
        entry.pack()

        if options is not None:
            dropdown_text = tk.StringVar(frame)
            dropdown_text.set(options[0]) # default
            dropdown = tk.OptionMenu(frame, dropdown_text, *options)
            dropdown.pack()

        button1 = tk.Button(frame, text="Lets go!", command=lambda: self.show_output(user_entry,
                                                                                     dropdown_text, frame))
        button1.pack(pady=10)


    def construct(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create a frame for the first tab
        options = [
            "in simple terms.",
            "in detail with definitions.",
            "to me like I'm a kindergartener."
        ]
        self.make_tab("Generate Information", "Explain", options)
        self.make_tab("Generate Social Media Post", "This is Tab 2!")
        self.make_tab("Tab 3", "This is Tab 2!")



root = tk.Tk()

o = optionFrame(root)
o.construct()

root.mainloop()
