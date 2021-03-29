from boxsdk import JWTAuth, Client
import json

def get_box_client(path_to_json):

    with open(path_to_json) as json_file:
            data = json.load(json_file)

    auth = JWTAuth.from_settings_dictionary(data)
    client = Client(auth)

    return client
