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

f = open('friend.yml', 'r', encoding='utf-8')
sitey = yaml.load(f.read(), Loader=yaml.FullLoader)
tsite = {}
for key in range(len(res)):
    id = res[key]['number']
    sitejson = "{" + getmidstring(res[key]['body'],"{","}") + "}"    
    if (len(res[key]["labels"]) >= 0) and (res[key]["labels"][0]["name"] == "pass"):      
      tsite[key] = json.loads(sitejson)
print(sitey["items"])
sitey["items"] = sitey["items"].append(tsite)
# stream = open("test/friend.yml", 'w+')
# yaml.safe_dump(sitey, stream, default_flow_style=False,allow_unicode=True)
