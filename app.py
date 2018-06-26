from bottle import Bottle, response
from infra import mongodb

app = Bottle()


@app.route("/school")
def index():
    try:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        response.status = 200
        return mongodb.find_all()
    except Exception as e:
        response.status = 400
        return e


@app.route("/school/<pk>")
def index(pk):
    try:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        response.status = 200
        return mongodb.find_id(pk)
    except Exception as e:
        response.status = 400
        return {"error": e}


if __name__ == "__main__":
    app.run(debug=None, reload=True)
