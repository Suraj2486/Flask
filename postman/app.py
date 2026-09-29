from flask import Flask, request

app = Flask(__name__)

names = ["Naina", "Siya", "Suraj"]
@app.route("/getnames")
def getName():
    return names

@app.route("/savenames", methods = ["POST"])
def savenames():
    data = request.get_json()
    name_value = data.get("name")
    names.append(name_value)
    return names

details = [
    {"name" : "naina", "age" : 21},
    {"name" : "siya", "age" : 19},
    {"name" : "suraj", "age" : 20}
]

@app.route("/getdetails", methods = ['GET'])
def getdetails():
    return details

@app.route("/savedetails", methods = ['POST'])
def savedetails():
    data = request.get_json()
    details.append(data)
    return details
 