from bot import telegram_chatbot 
from urllib.request import Request, urlopen
import json
from time import sleep
bot=telegram_chatbot("config.cfg")
update_id=None

def make_reply(msg=""):
    url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=149&date=13-05-2021"
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
            if(i["available_capacity"]<3):
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


while True:
    prev=[]
    print("...")
    reply=make_reply()
    if(prev==reply):
        sleep(15)

    if(reply==""):
        continue
    replystr=""
    for i in reply:
        for j in i:
            replystr+=(j+'\n')
        replystr+="\n\n"
    
    id1=730962429
    id2=793329729
    bot.send_message(replystr,id1)
    bot.send_message(replystr,id2)
    prev=reply

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