import csv

from journal_utils.journal import Journal


def write_file(file_name):
    with open(file_name + '.csv', 'w', encoding='utf8') as csv_file:
        fieldnames = ['title', 'package']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'title': 'Japan Academic', 'package': 'Japan Times'})
        writer.writerow({'title': 'Monthly Cooking', 'package': 'NHK Journal'})


def write_journal_list_to_csv(journal_list, file_name='journal_result'):
    print('Journal object is converted into output csv')
    with open(file_name + '.csv', 'w', encoding='utf8') as csv_file:
        fieldnames = ['Title',
                      'PackageName',
                      'URL',
                      'Publisher',
                      'PrintISSN',
                      'OnlineISSN',
                      'ManagedCoverageBegin',
                      'ManagedCoverageEnd'
                      'AsExpected',
                      'ProblemYears',
                      'FreeYears'
                      ]


def write_journal_to_csv(journal, file_name='journal'):
    """
    Given a journal object, creates a csv file with the articles of the journal objects
    :param journal: an object of a Journal class
    :param file_name: the name of the output file
    :return:
    """
    print('Journal object is converted into output csv')
    file_name = './journal_utils/journal-csv/acs-journals/acs-archives-articles/' + journal.title
    with open(file_name + '.csv', 'w', encoding='utf8') as csv_file:
        fieldnames = ['Name',
                      'Year',
                      'DOI',
                      'DOI-URL',
                      'Accessible'
                      ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for y in journal.year_dict:
            doi = journal.year_dict[y][2].doi
            if doi is None:
                doi = 'none'
            writer.writerow({'Name': journal.title,
                             'Year': y,
                             'DOI': journal.year_dict[y][2].doi,
                             'DOI-URL': 'https://doi.org/' + doi,
                             'Accessible': journal.year_dict[y][2].accessible
                             })


def write_result_csv(journal_list, file_name='journal_result'):
    print("result file")
    with open(file_name + '.csv', 'w', encoding='utf8') as csv_file:
        fieldnames = ['Title',
                      'PackageName',
                      'URL',
                      'Publisher',
                      'PrintISSN',
                      'OnlineISSN',
                      'ManagedCoverageBegin',
                      'ManagedCoverageEnd',
                      'AsExpected',
                      'ProblemYears',
                      'FreeYears'
                      ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for j in journal_list:
            writer.writerow({'Title': j.title,
                             'PackageName': j.package,
                             'URL': j.url,
                             'Publisher': j.publisher,
                             'PrintISSN': j.print_isssn,
                             'OnlineISSN': j.online_issn,
                             'ManagedCoverageBegin': j.expected_subscript_begin,
                             'ManagedCoverageEnd': j.expected_subscript_end,
                             'AsExpected': 'Correct',
                             'ProblemYears': '1993, 1995',
                             'FreeYears': '2005'
                             })


def read_csv_create_journal(file_name):
    journal_list = []

    with open(file_name, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            journal_list.append(
                Journal(row['Title'],
                        row['PackageName'],
                        row['URL'],
                        row['Publisher'],
                        row['PrintISSN'],
                        row['OnlineISSN'],
                        row['ManagedCoverageBegin'],
                        row['ManagedCoverageEnd']
                        ))
    return journal_list


def write_problem_csv():
    print("result file")


def write_doi_csv():
    print("result file")


def read_file(file_name):
    with open(file_name + '.csv', 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        # for row in reader:
        #     print(row['title'], '=>', row['package'])


def construct_journal_list_from(journals_csv):
    journal_obj_list = []

    with open(journals_csv, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            journal_obj_list.append(
                Journal(row['Title'],
                        row['PackageName'],
                        row['URL'],
                        row['Publisher'],
                        row['PrintISSN'],
                        row['OnlineISSN'],
                        row['ManagedCoverageBegin'],
                        row['ManagedCoverageEnd']
                        ))
    return journal_obj_list


def reconstruct_journal_list_from(articles_csv):
    """
    Reconstruct journal objects from the temporary article csv file
    :param articles_csv:
    :return:
    """
    journal_obj_list = []
    current_title = ''

    with open(articles_csv, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        j = None
        for row in reader:
            y = int(row['Year'])
            if row['Accessible'] == 'TRUE':
                access = True
            else:
                access = False
            if current_title != row['Title']:
                current_title = row['Title']

                j = Journal(row['Title'],
                            row['PackageName'],
                            row['URL'],
                            row['Publisher'],
                            row['PrintISSN'],
                            row['OnlineISSN'],
                            row['ManagedCoverageBegin'],
                            row['ManagedCoverageEnd']
                            )
                j.year_dict[y][2].doi = row['DOI']
                j.year_dict[y][2].accessible = access
                journal_obj_list.append(j)
            else:
                j.year_dict[y][2].doi = row['DOI']
                j.year_dict[y][2].accessible = access

    print('size' + str(len(journal_obj_list)))
    return journal_obj_list


def write_articles_csv_from(journal_obj_list, file_name='new-articles.csv'):
    print("result file")
    with open(file_name + '.csv', 'w', encoding='utf8') as csv_file:
        fieldnames = ['Title',

                      'Year',
                      'DOI',
                      'DOI-URL',
                      'Accessible',

                      'PackageName',
                      'URL',
                      'Publisher',
                      'PrintISSN',
                      'OnlineISSN',
                      'ManagedCoverageBegin',
                      'ManagedCoverageEnd',
                      'AsExpected',
                      'ProblemYears',
                      'FreeYears'
                      ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for j in journal_obj_list:
            for y in j.year_dict:
                writer.writerow({'Title': j.title,

                                 'Year': y,
                                 'DOI': j.year_dict[y][2].doi,
                                 'DOI-URL': 'http://doi.org/' + str(j.year_dict[y][2].doi),
                                 'Accessible': j.year_dict[y][2].accessible,

                                 'PackageName': j.package,
                                 'URL': j.url,
                                 'Publisher': j.publisher,
                                 'PrintISSN': j.print_issn,
                                 'OnlineISSN': j.online_issn,
                                 'ManagedCoverageBegin': j.expected_subscription_begin,
                                 'ManagedCoverageEnd': j.expected_subscription_end,
                                 'AsExpected': j.result_as_expected,
                                 'ProblemYears': j.wrong_years,
                                 'FreeYears': 'NoYears'
                                 })


def write_journals_csv_from(journal_obj_list, file_name='new-journals.csv'):
    print("result file")
    with open(file_name + '.csv', 'w', encoding='utf8') as csv_file:
        fieldnames = ['Title',
                      'PackageName',
                      'URL',
                      'Publisher',
                      'PrintISSN',
                      'OnlineISSN',
                      'ManagedCoverageBegin',
                      'ManagedCoverageEnd',
                      'AsExpected',
                      'ProblemYears',
                      'FreeYears'
                      ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for j in journal_obj_list:
            writer.writerow({'Title': j.title,
                             'PackageName': j.package,
                             'URL': j.url,
                             'Publisher': j.publisher,
                             'PrintISSN': j.print_issn,
                             'OnlineISSN': j.online_issn,
                             'ManagedCoverageBegin': j.expected_subscription_begin,
                             'ManagedCoverageEnd': j.expected_subscription_end,
                             'AsExpected': 'Correct',
                             'ProblemYears': j.wrong_years,
                             'FreeYears': '2005'
                             })


def write_wrong_result_csv_from(journal_list):
    wrong_result_csv = 1
    return wrong_result_csv


if __name__ == '__main__':
    # list = construct_journal_list_from('./journal-csv/acs-journals/acs-archives.csv')
    list = reconstruct_journal_list_from('./journal-csv/acs-journals/acs-short.csv')
    write_journals_csv_from(list)
    write_articles_csv_from(list)
