from boxsdk import Client
    
def get_box_client_login(client: Client):
    user = client.user()
    userGet = user.get()
    return userGet.login