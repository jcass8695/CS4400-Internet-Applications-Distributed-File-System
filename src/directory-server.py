import json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

MACHINES = {1: ('127.0.0.1', 5001)}
FILENAMES = {'test': (1, 1)}
parser = reqparse.RequestParser()
parser.add_argument('filename')


class DirectoryServer(Resource):
    def get(self):
        filename = parser.parse_args()['filename']
        if filename in FILENAMES.keys():
            file_id, machine_id = FILENAMES[filename]
            machine_address = MACHINES[machine_id] or None
            return {'file_id': file_id, 'machine_id': machine_address}


api.add_resource(DirectoryServer, '/')

if __name__ == '__main__':
    app.run(debug=True)