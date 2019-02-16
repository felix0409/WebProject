import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133875.mlab.com:33875/subscribers
host = "ds133875.mlab.com"
port = 33875
db_name = "subscribers"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())