'''
    Main app
'''

from bottle import route, run, template, response, request, post
import psycopg2 as psql
from datetime import datetime, timezone
import json

_PREFIX = r'F:/Projects/stateynik-frontend/'
# TODO: move to config
_DB_CONNECTION = psql.connect("dbname=stateynik user=matvey password=root")


@route("/")
def main():
    with open(_PREFIX + "index.html", mode="r") as index_file:
        index_data = index_file.read()
        return index_data


@route('/<filename>')
def index(filename):
    ext = filename.split(".")[-1]
    if ext == "css":
        response.set_header("Content-Type", "text/css")
    elif ext == "js":
        response.set_header("Content-Type", "text/javascript")
    else:
        response.set_header("Content-Type", "text/plain")
    try:
        with open(_PREFIX + filename, mode="r") as index_file:
            index_data = index_file.read()
            return index_data
    except FileNotFoundError:
        return ""


@post('/api/v1/publish')
def insert_publication():
    js = json.loads(request.body.read().decode('utf-8'))
    now = datetime.now(timezone.utc)
    with _DB_CONNECTION.cursor() as cur:
        cur.execute('''INSERT INTO public."Publication"(
    	title, content, author_id, pubdate)
    	VALUES (''' + "'" + js["title"] + "'" + ',' + "'" + js["content"] + "'" + ',' + '1' + ',' + "TIMESTAMP '" + str(now) + "'"  + ''');
        ''', ())
        # locks on cursor execution
        _DB_CONNECTION.commit()


run(host='localhost', port=8080)
