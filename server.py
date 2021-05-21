from bot import telegram_chatbot 
from urllib.request import Request, urlopen
import requests
import random
import json
import datetime
# from urllib2 import urlopen
# from urllib2 import Request
import json
from time import sleep
bot=telegram_chatbot("config.cfg")
update_id=None
daty=(datetime.datetime.today()+datetime.timedelta (days=1)).strftime ('%d-%m-%Y')
print(daty)
def make_reply(url):

    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()
    except requests.exceptions.ConnectionError as e:
        pass
    except Exception as e:
        #logger.error(e)
        randomtime = random.randint(1,5)
        print('ERROR - Retrying again website %s, retrying in %d secs' % (url, randomtime))
        #logger.warn('ERROR - Retrying again website %s, retrying in %d secs' % (url, randomtime))
        sleep(randomtime)
        return make_reply(url)

    if(data==None or data==""):
        reply=""
    else:
        dict=(json.loads(data))
    if(dict["sessions"]==[]):
        reply=""
    else:
        reply=[]
        for i in dict["sessions"]:
            temp=[]
            if(i["min_age_limit"]!=18):
                continue
            if(i["available_capacity"]==1):
                continue

            temp.append("Centre Name - "+str(i["name"]))
            temp.append("District Name - "+str(i["district_name"]))
            temp.append("Available Capacity - "+str(i["available_capacity"]))
            temp.append("Age limit - "+str(i['min_age_limit']))
            temp.append("Vaccine - "+str(i['vaccine']))
            temp.append("Fee - "+str(i["fee_type"]))
            reply.append(temp)
    if(reply==[]):
        reply=""
    return reply

prev=[]
prev2=[]
prev3=[]
while True:
    
    urlop="https://api.telegram.org/bot1898081410:AAHGGZ4kY8rv-hX_q32oFXeaggyDBKX-O5k/getUpdates"
    sleep(3)
    print("...")
    url1="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=149&date="+daty
    url2="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=145&date="+daty
    url3="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=143&date="+daty
    reply=make_reply(url1)
    sleep(3)
    reply2=make_reply(url2)
    sleep(3)
    reply3=make_reply(url3)
    if(prev==reply and prev2==reply2 and prev3==reply3):
        sleep(15)

    if(reply=="" and reply2=="" and reply3==""):
        continue
    southdelhi=""
    eastdelhi=""
    northwestdelhi=""
    for i in reply:
        for j in i:
            southdelhi+=(j+'\n')
        southdelhi+="\n\n"
    for i in reply2:
        for j in i:
            eastdelhi+=(j+'\n')
        eastdelhi+="\n\n"
    for i in reply3:
        for j in i:
            northwestdelhi+=(j+'\n')
        northwestdelhi+="\n\n"
    dicy={}
    dicy["southdelhi"]=southdelhi
    dicy["eastdelhi"]=eastdelhi
    dicy["northwestdelhi"]=northwestdelhi

    print(bot.get_updates)
    file=open('bot.txt','r')
    users=json.loads(file.read())
    for i in users:
        for j in users[i]:
            if j in dicy:
                if(dicy[j]!=""):
                    print(dicy[j])
                    print(i)
                    op=int(i)
                    bot.send_message(dicy[j],i)
        print(i)
##    if(southdelhi!=""):
##        bot.send_message(southdelhi,id1)
##        bot.send_message(southdelhi,id2)
##        bot.send_message(southdelhi,id3)
##    if(eastdelhi!=""):
##        bot.send_message(eastdelhi,id1)
##        bot.send_message(eastdelhi,id3)
##    if(northwestdelhi!=""):
##        bot.send_message(northwestdelhi,id2)
##        bot.send_message(northwestdelhi,id4)

    prev=reply
    prev2=reply2
    prev3=reply3
    # updates=bot.get_updates(offset=update_id)
    # updates=updates["result"]

    # if updates:

    #     for item in updates:
    #         update_id=item["update_id"]
    #         try:
    #             message = item["message"]["text"]
    #         except:
    #             message=None

    #         from_=item["message"]["from"]["id"]
    #         reply=make_reply(message)
    #         bot.send_message(reply,from_)
