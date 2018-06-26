import requests
from bs4 import BeautifulSoup as Bs
from infra import mongodb

URL = "http://idebescola.inep.gov.br/ideb"

if __name__ == "__main__":
    request = requests.post(f"{URL}/consulta-publica",
                            data={
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
    a = Bs(request.content, "html5lib")
    r = a.find("table", {'class', 'table-listar-escola'}).find_all('tr', {'class', 'coluna'})
    for i in r:
        print([t.text for t in i.find_all("td")])
        mongodb.insert([t.text for t in i.find_all("td")])
