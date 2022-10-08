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
    print(res[key]['body'])
    site = "{"+getmidstring(res[key]['body'],"{","}")+"}"    
    tempsite = json.loads(site)
    print(tempsite.url)
    os.system(f"lighthouse {tempsite.url} --output json --output-path ./{tempsite.url} .json")
#except:
#    print('error')
