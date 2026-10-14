from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def logar():
    return render_template("index.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

@app.route("/adicionar", methods=["GET"])
def adicionar():
    return render_template("adicionar.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)