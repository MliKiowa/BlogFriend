# -*- coding: utf-8 -*-
import requests
import sys,json,os,yaml
def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

url = "https://api.github.com/repos/Mlikiowa/BlogFriend/issues" 
res = requests.get(url).json()
for key in range(len(res)):
    id = res[key]['number']
    sitejson = "{" + getmidstring(res[key]['body'],"{","}") + "}"    
    if (len(res[key]["labels"]) >= 0) and (res[key]["labels"][0]["name"] == "pass"):
      sitey = yaml.load(sitejson, Loader=yaml.FullLoader)
      stream = open("test/friend.yaml", 'w+')
      yaml.safe_dump(sitey, stream, default_flow_style=False)
