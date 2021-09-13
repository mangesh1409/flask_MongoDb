from flask import Flask, request, render_template,jsonify,Response,redirect
import pymongo
import json
from bson.objectid import ObjectId

app=Flask("main")

#####################################################################
try:
    mongo=pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db=mongo.Task_Flask  # Cretae Databse
    mongo.server_info()
except:
    print("Error- Connot Connect To Database")



###############################################
# Home Page
@app.route("/form")
def myform():
    return render_template("form.html")


###############################################
@app.route("/adduser", methods=['POST'])
def createUser():
    try:
        if request.method =='POST':
            name=request.form.get('name')
            email=request.form.get('email')
            phone=request.form.get('phone')
            user={'name':name,'email':email,'phone':phone}
            dbResponce=db.users.insert_one(user)
            for attr in dir(dbResponce):
                    print(attr)
            
            return render_template("goback.html")

    except Exception as ex:
        print(ex)


####################################################
@app.route("/getuser", methods=['GET'])
def getUser():
    try:
        data=list(db.users.find())
        """for i in data():
            print(i)
        return data"""
        return '<h3>OUTPUT</h3>' + render_template('show.html',len=len(data),data=data)


    except Exception as ex:
        print((ex)) 



######################################################
@app.route("/delete",methods=['GET'])
def delete():
    try:
        user = request.args.get('id')
        dbResponce=db.users.delete_one({"_id":ObjectId(user)})
        for attr in dbResponce:
            print(attr)

        return user

    except Exception as ex:
        print(ex)





######################################################
@app.route("/update", methods=['GET'])
def update():
    try:
        user = Int(request.args.get('id'))
        data=dict(db.users.find({'_id': ObjectId(user)}))
        for i in data:
            print(i)
        
        return data
    except Exception as ex:
        print("***************************************************")
        print(ex)
        print("***************************************************")




###############################################
if __name__=="__main__":
    app.run(port=80,debug=True)