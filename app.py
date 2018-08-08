from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


entries = {
    'entry1': {'entry': 'studied python'},
    'entry2': {'entry': 'visited the zoo'},
    'entry': {'entry': 'went to the gym'}
}

def abort_if_entry_doesnt_exist(entry_id):
    if entry_id not in entries:
        abort(404, message="Entry {} doesn't exist".format(entry_id))

parser = reqparse.RequestParser()
parser.add_argument('entry')


#Entry
#Shows a single entry and allows you to delete an entry
class Entry(Resource):
    def get(self, entry_id):
       pass

    def delete(self, entry_id):
        pass

    def put(self, entry_id):
        pass

#EntryList
#Shows a list of all entries and lets you POST to add a new entry
class EntryList(Resource):
    def get(self):
        pass

    def post(self):
        pass

#Setup the Api routing, the version included
api.add_resource(EntryList, '/entry/api/v1/entries' )
api.add_resource(Entry, '/entries/api/v1/<entry_id>')

if __name__ == '__main__':
    app.run(debug=True)
