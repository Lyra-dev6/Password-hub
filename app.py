from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def check_strength(pwd):
    if len(pwd) < 6:
        return "Weak 🔴"
    
    has_digit = any(char.isdigit() for char in pwd)
    has_upper = any(char.isupper() for char in pwd)
    has_special = any(char in string.punctuation for char in pwd)
    
    score = sum([has_digit, has_upper, has_special])
    
    if len(pwd) >= 12 and score == 3:
        return "Strong 🟢"
    elif len(pwd) >= 8 and score >= 1:
        return "Medium 🟡"
    else:
        return "Weak 🔴"
    
@app.route("/", methods=["GET", "POST"])
def home():
    generated_password = ""
    strength_result = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate":
            length = int(request.form.get("length", 12))
            characters = ""
            
            if request.form.get("letters"):
                characters += string.ascii_letters
            if request.form.get("numbers"):
                characters += string.digits
            if request.form.get("symbols"):
                characters += string.punctuation

            if not characters:
                characters = string.ascii_letters

            generated_password = "".join(random.choice(characters) for _ in range(length))

        elif action == "check":
            password_to_check = request.form.get("password_to_check", "")
            strength_result = check_strength(password_to_check)

    return render_template("index.html", password=generated_password, strength=strength_result)

if __name__ == "__main__":
    app.run(debug=True)


