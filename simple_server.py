from flask import Flask
app = Flask(__name__)
app_version = "1.0"

@app.route("/")
def hello_world():
	app_version = "0.0.1"
	return app_version

@app.route("/version")
def version():
	return {"version": app_version}


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)

