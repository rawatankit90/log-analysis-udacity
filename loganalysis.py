#!/usr/bin/env python3
#

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

    <!--Bootstrap 4 -->
    <link rel="stylesheet"
     href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
     integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
     crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"
     integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n"
     crossorigin="anonymous"></script>

    <script src=
    "https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"
    integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb"
     crossorigin="anonymous"></script>

    <script src=
    "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js"
    integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn"
    crossorigin="anonymous"></script>

    <style type="text/css">
        body {
            padding-top: 80px;
        }
        .post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px; }
        .column {border: 1px solid #999;
                text-align:center;}
        h2 {
            padding : 10px;
        }
    </style>
  </head>
  <body>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h2>Most popular three articles of all time </h2>
                <table>
                    <tr class="post">
                        <th class="column">Article</th>
                        <th class="column">Views</th>
                    </tr>
                    %s
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Most popular author </h2>
                <table>
                    <tr class="post">
                        <th class="column">Author</th>
                        <th class="column">Views</th>
                    </tr>
                    %s
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Days with more than 1 percent of requests lead to errors
                </h2>
                <table>
                    <tr class="post">
                        <th class="column">Date</th>
                        <th class="column">Error Percentage</th>
                    </tr>
                    %s
                </table>
            </div>
        </div>
    </div>
  </body>
</html>
'''

# HTML template for an individual comment
POP_ARTICLE = '''\
    <tr class='post'><td class="column">%s</td><td class="column">%s</td></tr>
'''
POP_AUTHOR = '''\
    <tr class='post'><td class="column">%s</td><td class="column">%s</td></tr>
    '''
ERR_DATA = '''\
    <tr class='post'><td class="column">%s</td><td class="column">%s</td></tr>
    '''


@app.route('/', methods=['GET'])
def main():
    '''First Query'''
    article = "".join(POP_ARTICLE % (article, visitnumber)
                      for article, visitnumber in get_popular_article())

    author = "".join(POP_AUTHOR % (author, visitcount)
                     for author, visitcount in get_popular_article_author())

    error_day = "".join(ERR_DATA % (date, round(percent_error,2))
                        for percent_error, date in get_error_day())

    html = HTML_WRAP % (article, author, error_day)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
