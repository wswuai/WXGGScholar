
import scholar



def google_scholar_query(querystr):
    querier = scholar.ScholarQuerier()
    query = scholar.SearchScholarQuery()
    query.set_phrase(querystr)
    querier.send_query(query)

    ret = "\n=========\n"
    for article in querier.articles:
        ret += article.as_txt() +  "\n=========\n"

    return ret

if __name__=='__main__':
    querystr = "SVM"
    print google_scholar_query(querystr)

