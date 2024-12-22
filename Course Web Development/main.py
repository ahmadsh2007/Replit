from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    datePosted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Event('{self.title}', '{self.datePosted}')"

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('aboutUs.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)