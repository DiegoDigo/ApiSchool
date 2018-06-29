import requests
from bs4 import BeautifulSoup as Bs
from infra import mongodb

URL = "http://idebescola.inep.gov.br/ideb"


def find_info_school(table_schools: list):
    for field in table_schools:
        r = requests.get(f"{URL}/escola/dadosEscola/{field.find_all('td')[0].text}")
        a = Bs(r.content, "html5lib")
        ls = list(map(lambda x: x.find_all("td")[1].text,
                      a.find("table", {'class', 'tabela', 'table-dados-escola'}).find_all('tr')))
        mongodb.insert(ls, a.find("legend", {'class', 'legend-dados-escola'}).text)


if __name__ == "__main__":
    request = requests.post(f"{URL}/consulta-publica", data={
        "pkCodEntidade": None,
        "pkCodEstado": 35,
        "pkCodMunicipio": 3550308,
        "idDependenciaAdm": None,
        "noZona": 1,
        "idLocalizacaoDiferenciada": None,
        "codigoEscola": None,
        "noEntidade": None,
        "btnSearch": None
    })
    soup = Bs(request.content, "html5lib")
    data_school = soup.find("table", {'class', 'table-listar-escola'}).find_all('tr', {'class', 'coluna'})
    find_info_school(data_school)
