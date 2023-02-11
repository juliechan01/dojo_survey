from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ew this assignment'

@app.route('/')
def info():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def display_info():
    session.clear()
    session["name"] = request.form["name"], 
    session["location"] = request.form["location"],
    session["language"] = request.form["language"],
    session["comments"] = request.form["comments"]
    return redirect("/results")

@app.route('/results')
def show_results():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True, port=5500)