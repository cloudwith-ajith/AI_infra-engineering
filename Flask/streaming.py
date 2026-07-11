from flask import Flask,render_template,Response 
import cv2 
app = Flask(__name__)

def stream():
    camera = cv2.VideoCapture(0)
    while True:
        code,frame = camera.read()
        if not code:
            break
        else:
            res,buffer =cv2.imencode(".jpeg",frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
             
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/video")
def video():
    return Response(stream(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
