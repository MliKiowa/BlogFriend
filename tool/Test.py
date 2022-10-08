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
#try:
for key in range(len(res)):
    print(res[key]['id'])
    id = res[key]['number']
    site = "{"+getmidstring(res[key]['body'],"{","}")+"}"    
    tempsite = json.loads(site)
    siteurl = tempsite["url"]
    print(tempsite["url"])
    if "labels" not in res[key]:
       os.system(f"lighthouse {siteurl} --output json --output-path ./{id}.json")
       with open(f'./{id}.json','r',encoding='utf8')as fp:
       test_data = json.load(fp)
       headers = {'Authorization': 'oauth '+ os.environ["GHKEY"]}
       url = "https://api.github.com/repos/Mlikiowa/BlogFriend/issues/{id}/comments" 
       post_data = {"body":"test"}
       requests.post(url,post_data,headers)
#except:
#    print('error')
