from flask import Flask, render_template, request, redirect
from datetime import date
import json

app = Flask(__name__)
try:
    with open("kakeibo.json","r",encoding="utf-8")as f:
        kakeibo=json.load(f)
except FileNotFoundError:
    kakeibo=[]

try:
    with open("budget.json","r",encoding="utf-8")as f:
        budgets=json.load(f)
except FileNotFoundError:
    budgets={}

if kakeibo:
    ids=[]
    for record in kakeibo:
        ids.append(record["id"])
    next_id=max(ids)+1
else:
    next_id=1

@app.route("/")
def home():
    current_month=date.today().strftime("%Y-%m")
    results=[]
    for record in kakeibo:
        if record.get("date","")[:7]==current_month:
            results.append(record)
    total=0
    for record in results:
        total=total+record["money"]
    monthly_budget=budgets.get(current_month, 0)
    remaining = monthly_budget - total
    return render_template("index.html", kakeibo=results,total=total,monthly_budget=monthly_budget,remaining=remaining)

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
    current_month = date.today().strftime("%Y-%m")
    results = []
    for record in kakeibo:
        if item in record["item"]:
            results.append(record)
    total = 0
    for record in kakeibo:
        if record.get("date", "")[:7] == current_month:
            total = total + record["money"]
    monthly_budget = budgets.get(current_month, 0)
    remaining = monthly_budget - total
    return render_template("index.html",kakeibo=results,total=total,monthly_budget=monthly_budget,remaining=remaining)

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

    monthly_budget=budgets.get(month, 0)
    remaining = monthly_budget - total
    return render_template("index.html", kakeibo=results,total=total,monthly_budget=monthly_budget,remaining=remaining)

@app.route("/budget",methods=["POST"])
def budget():
    month=request.form["month"]
    money=request.form["money"]
    money=int(money)
    budgets[month]=money
    save_budgets()
    return redirect("/")
    

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
def save_budgets():
   with open("budget.json", "w", encoding="utf-8") as f:
        json.dump(budgets, f, ensure_ascii=False, indent=4)   
    
app.run()