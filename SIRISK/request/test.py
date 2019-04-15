import requests
import json
url='https://test-client-api.corpository.com/clientapi/api/demo'
# endpoint='demo'
# myToken = '6a7f708a7ba06d6bea3076ded83f8394ebdab4ff'
#
# head = {'Authorization': 'token {}'.format(myToken)}
# print('token {}'.format(myToken))
# resp= requests.get(url+endpoint, headers=head)
new_std = {"request": "searchCompanies",
           "para": {
               "api_auth_token": "x25TaJuE2nN6IKn5bYSpGrQpyCYtj4xD",
               "user_id": "899",
               "source_system": "clientapi",
               "search-criteria": {
                   "company-ids": [],
                   "company-names": [],
                   "company-name-partials": ["EDELWEISS ASSET"],
                   "cins": [],
                   "cin-partials": [],
                   "partials-search-type": "",
                   "city": [],
                   "state": [],
                   "status": [],
                   "type": [],
                   "liability": [],
                   "offset-start": 0,
                   "offset-end": 10
               }
           }

           }
def create_demo(url,**new_std):
    headers = {'content-type':'application/json'}
    Json_Value=json.dumps(new_std)
    print(Json_Value)
    resp = requests.post(url, headers=headers,data=Json_Value)
    print(resp.status_code)
    print(resp.json())

create_demo(url,**new_std)