import requests
from flask_restful import Api,Resource, reqparse, fields, marshal_with, abort
from flask import Flask, render_template,request, jsonify
import random

# responce = requests.get("https://api.stockmarketapi.in/api/v1/topgainers?token=65b774fa414c9b01c854a597b7ae82c57e7757b1e12abcb736ab9a754ffb617a")
# print(responce.json())

app = Flask(__name__)
api = Api(app)

class result(Resource):
    def get(self):
        temp= requests.get("https://api.stockmarketapi.in/api/v1/topgainers?token=65b774fa414c9b01c854a597b7ae82c57e7757b1e12abcb736ab9a754ffb617a")
        responce=temp.json()
        D=[]
        i=random.randint(0,len(responce['data']))
        D.append(responce['data'][i]['CompanyName'])
        i=random.randint(0,len(responce['data']))
        D.append(responce['data'][i]['CompanyName'])
        i=random.randint(0,len(responce['data']))
        D.append(responce['data'][i]['CompanyName'])
        return D

api.add_resource(result, "/")


if __name__ == "__main__":
    app.run(debug=True)

