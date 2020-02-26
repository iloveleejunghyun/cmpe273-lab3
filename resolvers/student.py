from ariadne import QueryType, MutationType, ObjectType
from MyErrors import RequiredAtLeastOne
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
User = ObjectType("Student")


@query.field("student")
def resolve_student(_, info, **kwargs):
    # return "user"
    id = kwargs.get("id", None)
    user = None
    if id:
        user = StudentModel.find_by_id(id)
    return user


@query.field("students")
def resolve_students(_, info):
    users = StudentModel.find_all()
    return users


@mutation.field("createStudent")
def resolve_create_student(_, info, name):
    student = StudentModel.find_by_name(name)
    if not student:
        student = StudentModel(name)
        student.save_to_db()
    return student
