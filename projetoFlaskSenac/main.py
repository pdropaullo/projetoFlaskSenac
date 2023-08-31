from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return "Projeto Web Senac!"

@app.route("/bio")
def biografica():
    return render_template("biografia.html")

if __name__ == "__main__":
    app.run()
