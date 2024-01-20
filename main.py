from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json


app = Flask(__name__)
api = Api(app)


class Hello(Resource):
  def get(self):
    """this is a function that will be for greeting"""
    return {
      "greeting":"hello world"
    }

def read():
  """this will  read the data from the contact.json file"""
  data = {}
  with open("contact.json", "r") as f:
    data = json.load(f)
  return data


def write(data):
  """this will write the data to the json file"""
  with open("contact.json", "w") as f:
    json.dump(data)

all_ = read()

class Contact(Resource):
  """this will deal with activities that involve the whole contact.json file"""

  def get(self):
    """returns all the data in the contact.json file to he user"""
    return jsonify(all_)
    
  def delete(self):
    """this will delete all the data in the contact.json file"""
    all_.clear()
    write(all_)
    return {"status": "successful deleted all the data"}


class MyContact(Resource):
  """this will deal with individual forms of data"""
  def get(self, cont_id):
    """returns an individual for the id put"""
    return {"id": cont_id, 
            "data": all_[cont_id],
            "status": "read successfully"
           }


  def post(self, cont_id):
    """adds the new data item to the contact.json file"""
    data = {
      "name": request.form['name'],
      "email": request.form['email'],
      "contact": request.form['contact'],
      "relationship": request.form['relationship']
    }
    all_[cont_id] = data
    write(all_)
    return {
      "id": cont_id ,
      "data": data,
      "status":"created a new record successfully"
    }

  
  def put(self, cont_id ):
    """this will be responsible for updating the data"""
    data = {
      "name": request.form['name'],
      "email": request.form['email'],
      "contact": request.form['contact'],
      "relationship": request.form['relationship']
    }
    all_[cont_id] = data
    write(all_)
    return {
      "id": cont_id ,
      "data": data,
      "status":"updated a new record successfully"
    }

  
  def delete(self, cont_id ):
    """this will delete a single instance with the same name""" 
    all_.pop(cont_id)
    write(all_)
    return {
    "message": "successfully  deleted"
    }

"""this will deal with the routing of the urls"""
api.add_resource(Hello, "/")
api.add_resource(Contact, "/contact")
api.add_resource(MyContact, "/contact/<int:cont_id>")



if __name__ == "__main__":
  app.run(debug=True)


