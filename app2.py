from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('index.html', user_name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dept')
def dept():
     return render_template('dept.html')

@app.route('/art')
def art():
     return render_template('art.html')


if __name__=="__main__":
      app.run(debug=True)

      