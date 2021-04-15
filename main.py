import requests
from datetime import datetime,timedelta
pixel_endpoint="https://pixe.la/v1/users"
USERNAME="sravya"
TOKEN="hjkw34adjsfnfdfgfh"
GRAPH_ID="graph7"
user_params={
  "token":"hjkw34adjsfnfdfgfh",
  "username":"sravya",
  "agreeTermsOfService":"yes",
  "notMinor":"yes",

}
#response=requests.post(url=pixel_endpoint, json=user_params)
#print(response.text)
graph_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs"
graph_params={
  "id":GRAPH_ID,
  "name":"reading graph",
  "unit":"hours",
  "type": "int",
  "color":"shibafu",
  "timezone":"Asia/Tokyo",

}
headers={
  "X-USER-TOKEN":TOKEN
}
#response=requests.post(url=graph_endpoint,json=graph_params, headers=headers)
#print(response.text)
pixel_creation_endpoint=f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today= datetime.now()
pixel_params={
  "date":today.strftime("%Y%m%d"),
  "quantity":"8",
}
response=requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)