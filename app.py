from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
logins_file = "logins.txt"
if not os.path.exists(logins_file):
    open(logins_file, "w").close()

@app.route("/", methods=["GET", "POST"])
def signup():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            with open(logins_file, "a") as f:
                f.write(f"{username}:{password}\n")
            message = f"Thanks {username}! Total signed up: {count_logins()}"
        else:
            message = "Please enter both username and password."
    return render_template_string(open("index.html").read(), message=message, total=count_logins())

def count_logins():
    with open(logins_file, "r") as f:
        return len(f.readlines())

if __name__ == "__main__":
    app.run(debug=True)
