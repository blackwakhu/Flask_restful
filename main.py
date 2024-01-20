from flask import Flask, request, jsonify
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Hello(Resource):
  def get(self):
    """this is a function that will be for greeting"""
    return {
      "greeting":"hello world"
    }


