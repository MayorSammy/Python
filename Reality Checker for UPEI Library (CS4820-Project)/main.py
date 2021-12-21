import tkinter as tk
import traceback
from time import sleep
import csv

import journal_ui.main_ui as main_ui
import journal_utils.csv_reader as csv_reader
import crossrefapi_utils.journal_search as searcher
import screenscrape_utils.screenscrape as screenscraper
import email_utils.email_handler as email_handler


class MainSystem(object):
    """
    This class is the main system.
    This class is instantiated at turning on the system.
    """

    def __init__(self):
        print("system turned on")
        self.journal_list = None
        self.file_path = None
        # self.root = tk.Tk()
        # self.root.title("Journal Reality")
        # self.main_ui = main_ui.MainUI(master=self.root, main_system=self)
        # self.main_ui.mainloop()  # starts UI

    def create_journal_list(self):
        """
        Creates a list of journals with a given file path
        :return: a list of journal objects
        """
        self.journal_list = csv_reader.read_csv_create_journal(self.file_path)

    def search_articles_journal_list(self, journal_list):
        # iterates a list of journal and fetches an article and a doi for each year
        for j in journal_list:
            self.search_article(j)

    @staticmethod
    def search_article(journal):
        """
        Fetching articles using crossref api.
        :param journal: a journal object
        :return:
        """
        for year in journal.year_dict:
            print(journal.title,
                  journal.year_dict[year][0],  # start_date
                  journal.year_dict[year][1],  # end_date
                  journal.print_issn, journal.online_issn)
            doi = searcher.search_journal(journal.title,
                                          journal.year_dict[year][0],  # start_date
                                          journal.year_dict[year][1],  # end_date
                                          journal.print_issn, journal.online_issn)
            journal.year_dict[year][2].doi = doi
            # journal.year_article_dict[year].doi = doi
            if doi is None:
                print(doi)
            else:
                print('https://doi.org/' + doi)
        print('Search article finished')

    def check_reality_journal_list(self, journal_list):
        """
        Iterates a list of journal objects and checks a reality of each article
        :param journal_list:
        :return:
        """
        for j in journal_list:
            self.check_reality(j)
            # write to a file one line by line
            #

        return True

    @staticmethod
    def check_reality(journal):
        """
        Screen scrape and determine the journal reality.
        :param journal: a journal object
        :return:
        """
        scraper = screenscraper.ScreenScraper
        print(journal.title, journal.publisher)
        for year in journal.year_dict:
            # print(journal.year_dict[year][2])
            doi = journal.year_dict[year][2].doi
            if doi is None:
                print('DOI is none')
            else:
                print('https://doi.org/' + doi)
                result = scraper.check_journal(scraper, doi=doi)
                journal.year_dict[year][2].accessible = result
                print(str(result))
        journal.record_wrong_years()  # wrong years are updated

        print('Reality check finished')

    def check_article_reality(self):
        print("article check")
        path = self.file_path
        with open(path, 'r') as article:
            reader = csv.DictReader(article)
            for row in reader:
                doi = row['DOI']
                print(row['Year'] + ": " + 'https://doi.org/' + doi)
                scraper = screenscraper.ScreenScraper
                # print(row['Year'])

                try:
                    result = scraper.check_journal(scraper, doi=doi)
                    print(result)
                except Exception as e:
                    print('error')
                # article['Accessible'] = result
                finally:
                    print("\n")
        print("reality check finished")

    @staticmethod
    def send_email(email='sora_tobu_neko@outlook.jp'):
        """
        Send the result file to a specified email address.
        :return:
        """
        emailer = email_handler.EmailHandler()
        your_email = email

        sender = your_email
        receiver = 'tori3.tobu@gmail.com'
        password = input("Please enter a password: ")
        files = ["./email_utils/test.csv", "./email_utils/test2.csv"]

        emailer.set_sender(sender=sender, password=password)
        emailer.set_receiver(receiver=receiver)
        emailer.send(files)

    def update(self, code):
        """
        This method is called from main_ui.py for updating this system.
            FILE_UPLOADED
            SEARCH_CLICKED
            DOWNLOAD_CLICKED
        :param code: a message from main_ui.py
        :return:
        """
        print('CODE:', code)

        if code == 'FILE_UPLOADED':
            self.file_path = self.main_ui.input_file_path
            # self.create_journal_list()
            # print('SIZE:', len(self.journal_list))

        elif code == 'SEARCH_CLICKED':
            n = int(input('Enter an index:'))
            self.search_article(self.journal_list[n])

        elif code == 'DOWNLOAD_CLICKED':
            n = int(input('Enter an index:'))
            self.check_reality(self.journal_list[n])

        elif code == 'EMAIL_CLICKED':
            self.send_email()

        if code == 'REALITY_CHECK_CLICKED' or 'FILE_UPLOADED':
            self.check_article_reality()


def start_with_ui(file_path="./journal_utils/journal-csv/use-this.csv"):
    """
    System starts the UI.
    :param file_path: the file path to the csv file of journals
    :return:
    """
    main_system = MainSystem()
    main_system.main_ui.mainloop()  # starts UI


def start_without_ui(file_path="./journal_utils/journal-csv/use-this.csv"):
    """
    Test method for starting the system without UI.
    :param file_path:
    :return: file_path: the file path to the csv file of journals
    """
    main_system = MainSystem()
    # main_system.send_email()
    main_system.file_path = file_path
    main_system.create_journal_list()
    n = int(input('Enter a starting index(-1 to exit):'))
    end = int(input('Enter an ending index(-1 to exit):'))
    err_count = 0
    while n <= end:
        print('\n\nIndex:' + str(n) + '\n\n')
        journal = main_system.journal_list[n]
        print('From', journal.expected_subscription_begin,
              'to', journal.expected_subscription_end)
        # try:
        main_system.search_article(journal)
        main_system.check_reality(journal)
        # csv_reader.write_journal_to_csv(journal)

        # except Exception as ex:
        #     print('EX NAME: ' + ex.__class__.__name__)
        #     print("Exception: {}".format(ex))
        #     print(str(ex) + '\n')
        #     ex_path = './journal_utils/journal-csv/acs-journals/exceptions/'
        #     with open(ex_path + str(n) + '-' + type(ex).__name__ + journal.title + '-' + str(n) + '.txt', 'w') as f:
        #
        #         f.write(ex.__class__.__name__)
        #         f.write('\n')
        #         f.write(journal.title)
        #         f.write('\n')
        #         f.write(str(ex))
        #         f.write('\n\n')
        #         f.write(str(traceback.extract_stack()))
        #         # f.write(traceback.print_exc())
        #         f.write('\n')

        # assert type(exception).__name__ == 'NameError'
        # assert exception.__class__.__name__ == 'NameError'
        n = n + 1
        # n = int(input('Enter an index(-1 to exit):'))


def main():
    """
    Main method to be called when the system gets turned on.
    :return:
    """
    #  start_with_ui()  # the main system
    start_without_ui()  # the test system


def test_call(turn_on_ui, file_path):
    """
    Test method to be called from test.py
    :param turn_on_ui: boolean to activate UI or not.
    :param file_path: the file path to the csv file of journals
    :return: file_path:
    """
    if turn_on_ui:
        start_with_ui(file_path)
    else:
        start_without_ui(file_path)


if __name__ == '__main__':
    main()


def test2():
    # print(MainSystem.__doc__)
    help(MainSystem)
    print(test_call.__annotations__)
    # print(help(MainSystem))
    # print(help(csv_reader))
