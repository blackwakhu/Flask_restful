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

if __name__ == "__main__":
  app.run(debug=True)


