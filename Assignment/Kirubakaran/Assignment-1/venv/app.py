from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
   return render_template('home.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/crew')
def crew():
   return render_template('crew.html')

@app.route('/about')
def about():
   return render_template('about.html')


@app.route('/aboves')
def aboves():
   return render_template('aboves.html')

if __name__ == '__main__':
    app.run(debug=True)