import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import Open_API


class optionFrame:
    def __init__(self, r):
        self.root = r

        self.filepath = ""

    def nonpdf_output(self, text_entry, dropdown_entry, frame, function_name):
        if function_name == "generate_text_on_topic":
            label = tk.Label(frame, text=Open_API.generate_text_on_topic(text_entry.get(), dropdown_entry.get()))
        elif function_name == "generate_social_media_post":
            label = tk.Label(frame, text=Open_API.generate_social_media_post(dropdown_entry.get(), text_entry.get()))

        label.pack(pady=10)

    def pdf_output(self, frame, function_name):
        if function_name == "find_terms_paper":
            label = tk.Label(frame, text=Open_API.find_terms_paper(self.filepath))
        elif function_name == "summarize_paper":
            label = tk.Label(frame, text=Open_API.summarize_paper(self.filepath))
        elif function_name == "convert_to_post":
            label = tk.Label(frame, text=Open_API.convert_to_post(self.filepath))

        label.pack(pady=10)

    def update_filepath(self):
        self.filepath = askopenfilename()

    def make_tab(self, tab_name, widget_text, function_name, options=None, need_input=False, need_upload=False):
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
            upload_button = tk.Button(frame, text="Open File", command=self.update_filepath)
            upload_button.pack()
            button = tk.Button(frame, text="Lets go!",
                               command=lambda: self.pdf_output(self.filepath, frame, function_name))

        if need_upload is False:
            button = tk.Button(frame, text="Lets go!", command=lambda: self.nonpdf_output(user_entry, dropdown_text,
                                                                                    frame, function_name))

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
        self.make_tab("Generate Information", "Explain", function_name="generate_text_on_topic", options=options,
                      need_input=True)
        # TODO Make options for tab 2?
        self.make_tab("Generate Social Media Post", "Write me a post about", function_name="generate_social_media_post",
                      need_input=True)
        self.make_tab("Convert to Social Media Post", "Convert document to a media post",
                      function_name="convert_to_post", need_upload=True)
        self.make_tab("Summarize Paper", "Recap the contents of", function_name="summarize_paper", need_upload=True)
        self.make_tab("Key Terms in Paper", "Find and define key terms in", function_name="find_terms_paper",
                      need_upload=True)
        # TODO add script generation

root = tk.Tk()

o = optionFrame(root)
o.construct()

root.mainloop()
