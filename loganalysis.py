#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for
from loganalysisdb import get_popular_article, \
        get_popular_article_author, get_error_day

app = Flask(__name__)

DBNAME = "news"
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Analysis</title>
    <style>
      .post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px; }
      .column {border: 1px solid #999;}
    </style>
  </head>
  <body>
  <p>Most popular three articles of all time </p>
    %s
  <p>Most popular author </p>
    %s
  <p>Days with more than 1 percent of requests lead to errors</p>
  %s
  </body>
</html>
'''

# HTML template for an individual comment
POP_ARTICLE = '''\
    <table><tr class='post'><td class="column">%s</td><td class="column">%s
    </td></tr></table>
'''
POP_AUTHOR = '''\
    <table><tr class='post'><td class="column">%s</td><td class="column">%s
    </td></tr></table>
    '''
ERR_DATA = '''\
    <table><tr class='post'><td class="column">%s</td><td class="column">%s
    </td></tr></table>
    '''


@app.route('/', methods=['GET'])
def main():
    '''First Query'''
    article = "".join(POP_ARTICLE % (article, visitnumber)
                      for article, visitnumber in get_popular_article())

    author = "".join(POP_AUTHOR % (author, visitcount)
                     for author, visitcount in get_popular_article_author())

    error_day = "".join(ERR_DATA % (date, percent_error)
                        for percent_error, date in get_error_day())

    html = HTML_WRAP % (article, author, error_day)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
