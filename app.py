from flask import Flask, render_template, request, redirect

app = Flask(__name__)
kakeibo=[]

@app.route("/")
def home():
    return render_template("index.html", kakeibo=kakeibo)

@app.route("/add", methods=["POST"])
def add():
    item=request.form["item"]
    money=request.form["money"]
    money = int(money)
    kakeibo.append({"item":item,
                    "money":money
    })
    return redirect("/")
app.run()