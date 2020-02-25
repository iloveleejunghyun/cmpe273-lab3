from ariadne import QueryType, MutationType, ObjectType
from MyErrors import RequiredAtLeastOne
from models.clazz import ClassModel
from models.classStudent import ClassStudentModel
from models.student import StudentModel
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_raw_jwt,
    jwt_refresh_token_required,
    fresh_jwt_required,
    create_access_token,
    create_refresh_token,
    get_csrf_token,
    verify_fresh_jwt_in_request
)
from blacklist import BLACKLIST
import datetime
from tokens import set_tokens

query = QueryType()
mutation = MutationType()
User = ObjectType("Class")


@query.field("class")
def resolve_class(_, info, **kwargs):
    id = kwargs.get("id", None)
    clazz = None
    studentList = []
    if id:
        clazz = ClassModel.find_by_id(id)
        if clazz:
            maps = ClassStudentModel.find_by_class_id(id)
            if maps:
                for classStudent in maps:
                    student = StudentModel.find_by_id(classStudent.studentId)
                    studentList.append(student)
            return {"id":id, "name":clazz.name, "students" : studentList}
    return {"id":id, "name":"class not found", "students" : []}

@query.field("classes")
def resolve_classes(_, info):
    classes = ClassModel.find_all()
    print(type(classes))
    # modify add students
    return classes


@mutation.field("createClass")
def resolve_create_class(_, info, name):
    clazz = ClassModel(name)
    clazz.save_to_db()
    return clazz


@mutation.field("addStudentToClass")
def resolve_add_student_to_class(_, info, classId, studentId):
    clazz = ClassModel.find_by_id(classId)
    student = StudentModel.find_by_id(studentId)
    if clazz:
        if student:
            csmMap = ClassStudentModel(classId, studentId)
            csmMap.save_to_db()
            return {"id":clazz.id, "name":clazz.name, "students" : [student]}
    return {"id":classId, "name":"student or class not found", "students" : []}
    # return csmMap