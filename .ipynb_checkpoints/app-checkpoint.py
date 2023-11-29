from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__)
base_path = pathlib.Path().cwd()
db_name = "School1.db"
file_path = base_path / db_name

@app.route("/")
def index():
    return render_template("index_fillin.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    students = cur.execute("SELECT * FROM students").fetchall()
    con.close()
    return render_template("data_table_fillin.html", students = students) #variable = value

if __name__=="__main__":
    app.run(debug=True)

