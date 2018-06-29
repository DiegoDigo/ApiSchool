from bottle import Bottle, response
from infra import mongodb

app = Bottle()


@app.route("/school")
def get_schools():
    try:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        response.status = 200
        return mongodb.find_all()
    except Exception as e:
        response.status = 400
        return e


@app.route("/school/<pk>")
def get_school_pk(pk):
    try:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        response.status = 200
        return mongodb.find_id(pk)
    except Exception as e:
        response.status = 400
        return {"error": e}


@app.route("/school/<state>/<county>")
def get_county_state(state: str, county: str):
    try:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        response.status = 200
        return mongodb.find_state_county("São paulo", "São paulo")
    except Exception as e:
        response.status = 400
        return {"error": e}


if __name__ == "__main__":
    app.run(debug=None, reload=True)
