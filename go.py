
import requests
from requests import exceptions 
import sys

#此程序作用是判断网站是否是中文网站

#判断字符串是否包含中文
def str_contain_chinese(str):
    for ch in str:
        if u'\u4e00'<=ch<=u'\u9fff':
            return True
    return False

def get_url(url):

    c=False
    
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }  # 构造请求头
    
    try:
        page=requests.get(url,headers=headers,timeout=3)
        page.encoding='utf-8'
        c = str_contain_chinese(page.text)

    except exceptions.Timeout as e:
        print('cuowu')
    except exceptions.HTTPError as e:
        print('cuowu')
    else:
        if page.status_code == 200:

            print('ok')
        else:
            print('none')

    return c

# 识别前的网站

fi=open('adult.txt','r')
txt=fi.readlines()
list1=[]
for w in txt:
    w=w.replace('\n','')
    list1.append(w)
#print(list1)


# 识别后的网站
list2 = []
for url in list1:
    #eurl = r'https://'+url
    eurl = r'http://'+url

    if(get_url(eurl)):
        list2.append(eurl)
    #print(get_url(eurl))



f=open("chadult.txt","w")
 
for line in list2:
    f.write(line+'\n')
f.close()



