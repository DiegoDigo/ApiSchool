from bottle import Bottle, response, jinja2_view, TEMPLATE_PATH
from infra import mongodb
from infra.loading import loading_data
from infra.mongodb import count_loading
from models.enums import MunicipalityCounty

app = Bottle()

TEMPLATE_PATH[:] = ['templates']


@app.route('/', name='home')
@jinja2_view('home.html')
def home():
    return {'title': 'Hello world'}


@app.route("/v1/school", method=['GET'])
def get_schools():
    try:
        response.headers['Content-Type'] = 'application/json'
        response.status = 200
        return mongodb.find_all()
    except Exception as e:
        response.status = 400
        return e


@app.route("/v1/school/<pk>", method=['GET'])
def get_school_pk(pk):
    try:
        response.headers['Content-Type'] = 'application/json'
        response.status = 200
        return mongodb.find_id(pk)
    except Exception as e:
        response.status = 400
        return {"error": e}


@app.route("/v1/school/<state>/<county>", method=['GET'])
def get_county_state(state: str, county: str):
    try:
        response.headers['Content-Type'] = 'application/json'
        response.status = 200
        return mongodb.find_state_county(state, "São paulo")
    except Exception as e:
        response.status = 400
        return {"error": e}


@app.route("/v1/school/loading/<state>/<county>")
def load_county_state(state: str, county: int):
    try:
        response.headers['Content-Type'] = 'application/json'
        response.status = 200
        loading_data(state, county)
        return dict(imported_quantity=count_loading(state),
                    imported_state=MunicipalityCounty.get_county(state))

    except Exception as e:
        response.status = 400
        return {"error": e}


if __name__ == "__main__":
    app.run(debug=True, reload=True, host="localhost", port=8085)
