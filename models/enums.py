from enum import Enum


class MunicipalityEnum(Enum):
    AC = 12
    AL = 27
    AP = 16
    AM = 13
    BH = 29
    CE = 23
    DF = 53
    ES = 32
    GO = 52
    MA = 21
    MT = 51
    MS = 50
    MG = 31
    PA = 15
    PB = 25
    PR = 41
    PE = 26
    PI = 22
    RJ = 33
    RN = 24
    RS = 43
    RO = 11
    RR = 14
    SC = 42
    SP = 35
    SE = 28
    TO = 17

    @classmethod
    def get_county(cls, county):
        return cls._member_map_[county].value


class MunicipalityCounty(Enum):
    AC = "Acre"
    AL = "Alagoas"
    AP = "Amapá"
    AM = "Amazonas"
    BA = "Bahia"
    CE = "Ceará"
    DF = "Distrito Federal"
    ES = "Espírito Santo"
    GO = "Goiás"
    MA = "Maranhão"
    MT = "Mato Grosso"
    MS = "Mato Grosso do Sul"
    MG = "Minas Gerais"
    PA = "Pará"
    PB = "Paraíba"
    PR = "Paraná"
    PE = "Pernambuco"
    PI = "Piauí"
    RJ = "Rio de Janeiro"
    RN = "Rio Grande do Norte"
    RS = "Rio Grande do Sul"
    RO = "Rondônia"
    RR = "Roraima"
    SC = "Santa Catarina"
    SP = "São Paulo"
    SE = "Sergipe"
    TO = "Tocantins"

    @classmethod
    def get_county(cls, county: str):
        return cls._member_map_[county.upper()].value.capitalize()
