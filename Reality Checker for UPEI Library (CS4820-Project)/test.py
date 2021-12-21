import main

# If you don't need UI, make this False
turn_on_ui = False

# your favourite file path (journals)
file_path = "./journal_utils/journal-csv/acs-journals/acs.csv"
file_path = "./journal_utils/journal-csv/use-this.csv"


# your favourite file path (articles)
# file_path = "./journal_utils/journal-csv/acs-journals/acs-archives.csv"

if __name__ == '__main__':
    main.test_call(turn_on_ui, file_path)
    # main.test2()

    
