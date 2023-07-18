from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

@app.route('/play/<int:num>/<color>')
def play(num,color):
    num = int(num)
    color = str(color)
    return render_template("index.html", phrase="hello",num =num,color=color)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)