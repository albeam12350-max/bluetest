from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("documento.html", id=id_param)


@app.route("/verificar")
def verif():
    return render_template("documento.html", id=id_param)

@app.route("/valdoc/")
def valdoc():
    id_param = request.args.get("id")
    if not id_param:
        abort(400, description="Falta el parámetro id")

    if id_param != "e67b8930d6653a04f380833a5f10ae617fdb760cb2b7b945e9b7a6463d018b74":
        return render_template("doc2.html", id=id_param)

    return render_template("documento.html", id=id_param)

if __name__ == "__main__":
    app.run(debug=True)
