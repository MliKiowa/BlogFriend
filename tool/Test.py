
# -*- coding: utf-8 -*-
import requests
import sys,json
def take_middle_text(txt,txt_s,txt_e='',seeks=0,seeke=0):#取中间文本函数
    try:
        if txt_e or seeks or seeke:
            pass
        else:
            raise 1
        s_1 = txt.find(txt_s)
        if s_1 == -1:
            raise 1
        l_1 = len(txt_s)
        if txt_e:
            s_2 = txt.find(txt_e,s_1)
            if s_1 == -1 or s_2 == -1:
                return False
            return txt[s_1+l_1:s_2]
        if seeks:
            return txt[s_1-seeks:s_1]
        if seeke:
            return txt[s_1+l_1:s_1+l_1+seeke]
    except:
        return '传参错误或未找到传参文本'

url = "https://api.github.com/repos/Mlikiowa/BlogFriend/issues" 
res = requests.get(url).json
for key in range(len(res)):
    print(res[key]['body'])
    site = take_middle_text(res[key]['body']',"```","```")
    print(site)
    tempsite = json.loads(site)
    print(site.url)
