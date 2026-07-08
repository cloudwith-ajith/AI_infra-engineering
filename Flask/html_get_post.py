### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',result=res)


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))

    



if __name__=='__main__':
    app.run(debug=True)



#-----------------------------------------------
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    # Shortened logic using an if-else expression
    res = "PASS" if score >= 50 else "FAIL"
    return render_template('result.html', result=res, score=score) # Sent score to template too!

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            # Using .get() with a default value of 0 prevents errors if an input is missing
            science = float(request.form.get('science', 0) or 0)
            maths = float(request.form.get('maths', 0) or 0)
            c = float(request.form.get('c', 0) or 0)
            data_science = float(request.form.get('datascience', 0) or 0)
            
            average_score = (science + maths + c + data_science) / 4
            
            # FIX: Convert float average to int so it matches the <int:score> rule
            final_score = int(average_score) 
            
            return redirect(url_for('success', score=final_score))
            
        except ValueError:
            # Handles cases where users type text instead of numbers
            return "Please enter valid numbers in all fields.", 400
            
    # If someone tries to access /submit via GET, send them back home
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
