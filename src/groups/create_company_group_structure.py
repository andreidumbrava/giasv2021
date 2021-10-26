import http.client
import json

from env_vars import API_TOKEN

conn = http.client.HTTPSConnection("forfitydp.okta.com")
payload = json.dumps({
  "profile": {
    "name": "marketing",
    "description": "Marketing department"
  }
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'SSWS ' + API_TOKEN
}
conn.request("POST", "/api/v1/groups", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))