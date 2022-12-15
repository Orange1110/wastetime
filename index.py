import firebase_admin
import random
from firebase_admin import credentials, firestore
cred = credentials.Certificate("riddle.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>猜謎語</h1>"
    homepage += "<a href=/item>物品型謎語</a><br>"
    homepage += "<a href=/place>地方型謎語</a><br>"
    homepage += "<a href=/slang>俚語型謎語</a><br>"
    homepage += "<a href=/random>隨機型謎語</a><br>"
    return homepage

@app.route("/item")
def item():

    num = str(random.randint(1,10))

    result =""

    if request.method == "POST":
        keyword = request.form["keyword"]

        collection_ref = db.collection("item")
        docs = collection_ref.get()
        for doc in docs:
            dict = doc.to_dict()
            if keyword in dict["num"]:
                result = format(dict["Answer"])

        return result
    else:
        return render_template("item.html")