from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/chat")
def chat():
  return render_template("chat.html")

app.run(host="0.0.0.0", port=8020, threaded=True,debug=True)