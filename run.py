from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['POST'])
def ola():
    return "<h1>Olá.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
