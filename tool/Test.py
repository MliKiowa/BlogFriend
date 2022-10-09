# -*- coding: utf-8 -*-
import requests
import sys,json,os
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
    print(res[key]['id'])
    id = res[key]['number']
    site = "{"+getmidstring(res[key]['body'],"{","}")+"}"    
    tempsite = json.loads(site)
    siteurl = tempsite["url"]
    print(tempsite["url"])
    if len(res[key]["labels"]) == 0:
       os.system(f"lighthouse {siteurl} --output html --output-path ./test/site–{id}.html")
       # os.system(f"git add ./test/site–{id}.html")        
       headers = {'Authorization': 'token '+ os.environ["GHKEY"]}
       url = f"https://api.github.com/repos/Mlikiowa/BlogFriend/issues/{id}/comments" 
       Test_Url = f"https://friend.nanaeo.cn/test/site%E2%80%93{id}.html"  
       post_data = {"body":"LightHouse Testing Ok,Then Go [there]({Test_Url})"}      
       print(requests.post(url,headers=headers, data=json.dumps(post_data)))
       url = f"https://api.github.com/repos/Mlikiowa/BlogFriend/issues/{id}/labels" 
       post_data = {"labels":["suspend"]}      
       print(requests.post(url,headers=headers, data=json.dumps(post_data)))
