from mongoengine import connect
from models.school import School

connect('schools', host='localhost', port=27017)


def insert(data: list):
    School(nameSchool=data[1],
           state=data[2].split("-")[1],
           admDependency=data[3],
           locate=data[4],
           andress=data[5]).save()


def find_all() -> list:
    return School.objects().to_json()


def find_name(name: str) -> str:
    try:
        model = School.objects(nameSchool=name).get()
        return model.to_json()
    except Exception:
        return None


def find_id(pk: str) -> str:
    model = School.objects(pk=pk).get()
    return model.to_json()
