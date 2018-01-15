# "Database code" for the log analysis Forum.
import psycopg2
DBNAME = "news"


def get_popular_article():
    # """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select replace(replace(initcap(path),'-',' '),'/Article/','')\
     as \"Article\",count(*) \"Number of Visits\" from log where \
     status ='200 OK' and path like '/article%' group by path,status order \
      by 2 desc limit 3;")
    popular_article = c.fetchall()
    db.close()
    return popular_article


def get_popular_article_author():
    # """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select n.name \"Author Name\",count(*) \"Views\" from log l,\
    (select b.name,lower(replace(substr(a.title,0,11),' ','-')) title \
    from articles a, authors b where a.author=b.id) n where l.status='200 OK' \
    and substr(path,10,10) = n.title group by n.name order by 2 desc;")
    popular_article_author = c.fetchall()
    db.close()
    return popular_article_author


def get_error_day():
    # On which days did more than 1% of requests lead to errors?
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select (cast(ed.count as float)/td.count)*100 error_rate,td.time\
      from total_data td,error_data ed where td.time=ed.time\
       and (cast(ed.count as float)/td.count)*100 > 1.0")
    error_data = c.fetchall()
    db.close()
    return error_data
