from mongoengine import connect

from models.enums import MunicipalityCounty
from models.school import School, Address
from utility.decorations import log

connect('schools', host='localhost', port=27017)


@log("inserindo")
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


def count_loading(state: str) -> int:
    return len(School.objects.filter(address__state=MunicipalityCounty.get_county(state)))


def find_name(name: str) -> str:
    return School.objects(nameSchool=name).get().to_json()


def find_id(pk: str) -> str:
    return School.objects(pk=pk).get().to_json()


def find_state_county(state: str, county: str) -> str:
    return School.objects.filter(address__state=MunicipalityCounty.get_county(state)).to_json()
