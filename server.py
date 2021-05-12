from bot import telegram_chatbot 
from urllib.request import Request, urlopen
# from urllib2 import urlopen
# from urllib2 import Request
import json
from time import sleep
bot=telegram_chatbot("config.cfg")
update_id=None

def make_reply(url):
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(req).read()
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
while True:
    sleep(4)
    
    print("...")
    url1="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=149&date=13-05-2021"
    url2="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=145&date=13-05-2021"
    reply=make_reply(url1)
    sleep(4)
    reply2=make_reply(url2)
    if(prev==reply and prev2==reply2):
        sleep(15)

    if(reply=="" and reply2==""):
        continue
    replystr=""
    replystr2=""
    for i in reply:
        for j in i:
            replystr+=(j+'\n')
        replystr+="\n\n"
    for i in reply2:
        for j in i:
            replystr2+=(j+'\n')
        replystr2+="\n\n"
    
    id1=730962429
    id2=793329729
    id3=1099803385
    if(replystr!=""):
        bot.send_message(replystr,id1)
        bot.send_message(replystr,id2)
        bot.send_message(replystr,id3)
    if(replystr2!=""):
        bot.send_message(replystr2,id1)
        bot.send_message(replystr2,id3)

    prev=reply
    prev2=reply2

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