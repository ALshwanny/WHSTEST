from flask import Flask, render_template, Blueprint, request, url_for, redirect
from db.logindb import logindb
from db.listdb import listdb
from db.writedb import writedb
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.register_blueprint(logindb)
app.register_blueprint(listdb)
app.register_blueprint(writedb)

app.secret_key="asdasd"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/list")
def list():
    return render_template('list.html')

@app.route("/write")
def write():
    return render_template('write.html')

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join('static/uploads', filename))
            return redirect(url_for('list'))
    return 'No file selected'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000" ,debug=True)
