from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mostrar_documento():
    return render_template("documento.html")

if __name__ == "__main__":
    app.run(debug=True)
