from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "CodeSchool PH API is running!"})

@app.route('/api/courses')
def courses():
    return jsonify([
        {"id": 1, "title": "Python for Beginners", "price": 499},
        {"id": 2, "title": "Web Dev Bootcamp",     "price": 599},
    ])

if __name__ == '__main__':
    app.run(debug=True)
```

**`requirements.txt`**
```
flask
flask-cors
gunicorn