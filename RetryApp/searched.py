import play_scraper as ps
from google_play_scraper import app as gapp
import requests as rs
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote
import time

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

class SoftwareDetails():

    def searchedsoftware(self,soft):
        detail = []
        disc = []
        result = rs.get("https://filehippo.com/search/?q="+str(soft))
        soup = bs(result.text,"html.parser")
        list = soup.findAll('li',{'class':'list-programs__item'})
        url = list[1].a['href']
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
        for p in disr[0]:
            disc.append(p.text)

        return (logo,download,detail,disc)

class WebsiteDetails():

    def searchedwebsite(self,web):
        ranks_val = []
        field_name = []
        Traffic_val = []
        country_traf = []
        country_traf_val =[]
        audiance_interest = []
        url = 'https://www.similarweb.com/website/'+str(web)+'.com/'
        handler = urlopen('https://api.proxycrawl.com/?token=DBFO18FPHMUm0En4IYFQig&url=' + url)
        result = handler.read()
        time.sleep(5)
        soup = bs(result,'html.parser')
        ranks = soup.findAll('div',{'class':'websiteRanks-container'})

        name = ranks[0].find_all('a',{'class':"websiteRanks-nameText"})
        for i in range(len(name)):
            field_name.append(name[i].text)
        time.sleep(1)
        logo = soup.findAll('img',{'class':'websiteHeader-screenImg'})
        img_logo = logo[0]['src']
        time.sleep(1)
        rank = ranks[0].find_all('div',{'class':"websiteRanks-valueContainer js-websiteRanksValue"})
        for i in range(len(rank)):
            ranks_val.append(rank[i].text.split())
        time.sleep(1)
        desc = soup.findAll('div',{'class':'websiteHeader-companyDescriptionWrapper'})[0].p.text

        Traffic_over = soup.findAll('span',{'class':'engagementInfo-valueNumber js-countValue'})
        for i in range(len(Traffic_over)):
            Traffic_val.append(Traffic_over[i].text)
        time.sleep(1)
        coun_tra = soup.findAll('a',{'class':'country-name country-name--link'})
        for i in range(len(coun_tra)):
            country_traf.append(coun_tra[i].text)

        coun_tra_val = soup.findAll('span',{'class':'traffic-share-valueNumber js-countValue'})
        for i in range(len(coun_tra_val)):
            country_traf_val.append(coun_tra_val[i].text)

        audiance = soup.findAll('a',{'class':'audienceCategories-itemLink'})
        for i in range(len(audiance)):
            audiance_interest.append(audiance[i].text)

        return (field_name,ranks_val,desc,Traffic_val,country_traf,country_traf_val,audiance_interest,img_logo)
