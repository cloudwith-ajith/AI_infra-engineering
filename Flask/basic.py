from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "hi there, Im AJITH!!!!!!"

if __name__ == "__main__":
    app.run()
