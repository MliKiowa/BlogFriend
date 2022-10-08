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
print(res)
try:
  for key in range(len(res)):
    print(res[key]['body'])
    site = getmidstring(res[key]['body'],"\`\`\`","\`\`\`")
    print(site)
    tempsite = json.loads(site)
    os.system(f"lighthouse {tempsite.url} --output json --output-path ./{tempsite.url} .json")
except:
    print('error')
