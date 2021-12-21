import tkinter as tk
from tkinter import filedialog
import journal_utils.csv_reader as csv_reader


class MainUI(tk.Frame):
    """This class models a UI"""

    def __init__(self, main_system, master=None):
        super().__init__(master)

        # master root
        self.master = master
        self.pack()

        # member variables
        self.main_system = main_system
        self.file_path = None
        self.input_file_path = None

        # upload button
        self.upload_button = tk.Button(self, text="Browse", command=self.upload_file)
        self.upload_button.grid(row=1, column=1)

        # csv file label
        self.file_var = tk.StringVar()
        self.file_var.set("no file")
        self.file_label = tk.Label(self, textvariable=self.file_var, bg='cyan2', height=1, width=30)
        self.file_label.grid(row=1, column=2)

        # email label
        self.email_label = tk.Label(self, text='Email:')
        self.email_label.grid(row=2, column=1)

        # email textfield
        self.email_textfield = tk.Text(self, bd=1, bg='yellow', height=1, width=40)
        self.email_textfield.grid(row=2, column=2)

        # search button
        self.search_button = tk.Button(self, text="Search Articles", command=self.search_article)
        self.search_button.grid(row=3, column=1)

        # download button
        self.download_button = tk.Button(self, text="Download", command=self.download_file)
        self.download_button.grid(row=3, column=2)

        # exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.grid(row=3, column=3)

        # email button
        self.email_button = tk.Button(self, text='Send', command=self.send_email)
        self.email_button.grid(row=4, column=1)

        # reality check button
        self.reality_check_button = tk.Button(self, text='Reality Check', command=self.check_reality)
        self.reality_check_button.grid(row=4, column=2)

    def create_widget(self):
        """
        Creates all the widgets needed for UI
        :return:
        """
        self.top_frame = tk.Frame(self, width=500, height=500)
        self.mid_frame = tk.Frame(self, width=500, height=100)
        self.buttom_frame = tk.Frame(self)
        self.first_label = tk.Label(self, text="Journal Reality Checking")

        self.content_field = tk.Text(self.top_frame)
        self.ready_label = tk.Entry(self.mid_frame)

        self.upload_button = tk.Button(self.buttom_frame, text="Browse File", command=self.upload_file)
        self.search_button = tk.Button(self.buttom_frame, text="Search Articles", command=self.search_article)
        self.download_button = tk.Button(self.buttom_frame, text="Download", command=self.download_file)
        self.exit_button = tk.Button(self.buttom_frame, text="Exit", command=self.quit)

        self.ready_label.pack()
        self.mid_frame.pack()
        self.top_frame.pack()

        self.buttom_frame.pack()
        self.first_label.pack()

        self.content_field.pack()
        self.upload_button.pack(side=tk.LEFT)
        self.search_button.pack(side=tk.LEFT)
        self.download_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.RIGHT)

    def upload_file(self):
        """
        Allows a user to browse a csv file and upload it.
        :return:
        """
        self.input_file_path = filedialog.askopenfilename(initialdir="currdir", title="Select File",
                                                          filetypes=(("csv files", "*.csv"),
                                                                     ("all files", "*.*")))
        print(self.input_file_path)

        res2 = self.input_file_path.split('/')[-1]
        print(res2)
        self.file_var.set(res2)
        self.main_system.update('FILE_UPLOADED')

    def download_file(self):
        """
        This method is fired when a download button is clicked.
        :return:
        """
        self.main_system.update('DOWNLOAD_CLICKED')

    def search_article(self):
        """
        This method is fired whtn
        :return:
        """
        self.main_system.update('SEARCH_CLICKED')

    def send_email(self):
        self.main_system.update('EMAIL_CLICKED')

    def check_reality(self):
        self.main_system.update('REALITY_CHECK_CLICKED')

    def print_message(self):
        print('message')


if __name__ == '__main__':
    root = tk.Tk()
    app = MainUI(master=root)
    app.mainloop()
