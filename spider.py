import requests
from bs4 import BeautifulSoup
from time import sleep
import os, sys
# 将django项目根目录加入环境变量
parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_path)
# 引入django配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Products.settings")
# 启动django
import django
django.setup()
from app.models import *

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Host": "www.cgi.gov.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

url = "http://www.cgi.gov.cn/Products/List/?page=%s"
max_page = 147

def get_response(page):
    response = requests.get(url=url%page,headers=headers)
    # print(response.text)
    return response.text

def get_info():
    for i in range(1,max_page+1):
        response = get_response(i)
        soup = BeautifulSoup(response,"html.parser")
        result = soup.findAll("div", class_="ProItemBox")
        for i in result:
            #获取需要的内容段
            temp = i.findAll("tr")
            #获取原图片
            img = temp[0].a.img['src']
            #获取特色产品
            product = temp[1].a.string
            #获取地点
            province = temp[2].a.string
            insert_data(province,product)
            #防止数据库locked
            sleep(0.1)
        sleep(3)


def insert_data(*args):
    province_name = str(args[0]).strip()
    province_name = province_name.strip("[").strip("]")
    product = str(args[1]).strip()
    p = Province.objects.filter(name=province_name)
    if p:
        #存在省份
        print("已存在省份:%s"%province_name)
        p = p.first()
    else:
        p = Province.objects.create(name=province_name)
    flag = Goods.objects.filter(provice=p, name=product)
    if flag:
        print("已经存在数据")
    else:
        Goods.objects.create(name=product, provice=p)
        print("插入数据%s成功"%product)


get_info()
