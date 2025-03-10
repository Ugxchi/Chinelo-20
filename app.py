from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store wishes in memory (can be moved to a database in a real-world application)
wishes = []

# Home route (submit wishes page)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        wish = request.form["wish"]
        
        # Add the wish to the list
        wishes.append({"name": name, "wish": wish})
        
        # Display thank you message and stay on the same page
        return render_template("index.html", message="Thank you for your wish! 🎉")
    
    return render_template("index.html", message=None)


# Route to handle the password-protected wishes page
@app.route("/wishes", methods=["GET", "POST"])
def view_wishes():
    # Check if the form is being submitted
    if request.method == "POST":
        password = request.form.get('password')
        correct_password = "birthday20"  # The correct password

        if password == correct_password:
            # If the password is correct, show the wishes page
            return render_template("wishes.html", wishes=wishes)
        else:
            # If the password is incorrect, show an error message
            return "Incorrect password. Please try again.", 403
    
    # If the user isn't submitting the password, show the password protection form
    return render_template("password_protection.html")


# Password protection page (before accessing wishes)
@app.route("/password", methods=["GET"])
def password_protection():
    return render_template("password_protection.html")


if __name__ == "__main__":
    app.run(debug=True)

