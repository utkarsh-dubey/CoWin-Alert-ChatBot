from bot import telegram_chatbot 
from urllib.request import Request, urlopen
import requests
import random
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
    replystr=""
    replystr2=""
    replystr3=""
    for i in reply:
        for j in i:
            replystr+=(j+'\n')
        replystr+="\n\n"
    for i in reply2:
        for j in i:
            replystr2+=(j+'\n')
        replystr2+="\n\n"
    for i in reply3:
        for j in i:
            replystr3+=(j+'\n')
        replystr3+="\n\n"
    
    id1=730962429
    id2=793329729
    id3=1099803385
    id4=1489029276
    if(replystr!=""):
        bot.send_message(replystr,id1)
        bot.send_message(replystr,id2)
        bot.send_message(replystr,id3)
    if(replystr2!=""):
        bot.send_message(replystr2,id1)
        bot.send_message(replystr2,id3)
    if(replystr3!=""):
        bot.send_message(replystr3,id2)
        bot.send_message(replystr3,id4)

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
