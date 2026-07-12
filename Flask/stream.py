import cv2
from flask import Flask, Response, render_template

app = Flask(__name__)

#  Load classifiers globally using OpenCV's built-in system paths
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


def stream():
    camera = cv2.VideoCapture(0)

    while True:
        code, frame = camera.read()
        if not code:
            break

        # 1. Convert to grayscale first
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 2. Track faces
        faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y : y + h, x : x + w]
            roi_color = frame[y : y + h, x : x + w]

            # 3. Track eyes inside face region
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # 4. Stream frame
        res, buffer = cv2.imencode(".jpeg", frame)
        frame_bytes = buffer.tobytes()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
        )

    camera.release()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/video")
def video():
    return Response(
        stream(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    # use_reloader=False prevents Anaconda/Flask from starting background duplicate threads
    app.run(debug=True, use_reloader=False)
