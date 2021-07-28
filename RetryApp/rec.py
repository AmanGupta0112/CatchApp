import play_scraper as ps
from google_play_scraper import app as gapp
import requests as rs
from bs4 import BeautifulSoup as bs
from RetryAccount import models
from . import searched
import random


def Recommend(request_post):
    # import pdb; pdb.set_trace()
    User_id=request_post.user.id
    user = models.Profile.objects.filter(user_id=User_id).values('Profession','Interest')[0]
    intres = user['Interest']
    interests = random.sample(intres,2)
    pro = user['Profession'].split(" ")
    st = ''
    for i in range(0,len(pro)):
        st += pro[i].lower()
    app_data = []
    for interest in interests:
        app = ps.search(interest,page=1)
        app_data.append(app)

    data_dict = {}
    result = rs.get("https://download.cnet.com/s/"+str(st)+"/?platform=windows")
    soup = bs(result.text,"html.parser")
    list_d = soup.findAll('div',{'class':'g-grid-container u-grid-columns c-searchResults-search'})

    ls = list_d[0].text.split("\n")
    a = list_d[0].find_all('a')
    img = list_d[0].find_all('img')
    for i in range(1,len(list_d[0]),2):
        data_list = []
        title = (ls[i])
        data_list.append(title)
        disc = ls[i-1]
        data_list.append(disc)
        data_dict[i] = data_list
    return(app_data, data_dict)
