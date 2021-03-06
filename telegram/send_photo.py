


import telegram
import time
import datetime
import glob
import os
import requests

REQUEST_URL = 'https://api.telegram.org/bot694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk'
BOT_API = '694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk'
USER_ID = -318152844

def send_files( typ , number, path):
    send_para = ""
    send_typ = ""
    if(typ == 'mp4'):
        send_para = "/sendVideo"
        send_typ = 'video'
    else:
        send_para = '/sendPhoto'
        send_typ = 'photo'
    
    path = path + '*/*/*' + typ
    list_of_files = glob.glob(path)
    list_of_files.sort(key=os.path.getctime)
    number = number*-1
    list_files_send = list_of_files[number:]
    bot = telegram.Bot(token=BOT_API)


    
    #print(bot.get_me())
    time_now = datetime.datetime.now()
    time_message = 'Kamera 1: \nMotion detected at: '+ str(time_now)
    #bot.sendMessage(chat_id=-318152844, text=time_message)

    #bot.sendPhoto(-318152844, latest_file)
    user_id = USER_ID
    #REQUEST_URL = 'https://api.telegram.org/bot694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk'
    data = {'chat_id': user_id}
    for item in list_files_send:
        imagePath = item
        print item
        files = { send_typ: (imagePath, open(imagePath, "rb"))}
        requests.post(REQUEST_URL + send_para, data=data, files=files)
        
def send_snapshot( typ , number , path):
    send_para = ""
    send_typ = ""
    if(typ == 'mp4'):
        send_para = "/sendVideo"
        send_typ = 'video'
    else:
        send_para = '/sendPhoto'
        send_typ = 'photo'
    
    path = path + '*' + typ
    list_of_files = glob.glob(path)
    list_of_files.sort(key=os.path.getctime)
    number = number*-1
    list_files_send = list_of_files[number:]
    bot = telegram.Bot(token=BOT_API)


    
    #print(bot.get_me())
    #time_now = datetime.datetime.now()
    #time_message = 'Kamera 1: \nMotion detected at: '+ str(time_now)
    #bot.sendMessage(chat_id=-318152844, text=time_message)

    #bot.sendPhoto(-318152844, latest_file)
    user_id = USER_ID
    
    data = {'chat_id': user_id}
    for item in list_files_send:
        imagePath = item
        print item
        files = { send_typ: (imagePath, open(imagePath, "rb"))}
        requests.post(REQUEST_URL + send_para, data=data, files=files)
    
    '''
    data = {'chat_id': user_id}
    files = {'video': (imagePath, open(imagePath, "rb"))}
    requests.post(REQUEST_URL + '/sendVideo',text=time_message, data=data, files=files)
    '''

#send_files( 'mp4' , 2)

