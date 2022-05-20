from flask import Flask,jsonify, request
import datetime

app=Flask(__name__)
user={}
time=datetime.datetime.now()
array1=[]
id=0
@app.route('/', methods=['GET'])

@app.route('/profile',methods=["POST"])
def profile():
    
    global time
    time =datetime.datetime.now()
    global user
    user = {
        "last_updated" : time,
        "username": request.json["username"],
        "role" : request.json["role"],
        "color" : request.json["color"]
    }

    return {"data":user}

@app.route('/profile', methods=['GET'])
def profile2():
    return {"data":user}

@app.route('/profile', methods=['PATCH'])
def profile3():
    
    global time 
    time = datetime.datetime.now()

    if "username" in request.json:
      user["username"] = request.json["username"]

    if "role" in request.json:
      user["role"] = request.json["role"]

    if "color" in request.json:
      user["color"] = request.json["color"]
      
    return {"data": user}


@app.route('/data',methods=["POST"])
def data():
    global tankr
    global id
    id= id + 1
    tankr = {
        "id":id,
        "location":request.json["location"],
        "lat":request.json["lat"],
        "long":request.json["long"],
        "percentage_full":request.json["percentage_full"]   
    }
    array1.append(tankr)
    return jsonify(tankr)


@app.route('/data', methods=['GET'])
def tankr2():
    return jsonify (array1)   

@app.route('/data/<int:id>', methods=['PATCH'])
def tankr3(id):  
    for a in array1:
    
        if id == a["id"]:
       
            if "location" in request.json:
                a["location"] = request.json["location"]    
            
            if "lat" in request.json:
                a["lat"] = request.json["lat"]
            
            if "long" in request.json:
                a["long"] = request.json["long"]
            
            if "percentage_full" in request.json:
                a["percentage_full"] = request.json["percentage_full"]

    return jsonify(array1[int(id)-1])


@app.route('/data/<int:id>', methods=["DELETE"])
def tankr4(id):
 
  for a in array1:
    
    if id == a["id"]:
      array1.remove(a)
  
  return {"success": True}



if __name__ == "__main__":
    app.run(debug=True,
    port=3000,
    host="0.0.0.0"
    )
