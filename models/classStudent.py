from werkzeug.security import generate_password_hash
from db import db


class ClassStudentModel(db.Model):
    __tablename__ = "classStudent"

    id = db.Column(db.Integer, primary_key=True)
    classId = db.Column(db.Integer, nullable=False)
    studentId = db.Column(db.Integer, nullable=False)

    def __init__(self, classId, studentId):
        self.classId = classId
        self.studentId = studentId

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.filter_by()

    @classmethod
    def find_by_class_id(cls, _classId):
        return cls.query.filter_by(classId=_classId).all()

    @classmethod
    def find_by_class_id_student_id(cls, _classId, _studentId):
        return cls.query.filter_by(classId=_classId, studentId=_studentId).first()