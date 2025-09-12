from flask import Flask, render_template, request
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":

        # received uuid
        rec_id = request.form.get("uuid")
        # input description
        desc = request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            file = request.files[key]
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                if rec_id is not None:
                    upload_path = os.path.join(
                        app.config['UPLOAD_FOLDER'], str(rec_id))

                    if not os.path.exists(upload_path):
                        os.mkdir(upload_path)

                    file.save(os.path.join(upload_path, filename))
                    input_files.append(filename)
                    # capture description and save to file
                    with open(os.path.join(upload_path, "desc.txt"), "w") as f:
                        f.write(desc if desc is not None else "")
        for fl in input_files:
            with open(os.path.join(upload_path, "input.txt"), "a") as f:
                f.write(
                    f"file '{fl}' \nduration 2 \n")

    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    return render_template("gallery.html", reels=reels)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    # to run the code directly from python
    print("RUNNING FROM MAIN FUNCTION")
    app.run(host='localhost', port=9000, debug=True)
