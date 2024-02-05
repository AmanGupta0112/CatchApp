import play_scraper as ps
from google_play_scraper import app as gapp
import requests as rs
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote
import time
from .constants import NEW_RELEASE,DOWNLOAD,SOFTWARE,POPULAR,WEBSITE
class AppDetails():

    def searchapp(self,app):
         result = ps.search(app, page=1)
         id = result[0]['app_id']
         appdetail = gapp(id)
         keys=   appdetail
         return keys,result[0]

    def NewRelease(self):
        app = ps.search("New Release",page=1)
        return app

    def Trending(self):
        app = ps.search("Trending",page=1)
        return app

class SoftwareDetails():

    def searchedsoftware(self,soft):
        detail = []
        disc = []
        result = rs.get(f"{SOFTWARE}{str(soft)}")
        soup = bs(result.text,"html.parser")
        list_d = soup.findAll('li',{'class':'list-programs__item'})
        try:
            url = list_d[1].a['href']
            final_re = rs.get(url)
            f_soup = bs(final_re.text,'html.parser')
            down = f_soup.findAll('div',{"class":"program-actions-header__download"})
            download = down[0].a['href']
            img = f_soup.findAll('div',{"class":"media__image"})
            logo = img[0].img['src']
            content = f_soup.findAll('dl',{"class":"program-technical"})
            for dd in content[0]:
                detail.append(dd.text)

            disr = f_soup.findAll('article',{"class":"program-description"})
            count =0
        except:
            pass
        try:
            disc.append(disr[0].text)
        except:
            for p in disr[0]:
                count+= 1
                if count == 3:
                    disc.append(p.text)
                else:
                    msg = "No discription available"
                    disc.append(msg)
        return (logo,download,detail,disc)

    def NewRelease(self):

        data_dict = {}
        result = rs.get(NEW_RELEASE)
        soup = bs(result.text,"html.parser")
        #
        list_d = soup.findAll('div',{'class':'c-globalCard lg:u-col-3 md:u-col-3 sm:u-col-2 c-productCard u-flexbox-column c-productCard-detailed'})

        for i in range(0,20):
            data_list = []
            try:
                title = list_d[i].text.split("\n")[1]
                data_list.append(title)
                disc = list_d[i].text.split("\n")[0]
                data_list.append(disc)
                img =  list_d[i].img['src']
                data_list.append(img)
                url = f"{DOWNLOAD}{str(list_d[i].a['href'])}"
                data_list.append(url)
            except:
                pass
            data_dict[i] = data_list
        return(data_dict)


    def Trending(self):

        data_dict = {}
        result = rs.get(POPULAR)
        soup = bs(result.text,"html.parser")
        list_d = soup.findAll('div',{'class':'c-globalCard lg:u-col-3 md:u-col-3 sm:u-col-2 c-productCard u-flexbox-column c-productCard-detailed'})

        for i in range(0,20):
            data_list = []
            try:
                title = list_d[i].text.split("\n")[1]
                data_list.append(title)
                disc = list_d[i].text.split("\n")[0]
                data_list.append(disc)
                img =  list_d[i].img['src']
                data_list.append(img)
                url = f"{DOWNLOAD}{str(list_d[i].a['href'])}"
                data_list.append(url)
            except:
                pass
            data_dict[i] = data_list
        return(data_dict)



class WebsiteDetails():

    def searchedwebsite(self,web):
        
        url = f'{WEBSITE}{str(web)}.com/'
        try:
            result = rs.get(url)

            soup = bs(result.text,'html.parser')
            data = soup.findAll('div',{'class':'___SFlex_11qft_gg_'})

            disc = soup.findAll('p',{'class':'___SText_6st4r_gg_ __color_6st4r_gg_ __fontSize_6st4r_gg_ __lineHeight_6st4r_gg_'})[3].text

            field_name = data[1].text


            logo = soup.findAll('img',{'class':'Favicon__img___3IQrT'})[0]['src']

            g_ranks_val = data[3].text
            c_ranks_val = data[4].text

            Traffic_val = data[6].text
            search_tra = data[8].text
            p_search_tra = data[10].text
            backlinks = data[12].text
        except:
            field_name = ""

            disc = ""
            logo = ""

            g_ranks_val =""
            c_ranks_val = ""

            Traffic_val = ""
            search_tra = ""
            p_search_tra = ""
            backlinks = ""


        return (url,field_name,g_ranks_val,c_ranks_val,disc,Traffic_val,search_tra,p_search_tra,backlinks,logo)
