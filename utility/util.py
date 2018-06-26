from json import JSONEncoder
from bson import ObjectId
from mongoengine import Document


class ObjEncoder(JSONEncoder):

    def default(self, obj, **kwargs):
        if isinstance(obj, Document):
            return obj.to_mongo()
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return JSONEncoder.default(self, obj)
