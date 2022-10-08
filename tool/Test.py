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
    if len(res[key]["labels"]) == 0:
       os.system(f"lighthouse {siteurl} --output json --output-path ./{id}.json")
       fp = open(f'./{id}.json','r',encoding='utf8')
       test_data = json.load(fp)
       headers = {'Authorization': 'token '+ os.environ["GHKEY"]}
       url = f"https://api.github.com/repos/Mlikiowa/BlogFriend/issues/{id}/comments" 
       post_data = {"body":fp.read()}
       print(os.environ["GHKEY"])
       print(requests.post(url,headers=headers, data=json.dumps(post_data)))
#except:
#    print('error')
