from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/result/<int:mark>")
def result(mark):
    return render_template("result.html",result = mark)

@app.route("/submit",methods =["POST","GET"])
def submit():
    total_mark = " "
    sci = float(request.form["science"])
    c = float(request.form["c"])
    math = float(request.form["maths"])
    ds = float(request.form["datascience"]) 
    total_mark = ((math+sci+c+ds)/4)
    return redirect(url_for("result",mark = total_mark))


if __name__ == "__main__":
    app.run(debug=True)