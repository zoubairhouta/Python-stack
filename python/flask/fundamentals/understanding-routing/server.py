from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


# 1st assignment


@app.route("/")
def hello_world():
    return "Hello World!"


# 2nd Asssignment
@app.route("/Dojo")
def Dojo():
    return "Dojo!"


# 3rd assignment
@app.route("/say/<str:name>")
def say(name):
    return f"Hello  {name} ! "


# 4th assignment
@app.route("/repeat/<int:number>/<text>")
def repeat_text(number, text):
    result = ""
    for _ in range(number):
        result += f"{text}\n"
    return result


@app.route("/<path:path>")
def handle_invalid_routes(path):
    return "Sorry! No response. Try again."


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True, port=5500)  # Run the app in debug mode.
