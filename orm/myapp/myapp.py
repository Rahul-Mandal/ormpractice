import requests
import json

URL = 'http://127.0.0.1:8000/hello/'
#URL = 'http://127.0.0.1:8000/hi/'
def get_data(id = None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    r = requests.get(url = URL, headers=headers,data=json_data)
    print(r)
    data = r.json()
    print(data)
get_data(1)

def post_data():
    data ={ 'name': 'Rahul Mandal22', 'email': 'rahulmandal30010@gmail.com', 'user': None}
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers,data=json_data)
    data = r.json()
    print(data)
# post_data()
    


def put_data():
    data ={ 'id':3,'name': 'Rahul Manda', 'email': 'rahulmandal300@gmail.com', 'user': None}
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers,data=json_data)
    data = r.json()
    print(data)
# put_data()
    
def patch_data():
    data ={ 'id':3,'name': 'Rahul Manda', 'email': 'rahulmandal300@gmail.com', 'user': None}
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers,data=json_data)
    data = r.json()
    print(data)
#patch_data()

def delete_data(id = None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    headers = {'Content-Type':'application/json'}
    r = requests.delete(url = URL, headers=headers,data=json_data)
    data = r.json()
    print(data)
# delete_data(4)
