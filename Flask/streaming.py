from flask import Flask, Response 
app = Flask(__name__)
camera =  cv2.video.Capture(0)

def frame_capture():
    while True:
        stauts_code, frames = camera.read()
        if not stauts_code:
            break
        else:
            res, buffer = cv2.imencode("jpeg",frames)
            frame   = buffer.tobytes() 

            yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/video")
def video():
    return Response(func(),mimetype='multipart/x-mixed-replace; boundary=frame')
    

    
if __name__ == "__main__":
    app.run(debug = True) 
