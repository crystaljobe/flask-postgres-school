from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy

school_app = Flask(__name__)

school_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://crystaljobe@localhost/school2'

db = SQLAlchemy(school_app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    subject_name = db.relationship('subject', backref=db.backref('student'))
    
class Subjects(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(10))
    
class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    subject_name = db.relationship('subject', backref=db.backref('teachers'))
    
    
@school_app.route('/students/', methods=['GET'])
def get_students():
    students = Student.query.all()
    json_students = [{'id': stud.id, 'first_name': stud.first_name, 'last_name': stud.last_name, 'age': stud.age, 'class': {'subject': stud.subject_name.subject}} for stud in students]
    return jsonify(json_students)

#response = Response(json.dumps(student_list, sort_keys=False), mimetype='application/json')

#@school_app.route('/students/', methods=['GET'])
#def get_teachers():

school_app.run(debug=True)
