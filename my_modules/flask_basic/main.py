# Copilot recommendation manual --> OPTION + \

# If choosing separate environment for your app:
# To set environment:
#    source .venv/bin/activate
# to write down all dependencies->
#    pip freeze > requirements.txt
# to isntall dependencies from requirements.txt file
#    pip install -r requirements.txt


# You can also run the code like below:
# To run from terminal using the flask command:
#   flask --app main run. - bring server up on port 5000 by default
#   flask --app main run --host=localhost --port=9000 -- can provide custom port


from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route('/download/<filename>')
def download_image(filename):
    # The directory where the files are located (your static folder)
    directory = 'static'
    filename = "".join((filename, ".jpeg"))
    # Use send_from_directory to serve the file and prompt download
    return send_from_directory(directory, filename, as_attachment=True)


@app.route("/", methods=["GET", "POST"])
def home():
    print(request.method)

    if (request.method == "POST"):
        print("POST METHOD CALLED")
        print(request.form)
        print(f"{request.form['fullName']} {request.form['email']}")
        # with open("file.txt", "w") as f:
        #    f.write(f"{request.form['fullName']} {request.form['email']}")

    marks = {
        "John": 45,
        "Asim": 100,
        "SN": 91,
        "Taran": 66,
        "AS": 89,
        "SK": 89

    }

    return render_template("home.html", marks=marks)


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # to run the code directly from python
    print("RUNNING FROM MAIN FUNCTION")
    app.run(host='localhost', port=9000, debug=True)
