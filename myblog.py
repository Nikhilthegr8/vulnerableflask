from flask import *

app = Flask(__name__)

l = ['vanilla','chocolate','strawberry']

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',content=l)

@app.route("/user/<username>")
def user(username):
    return "<h1>{}</h1>".format(username)

@app.route("/ssti")
def login():
    return render_template('ssti.html')

@app.route("/validate",methods=['POST'])
def validate():
    username = request.form['username']
    response = "<h1>Welcome {}".format(str(username))
    return render_template_string(response)

@app.route("/xss")
def xss():
   return render_template('xss.html')


@app.route("/validatexss",methods=['POST'])
def xssalert():
    name = request.form['username']
    return "<html>{}</html>".format(name)


@app.route("/idor")
def idoor():
    return "<h1>You shall not pass !</h1>"

@app.route("/idor/<key>")
def idor(key):
    if int(key)==0:
        return "<h1>Success</h1>"
    else:
        return "<h1>Fail</h1"


if __name__ == '__main__':
    app.run(debug=True)
