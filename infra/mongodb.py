from mongoengine import connect
from models.school import School, Address

connect('schools', host='localhost', port=27017)


def insert(data: list, name: str):
    School(code_inep=data[0],
           address=Address(address=data[1].strip().capitalize(),
                           neighborhood=data[2].capitalize(),
                           zip_code=int(data[3].replace("-", "")),
                           county=data[4].capitalize(),
                           state=data[5].capitalize()),
           nameSchool=name.capitalize(),
           admDependency=data[6].capitalize(),
           locate=data[7].capitalize()).save()


def find_all() -> list:
    return School.objects().to_json()


def find_name(name: str) -> str:
    return School.objects(nameSchool=name).get().to_json()


def find_id(pk: str) -> str:
    return School.objects(pk=pk).get().to_json()


def find_state_county(state: str, county: str) -> str:
    return School.objects.filter(address__state=state, address__county=county).to_json()


if __name__ == "__main__":
    pprint(School.objects.filter(address__state='sao paulo', address__county='São paulo').to_json())
