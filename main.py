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

