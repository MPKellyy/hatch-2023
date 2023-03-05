import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import Open_API


class optionFrame:
    def __init__(self, r):
        self.root = r

    def show_output(self, text_entry, dropdown_entry, frame):
        print("done")
        label1_2 = tk.Label(frame, text=Open_API.generate_text_on_topic(text_entry.get(), dropdown_entry.get()))
        label1_2.pack(pady=10)

    def get_file(self):
        filename = askopenfilename()

    def make_tab(self, tab_name, widget_text, options=None, need_input=False, need_upload=False):
        # Create a frame for the second tab
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text=tab_name)

        # Add widgets to the second tab
        label = tk.Label(frame, text=widget_text)
        label.pack(pady=10)

        if need_input:
            user_entry = tk.StringVar(frame)
            entry = tk.Entry(frame, textvariable=user_entry)
            entry.pack()

        if options is not None:
            dropdown_text = tk.StringVar(frame)
            dropdown_text.set(options[0]) # default
            dropdown = tk.OptionMenu(frame, dropdown_text, *options)
            dropdown.pack()

        if need_upload:
            upload_button = tk.Button(frame, text="Open File", command=self.get_file)
            upload_button.pack()

        button = tk.Button(frame, text="Lets go!", command=lambda: self.show_output(user_entry,
                                                                                     dropdown_text, frame))
        button.pack(pady=10)

    def construct(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create a frame for the first tab
        options = [
            "in simple terms.",
            "in detail with definitions.",
            "to me like I'm a kindergartener."
        ]
        self.make_tab("Generate Information", "Explain", options, need_input=True)
        self.make_tab("Generate Social Media Post", "Write me a post about", need_input=True)
        self.make_tab("Convert to Social Media Post", "Convert document to a post for", need_upload=True)
        self.make_tab("Summarize Paper", "Recap the contents of", need_upload=True)
        self.make_tab("Key Terms in Paper", "Find and define key terms in", need_upload=True)

root = tk.Tk()

o = optionFrame(root)
o.construct()

root.mainloop()
