import requests
from bs4 import BeautifulSoup as Bs
from infra import mongodb
from datetime import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

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
    table_schools = a.find("table", {'class', 'table-listar-escola'}).find_all('tr', {'class', 'coluna'})

    for field in table_schools:
        r = request = requests.get(f"{URL}/escola/dadosEscola/{field.find_all('td')[0].text}")
        a = Bs(r.content, "html5lib")
        c = a.find("table", {'class', 'tabela', 'table-dados-escola'}).find_all('tr')
        ls = []
        for campo in c:
            ls.append(campo.find_all("td")[1].text)
            logging.info(f'importando {campo.find_all("td")[1].text}')
        mongodb.insert(ls, a.find("legend", {'class', 'legend-dados-escola'}).text)
