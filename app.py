from flask import Flask, render_template, request, redirect

app = Flask(__name__)
kakeibo=[]
next_id=1

@app.route("/")
def home():
    return render_template("index.html", kakeibo=kakeibo)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    item=request.form["item"]
    money=request.form["money"]
    money = int(money)
    kakeibo.append({
        "id":next_id,
        "item":item,
        "money":money
    })
    next_id = next_id + 1
    return redirect("/")
@app.route("/delete/<int:id>")
def delete(id):
   for i,record in enumerate(kakeibo):
       if record["id"]==id:
           del kakeibo[i]
   return redirect("/")        
app.run()