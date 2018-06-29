import mongoengine_goodjson as gj
import mongoengine as db
from datetime import datetime


class Address(gj.EmbeddedDocument):
    address = db.StringField(required=True, max_length=200)
    neighborhood = db.StringField(required=True, max_length=100)
    zip_code = db.IntField(required=True)
    county = db.StringField(required=True, max_length=200)
    state = db.StringField(required=True, max_length=100)


class School(gj.Document):
    code_inep = db.StringField(required=True, max_length=10, unique=True)
    address = db.EmbeddedDocumentField(Address)
    nameSchool = db.StringField(required=True, unique=True, max_length=200)
    admDependency = db.StringField(required=True, max_length=100)
    locate = db.StringField(required=True, max_length=100)
    create_at = db.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nameSchool
