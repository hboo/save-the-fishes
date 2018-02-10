from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html", name=app)

@app.route("/get_fish/<image>/<size>/<location>")
def get_fish(image, size, location):
	# do something with image path
	return {'fish_id': 'Morone americana'}


if __name__ == "__main__":
    app.run()
