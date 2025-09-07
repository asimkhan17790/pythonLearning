# Flask Basic App Concepts

This project demonstrates several key concepts in Flask and Jinja templating:

## 1. Flask Application Setup

Example:

```python
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='localhost', port=9000, debug=True)
```

## 2. Routing

Example:

```python
@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/download/<filename>")
def download(filename):
    # ...
    pass
```

## 3. Serving Static Files

Example:

```python
from flask import send_from_directory

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory('static', filename, as_attachment=True)
```

## 4. Jinja Templating

Example:

```jinja
<!-- Loop through dictionary -->
{% for name, mark in marks.items() %}
<tr>
  <td>{{ loop.index }}</td>
  <td>{{ name }}</td>
  <td>{{ mark }}</td>
  <td>{% if mark > 80 %}<span>Good</span>{% else %}<span>Bad</span>{% endif %}</td>
</tr>
{% endfor %}
```

## 5. HTML Forms

Example:

```html
<form action="/" method="post">
  <input type="text" name="fullName" />
  <input type="text" name="email" />
  <button type="submit">Submit</button>
</form>
```

## 6. Requirements Management

Example:

```sh
python -m venv .venv
source .venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
```

## 7. Comments

Python:

```python
# This is a Python comment
```

Jinja:

```jinja
{# This is a Jinja comment #}
```

## 8. Form Handling and Request Parameters

Example:

```python
from flask import request

@app.route('/', methods=['POST'])
def handle_form():
    name = request.form['fullName']  # POST param
    email = request.form.get('email')
    # For GET params: request.args.get('param')
    return f"Received: {name}, {email}"
```

## 9. url_for Function

Example:

```python
from flask import url_for

@app.route('/')
def home():
    about_url = url_for('about')
    return f'<a href="{about_url}">About</a>'
```

## 10. Creating APIs with jsonify

Example:

```python
from flask import jsonify

@app.route('/api/data')
def api_data():
    data = {"name": "Asim", "marks": 90}
    return jsonify(data)
```

## 11. Flash Messages

Example:

```python
from flask import flash, get_flashed_messages, render_template, redirect, url_for

@app.route('/submit', methods=['POST'])
def submit():
    flash('Form submitted successfully!')
    return redirect(url_for('home'))

@app.route('/')
def home():
    messages = get_flashed_messages()
    return render_template('home.html', messages=messages)
```

Jinja template:

```jinja
{% for message in messages %}
  <div class="alert alert-info">{{ message }}</div>
{% endfor %}
```

---

This README summarizes the main concepts and features demonstrated in the codebase. For more details, see the code in `main.py` and the templates in the `templates/` folder.
