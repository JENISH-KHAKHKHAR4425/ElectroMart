from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/about')
def about():
    return render_template('about us.html')  # Make sure the file name is about_us.html in templates/

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/product')
def product():
    return render_template('product.html')  # This handles <a href="product.html">

if __name__ == '__main__':
    app.run(debug=True)
