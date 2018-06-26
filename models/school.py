import mongoengine_goodjson as gj
import mongoengine as db


class School(gj.Document):
    nameSchool = db.StringField(required=True, unique=True, max_length=200)
    state = db.StringField(required=True, max_length=100)
    admDependency = db.StringField(required=True, max_length=100)
    locate = db.StringField(required=True, max_length=100)
    andress = db.StringField(required=True, max_length=200)

    def __str__(self):
        return self.nameSchool
