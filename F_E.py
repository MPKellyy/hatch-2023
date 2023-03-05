import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import Open_API


class OptionFrame:
    def __init__(self, r):
        self.root = r
        self.notebook = ttk.Notebook(self.root)

        self.filepath = ""

    def nonpdf_output(self, text_entry, dropdown_entry, frame, function_name):
        if function_name == "generate_text_on_topic":
            label = tk.Label(frame, text=Open_API.generate_text_on_topic(text_entry.get(), dropdown_entry.get()),
                             wraplength=frame.winfo_width() - frame.winfo_width()/10, justify="center")
        elif function_name == "generate_social_media_post":
            label = tk.Label(frame, text=Open_API.generate_social_media_post(dropdown_entry.get(), text_entry.get()),
                             wraplength=frame.winfo_width() - frame.winfo_width()/10, justify="center")
        else:  # generate script
            label = tk.Label(frame, text=Open_API.generate_script(text_entry.get()),
                             wraplength=frame.winfo_width() - frame.winfo_width() / 10, justify="center")

        if frame.grid_slaves(3, 0).__len__() != 0:
            temp = frame.grid_slaves(3, 0)[0]
            temp.grid_forget()
            temp = label
            temp.grid(row=3, column=0, padx=frame.winfo_width()/20, pady=2, columnspan=frame.grid_size()[0])
        else:
            label.grid(row=3, column=0, padx=frame.winfo_width()/20, pady=2, columnspan=frame.grid_size()[0])

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
        label.grid(row=0, column=0, pady=2, sticky='E')

        if function_name == "generate_social_media_post":
            label2 = tk.Label(frame, text="in the format of a:")
            label2.grid(row=1, column=0, pady=2, sticky='E')

        if need_input:
            user_entry = tk.StringVar(frame)
            entry = tk.Entry(frame, textvariable=user_entry)
            entry.grid(row=0, column=1, pady=2, sticky="W")

        dropdown_text = tk.StringVar(frame)
        if options is not None:
            dropdown_text.set(options[0]) # default
            dropdown = tk.OptionMenu(frame, dropdown_text, *options)
            if frame.grid_slaves(1, 0).__len__() != 0:
                dropdown.grid(row=1, column=1, pady=2, sticky="W")
            else:
                dropdown.grid(row=1, column=0, pady=2, columnspan=frame.grid_size()[0])

#
#
#   incorrect? self isn't actually passed???
#
#
        if need_upload:
            upload_button = tk.Button(frame, text="Open File", command=self.update_filepath)
            upload_button.grid(row=1, column=0, pady=2)
            button = tk.Button(frame, text="Lets go!",
                               command=lambda: self.pdf_output(self.filepath, frame, function_name))

        else:
            button = tk.Button(frame, text="Lets go!", command=lambda: self.nonpdf_output(user_entry, dropdown_text,
                                                                                    frame, function_name))

        button.grid(row=2, column=0, pady=2, columnspan=frame.grid_size()[0])

    def construct(self):
        self.notebook.pack(fill="both", expand=True)

        # Options for dropdown on "Generate Information"
        options1 = [
            "in simple terms.",
            "in detail with definitions.",
            "in terms a kindergartener would understand.",
            "as if I had no prior knowledge on it."
        ]

        options2 = [
            "tweet",
            "instagram post",
            "blog post",
            "facebook post",
            "linked-in post"
        ]

        self.make_tab("Generate Information", "Explain", function_name="generate_text_on_topic", options=options1,
                      need_input=True)
        # TODO Make options for tab 2? -> DONE
        self.make_tab("Generate Social Media Post", "Write me a social media post about",
                      function_name="generate_social_media_post", options=options2, need_input=True)
        self.make_tab("Generate Presentation Script", "Write me a script for a presentation on",
                      function_name="generate_script", need_input=True)
        self.make_tab("Convert to Social Media Post", "Convert document to a media post",
                      function_name="convert_to_post", need_upload=True)
        self.make_tab("Summarize Paper", "Recap the contents of", function_name="summarize_paper", need_upload=True)
        self.make_tab("Key Terms in Paper", "Find and define key terms in", function_name="find_terms_paper",
                      need_upload=True)
        # TODO add script generation -> DONE
