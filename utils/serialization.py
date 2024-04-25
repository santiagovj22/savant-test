from uuid import UUID
import json

class Serialize(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
    

    def json_convert(obj):
        string_data = json.dumps(obj, cls=Serialize)
        return json.loads(string_data)