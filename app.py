from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
try:
    with open("kakeibo.json","r",encoding="utf-8")as f:
        kakeibo=json.load(f)
except FileNotFoundError:
    kakeibo=[]

if kakeibo:
    ids=[]
    for record in kakeibo:
        ids.append(record["id"])
    next_id=max(ids)+1
else:
    next_id=1

@app.route("/")
def home():
    total=0
    for record in kakeibo:
        total=total+record["money"]
    return render_template("index.html", kakeibo=kakeibo,total=total)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    item=request.form["item"]
    money=request.form["money"]
    date=request.form["date"]
    money = int(money)
    kakeibo.append({
        "id":next_id,
        "item":item,
        "money":money,
        "date":date
    })
    save_data()
    next_id = next_id + 1
    return redirect("/")

@app.route("/search", methods=["POST"])
def search():
    item=request.form["item"]
    results = []
    for record in kakeibo:
        if item in record["item"]:
            results.append(record)
    return render_template("index.html",kakeibo=results)

@app.route("/month",methods=["POST"])
def month():
    month=request.form["month"]
    results=[]
    for record in kakeibo:
        if record.get("date","")[:7]==month:
            results.append(record)
    total=0
    for record in results:
        total=total+record["money"]
    return render_template("index.html", kakeibo=results,total=total)

@app.route("/delete/<int:id>")
def delete(id):
   for i,record in enumerate(kakeibo):
       if record["id"]==id:
           del kakeibo[i]
   save_data()
   return redirect("/")

@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id):
    for i,record in enumerate(kakeibo):
        if record["id"]==id:
            if request.method=="POST":
                item=request.form["item"]
                money=request.form["money"]
                date=request.form["date"]
                money=int(money)
                record["item"]=item
                record["money"]=money
                record["date"]=date
                save_data()
                return redirect("/")
            return render_template("edit.html", record=record)
def save_data():
    with open("kakeibo.json", "w", encoding="utf-8") as f:
        json.dump(kakeibo, f, ensure_ascii=False, indent=4)   
app.run()