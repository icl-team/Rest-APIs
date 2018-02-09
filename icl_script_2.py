from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///icl_lab.db')
app = Flask(__name__)
api = Api(app)

# show all data
class show_icl(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from user_data")  # This line performs query and returns json result
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
#ques 2
class add_icl(Resource):
    def get(self,id):
        conn = db_connect.connect()  # connect to database
        if id==2:
            name='Abhi'
            email='ab@gmail.com'

        elif id == 35:
            name = 'Sanjana'
            email = 'sh@gmail.com'

        elif id  == 1:
            name = 'Madhav'
            email = 'mb@gmail.com'
        query = conn.execute('''INSERT INTO user_data(id, name, email)
                                        VALUES(?,?,?)''', (int(id), name, email))
        return jsonify({'response': 'Success'})

#ques 3
class upd_icl(Resource):
    def get(self,id):
        conn = db_connect.connect()  # connect to database
        if id==2:
            updated_name='Abhilash N'
        elif id == 35:
            updated_name = 'Sanjana Hathwar'
        elif id  == 1:
            updated_name = 'Madhav Bharadwaj'

        query = conn.execute("UPDATE user_data SET name = '"+str(updated_name)+"' WHERE id = %d" % int(id))
        return jsonify({'response': 'Success'})

api.add_resource(show_icl,'/icl')
api.add_resource(add_icl, '/icl/add/<int:id>')  # Route_3
api.add_resource(upd_icl, '/icl/update/<int:id>')


if __name__ == '__main__':
    app.run(port=5002)
