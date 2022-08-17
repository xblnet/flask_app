from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
    #return "This is home page"
    return render_template('home.html')

@application.route('/about')
def about():
    #return "This is about page"
    return render_template('about.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/project')
def projects():
    return render_template('project.html')

if __name__=='__main__':
    application.run(debug=True, host='localhost',port='5000')