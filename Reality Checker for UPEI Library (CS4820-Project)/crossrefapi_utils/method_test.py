from crossref.restful import Works
from crossref.restful import Journals

works = Works()

for i in works.query('Nonlinear Analysis: Real World Applications').filter(has_funder='true', has_license='true', issn='1468-1218',
                                                                           from_pub_date='2000-12-31').sample(10).select('DOI, prefix'):
    print(str(i))


journals = Journals()
journal_ = journals.journal('1468-1218')
#print (journal_)

re = works.doi("10.1016/S0362-546X(00)00002-X")
print (re)
print(re['publisher'])