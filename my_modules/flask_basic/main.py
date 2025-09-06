# If choosing separate environment for your app:
# To set environment:
#    source .venv/bin/activate
# to write down all dependencies->
#    pip freeze > requirements.txt
# to isntall dependencies from requirements.txt file
#    pip install -r requirements.txt


# You can also run the code like below:
# To run from terminal using the flask command
#   flask --app main run


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello Asim... Lets do this!!</p>"


if __name__ == "__main__":
    app.run(debug=True)
