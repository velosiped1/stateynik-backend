'''
    Main app
'''

from bottle import route, run, template, response, request

_PREFIX = r'F:/Projects/stateynik-frontend/'


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


run(host='localhost', port=8080)
