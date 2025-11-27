from flask import Flask, render_template, request, redirect, url_for, session
import json, os


app = Flask(__name__)
DATA_FILE = "data.json"
UPLOAD_FOLDER = "static/images"
app.secret_key = "my_super_secret_key_2025" 

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        return json.dump(data, f, indent=4)
    

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/validation')
def validation():
    data = load_data()
    return render_template('validation.html', data=data)

@app.route('/register', methods=["GET", "POST"])
def register():
    data = load_data()
    if request.method == "POST":
        data['fName'] = request.form['f-name']
        data['lName'] = request.form['l-name']

        save_data(data)

    return render_template('register.html', data=data)


@app.route('/ribpay')
def ribpay():
    data = load_data()
    return render_template('ribpay.html', data=data)



APP_USERNAME = ["admin2025", "admindev", "dev"]
ADMIN_USERNAME = APP_USERNAME[1]
ADMIN_PASSWORD = "22222"

@app.route("/login", methods=['GET', "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        username = request.form["username"]
        if password == ADMIN_PASSWORD and username in APP_USERNAME:
            session["is_admin"] = True
            return redirect("/admin")
        else:
            return "Invalid username and password" and render_template("login.html")
            
    return render_template("login.html")




@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('is_admin'):
        return redirect('/login')

    data = load_data()
    if request.method == 'POST':
        data['productPrice'] = request.form['price']
        data['productName'] = request.form['product-name']
        data['productTax'] = request.form['product-tax']
        data['totalPrice'] = request.form['total-price']

        data['agent'] = request.form['agent']

        data['titulaire'] = request.form['titulaire']
        data['iban'] = request.form['iban']
        data['bic'] = request.form['bic']

        data['lastSeen'] = request.form['last-seen']
        data['lastMsg'] = request.form['last-msg']
        

        mainImg = request.files.get('main-photo')
        if mainImg:
            main_img_path = f'static/images/{mainImg.filename}'
            mainImg.save(main_img_path)
            data['mainImg'] = f'/{main_img_path}'

        save_data(data)

    return render_template('admin.html', data=data)









if __name__ == "__main__":
    app.run(debug=True)