from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


ENTRIES = {
    'entry1': {'entry': 'studied python'},
    'entry2': {'entry': 'visited the zoo'},
    'entry3': {'entry': 'went to the gym'}
}

def abort_if_entry_doesnt_exist(entry_id):
    if entry_id not in ENTRIES:
        abort(404, message="Entry {} doesn't exist".format(entry_id))

parser = reqparse.RequestParser()
parser.add_argument('entry')


#Entry
#Shows a single entry and allows you to delete an entry
class Entry(Resource):
    def get(self, entry_id):
        abort_if_entry_doesnt_exist(entry_id)
        return ENTRIES[entry_id]

    def delete(self, entry_id):
        abort_if_entry_doesnt_exist(entry_id)
        del ENTRIES[entry_id]
        return ' ', 204

    def put(self, entry_id):
        args = parser.parse_args()
        entry = {'entry': args['entry']}
        ENTRIES[entry_id] = entry
        return entry, 201

#EntryList
#Shows a list of all ENTRIES and lets you POST to add a new entry
class EntryList(Resource):
    def get(self):
        return ENTRIES

    def post(self):
        pass

#Setup the Api routing, the version included
api.add_resource(EntryList, '/entry/api/v1/entries' )
api.add_resource(Entry, '/entry/api/v1/entries/<entry_id>')

if __name__ == '__main__':
    app.run(debug=True)
