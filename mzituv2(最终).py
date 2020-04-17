import requests
from lxml import etree

class mzi():

    def __init__(self):

        self.url='https://www.mzitu.com/xinggan/page/{}'

        self.pn=1

        self.headers={
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': 'http://www.mzitu.com'
            }

    def OnePage(self):

        r=requests.get(self.url.format(self.pn),headers=self.headers)

        html=etree.HTML(r.text)

        link_list=[]

        for i in range(1,25):

            if i==4 or i==8 or i==12 or i==16 or i==23:

                pass

            else:

                link=html.xpath('//*[@id="pins"]/li['+str(i)+']/a/@href')

                link_list.append(link[0])

        return link_list

    def DownloadPage(self,link,num):

        for i in link:

            r=requests.get(i,headers=self.headers)

            html=etree.HTML(r.text)

            maxnum=html.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')


            for n in range(1,int(maxnum[0])+1):

                try:

                    pic=requests.get(i+'/'+str(n),headers=self.headers)

                    pic_html=etree.HTML(pic.text)

                    pic_link=pic_html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')

                    print(pic_link[0])

                    try:

                        one_pic=requests.get(pic_link[0],headers=self.headers)


                        with open(str(num)+'.jpg','wb') as file:

                            file.write(one_pic.content)
                        
                        num+=1

                        print(num)



                    except:

                        print('下载%s失败' % pic_link)

                        pass

                except:

                    print("读取%s失败" % pic_link)

                    pass

        return num

if __name__=="__main__":

    m=mzi()

    num=1

    for i in range(1,153):

        m.pn=i
        
        try:

            num=m.DownloadPage(m.OnePage(),num)

        except:

            print("第%i失败" % i)

            pass

        
