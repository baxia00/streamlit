import requests
from fake_useragent import UserAgent

headers = {'User-Agent':UserAgent().random}
base_url = "https://www.sznest.net/_backup/html/get_the_real_address_of_Tencent_video_ajax.php"



def get_rel_url(url): 

    data = {
            "userip":"183.198.90.104",
            "weburl":url,
            "temprealurl":""
    }
   
    try:
        r = requests.post(base_url,headers=headers,data=data,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("获取了个寂寞！")

if __name__ == '__main__':

    url = "https://v.qq.com/x/page/g3116qm34rs.html"
    print(get_rel_url(url))
    