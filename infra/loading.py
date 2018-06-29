import requests
import json
from bs4 import BeautifulSoup as Bs
from infra import mongodb
from models.enums import MunicipalityEnum

URL = "http://idebescola.inep.gov.br/ideb"


def find_info_school(table_schools: list) -> None:
    for field in table_schools:
        r = requests.get(f"{URL}/escola/dadosEscola/{field.find_all('td')[0].text}")
        a = Bs(r.content, "html5lib")
        ls = list(map(lambda x: x.find_all("td")[1].text,
                      a.find("table", {'class', 'tabela', 'table-dados-escola'}).find_all('tr')))
        mongodb.insert(ls, a.find("legend", {'class', 'legend-dados-escola'}).text)


def find_county_by_state(state: str):
    r = requests.post(f"{URL}/get-municipio-by-uf", data={"pkCodEstado": MunicipalityEnum.get_county(state)})
    print(list(map(lambda x: (x['value'], x['text']), json.loads(r.content))))
    # print([a['value'], a['text'] for a in json.loads(r.content)])


def loading_data(state: str, county: int) -> None:
    request = requests.post(f"{URL}/consulta-publica", data={
        "pkCodEntidade": None,
        "pkCodEstado": MunicipalityEnum.get_county(state.upper()),
        "pkCodMunicipio": county,
        "idDependenciaAdm": None,
        "noZona": None,
        "idLocalizacaoDiferenciada": None,
        "codigoEscola": None,
        "noEntidade": None,
        "btnSearch": None
    })

    soup = Bs(request.content, "html5lib")
    data_school = soup.find("table", {'class', 'table-listar-escola'}).find_all('tr', {'class', 'coluna'})
    find_info_school(data_school)
