import requests
import json
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class tao():

    def __init__(self):

        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
            }

        self.session=requests.session()

        self.pic='code.png'

    def ge(self):

        r=self.session.get('https://passport.taoshouyou.com/api/sms/captcha?refresh=1',headers=self.headers)

        l=self.session.get('https://passport.taoshouyou.com'+r.text[32:-2],headers=self.headers)

        with open(self.pic,'wb') as f:

            f.write(l.content)

            f.close()

        captcha=Image.open(self.pic)
        
        result=pytesseract.image_to_string(captcha)

        print(result)

        


if __name__=='__main__':

    tao().ge()
