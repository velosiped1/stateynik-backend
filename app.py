'''
    Main app
'''

from bottle import route, run, template


@route("/")
def main():
    with open("index.html", mode="r") as index_file:
        index_data = index_file.read()
        return index_data

@route('/<filename>')
def index(filename):
    with open(filename, mode="r") as index_file:
        index_data = index_file.read()
        return index_data   

run(host='localhost', port=8080)
