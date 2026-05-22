# Password Hub 
An interactive, dual-purpose web app featuring a customizable strong password generator and a visual password strength checker. Project #5 in my coding journey.

## Overview
As my fifth project—and my very first time building a website with a Python backend—this app combines aesthetic frontend design with server-side logic. My previous web projects used standard client-side JavaScript, but for this one, I wanted to learn how a backend server handles data. I used the Flask framework to connect my HTML forms to Python scripts that securely process user selections and calculate password strength ratings.

## How to Run It Locally
Since this website uses a Python backend, it requires a local server environment to run on your computer:

### Step 1: Install the Requirements
Open your terminal or VS Code PowerShell inside the project folder and install the Flask library by typing:
```bash
pip install -r requirements.txt
```

### Step 2: Start the Web Server
Launch the backend engine by running the main script:
```bash
python app.py
```
*(Note: If you are on a Mac, you may need to type `python3 app.py` instead).*

### Step 3: View the App
Look at your terminal logs for a local network address (it will look like `http://127.0.0.1:5000`). 
Hold **Ctrl** (or **Cmd** on Mac) and click the link, or simply open Google Chrome and type `localhost:5000` into your search bar to see the live site!

## Features
- **PPT-Style Sliding Transition:** Uses a custom viewport slider that smoothly swooshes left-to-right when you click the top toggle menu.
- **Customizable Generator:** Lets you mix and match uppercase/lowercase letters, numbers, and symbols to create a completely random string based on your preferred length.
- **Inline Copy Button:** Features a quick "Copy to Clipboard" button built directly into the password result bar that changes to a checkmark once clicked.
- **State-Saving Switch:** Includes a smart feature where the website remembers which screen you were on, landing you back on the Checker side even after the page reloads a result.

## What I Learned
- **Web Framework Setup:** Understanding how Flask uses strict directory routing to map backend variables into a frontend `templates` folder.
- **Form Action Handling:** Learning how to use `request.method == 'POST'` to read button clicks and process different actions from separate HTML forms on the same page.
- **Jinja Templating:** Passing Python strings into HTML using dynamic double-curly-brace `{{ }}` tags.
- **Styling External Components:** Figuring out how to import daisyUI components and override their default color schemes using exact hex codes.
- **Server Communication vs JavaScript:** Learning the difference between client-side script speeds and server-side page reloads, and how to combine a tiny bit of JS with Python to handle animations.

## Status
- Completed
