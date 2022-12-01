from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def add_post():
    if request.method=="POST":
        num1 = request.form['text1']
        num2 = request.form['text1']
        num3 = float(num1) + float(num2)
        return render_template('index.html',num3=num3)

    

if __name__ == "__main__" :
    app.run(debug=True) 