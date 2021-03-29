# -*- coding: utf-8 -*-
import requests, json, schedule, threading, os
from random import randint, randrange
from time import sleep

with open("config.json", encoding='utf-8-sig') as f: # cfg
    config = json.load(f)

authorization = str(config["authorization"]).rstrip().lstrip()
windows_title = config["windows_title"] 

telegram_notifications = config["telegram_notifications"] 
telegram_user_id = config["telegram_user_id"]  
telegram_bot_token = config["telegram_bot_token"]  

job_name = config["job_name"] 
min_price = config["min_price"] 
max_price = config["max_price"]
buy_slave = config["buy_slave"]
buy_fetter = config["buy_fetter"]
upgrade_slave = config["upgrade_slave"]

print(f'Windows title: {windows_title}')
print(f'Telegram notifications: {telegram_notifications}')
print(f'Job name: {job_name}')
print(f'Min price: {min_price}, max price: {max_price}')
print(f'Buy slave: {buy_slave}')
print(f'Buy fetter: {buy_fetter}')
print(f'Upgrade slave: {upgrade_slave}')
print(f'')

def myProfile():
    global authorization
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/start'
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while 1:
        response = requests.request('GET', url, headers=headers, data=payload)
        if response.status_code == 200:
            break
    return response.json()

def userProfile(user_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/user?id=' + str(user_id)
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while 1:
        response = requests.request('GET', url, headers=headers, data=payload)
        if response.status_code == 200:
            break
    return response.json()

def topUsers():
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/topUsers'
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()

def jobSlave(slave_id):
    global job_name
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/jobSlave'
    payload = json.dumps({'slave_id':slave_id, 
     'name':job_name[randrange(0, len(job_name))]})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when installing the job, possibly cooldown. Slave: {slave_id}')
        if telegram_notifications == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Error when installing the job, possibly cooldown. Slave: {slave_id}")
    elif response.status_code == 200:
        print(f'Set job: {slave_id}. Name: ' + userProfile(slave_id)['job']['name'])
        if telegram_notifications == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Set job: {slave_id}. Name: " + userProfile(slave_id)['job']['name'])
    else:
        print(f'Unknown error. Slave: {slave_id}')
        if telegram_notifications == True:
            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Unknown error. Slave: {slave_id}")

    return response.json()

def buyFetter(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buyFetter'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when buying fetter, possibly a cooldown. Slave: {slave_id}')
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Error when buying fetter, possibly a cooldown. Slave: {slave_id}")
    elif response.status_code == 200:
        print(f'Buy fetter: {slave_id}. Price: ' + str(int(userProfile(slave_id)['fetter_price'])))
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Buy fetter: {slave_id}. Price: "+ str(int(userProfile(slave_id)['fetter_price'])))
    else:
        print(f'Unknown error. Slave: {slave_id}')
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Unknown error. Slave: {slave_id}")
   
    return response.json()

def buySlave(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/buySlave'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when buying slave, possibly a cooldown. Slave: {slave_id}')
        if telegram_notifications == True:
          requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Error when buying slave, possibly a cooldown. Slave: {slave_id}")
    elif response.status_code == 200:
        print(f'Buy: {slave_id}. Price: ' + str(int(userProfile(slave_id)['price']/1.49998088027))) 
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Buy: {slave_id}. Price: " + str(int(userProfile(slave_id)['price']/1.5)))
    else:
        print(f'Unknown error. Slave: {slave_id}')
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Unknown error. Slave: {slave_id}")

    return response.json()

def slaveList(user_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/slaveList?id=' + str(user_id)
    payload = {}
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()['slaves']

def saleSlave(slave_id):
    url = 'https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0/saleSlave'
    payload = json.dumps({'slave_id': slave_id})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'Content-Type': "application/json",
     'authorization': authorization,
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com'}
    response = requests.request('POST', url, headers=headers, data=payload)
    if response.status_code == 422:
        print(f'Error when selling slave, possibly a cooldown. Slave: {slave_id}')
        if telegram_notifications == True:
          requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Error when selling slave, possibly a cooldown. Slave: {slave_id}")
    elif response.status_code == 200:
        print(f'Sell: {slave_id}. Price: ' + str(int(userProfile(slave_id)['sale_price']/1.49998088027)))
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Sell: {slave_id}. . Price: " + str(int(userProfile(slave_id)['sale_price']/1.5)))
    else:
        print(f'Unknown error. Slave: {slave_id}')
        if telegram_notifications == True:
           requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Unknown error. Slave: {slave_id}")

    return response.json()

def Profile():
    print('Profile?  0_o')
    me = myProfile()['me']
    if me['fetter_to'] != 0:
        if me['balance'] >= me['price']:
            if buy_slave == True:
                if int(slave['price']) >= min_price:
                        if int(slave['price']) <= max_price:
                           sleep(randint(config["min_delay"],config["max_delay"]))
                           buySlave(int(str(slave['id']).replace('-','')))
    me = myProfile()['me']
    slaves = myProfile()['slaves']
    
    for slave in slaves:
        if slave['job']['name'] == '':
            sleep(randint(config["min_delay"],config["max_delay"]))
            jobSlave((slave['id']))

        if slave['fetter_price'] <= me['balance'] and slave['fetter_to'] == 0:
            if buy_fetter == True:
                           sleep(randint(config["min_delay"],config["max_delay"]))
                           buyFetter(int(str(slave['id']).replace('-','')))

def ThreadProfile():
    my_thread = threading.Thread(target=Profile)
    my_thread.start()

me = myProfile()['me']
schedule.every(1).minutes.do(ThreadProfile)

while True:
    try:
        me = myProfile()['me']
        if windows_title == True:
           os.system(f'title Your ID: ' + str(me['id']) +  ", slaves: " + str(me['slaves_count']) + ", balance: " + str(me['balance']) + ", profit: " + str(me['slaves_profit_per_min']) + "/per min")
    except Exception as e:
        print(f'Critical Error - {e}')
        input
    try:
        if buy_slave == True:
           randomid = randint(10000, 647000000)
        
        slave = userProfile(randomid)
        schedule.run_pending()
        print('Slave: ' + str(randomid))
        if int(myProfile()['me']['balance']) >= int(slave['fetter_price']):
            if int(slave['fetter_to']) == 0:
                if int(slave['price']) >= min_price:
                    if int(slave['price']) <= max_price:
                        sleep(randint(config["min_delay"],config["max_delay"]))
                        if buy_slave == True:
                            if upgrade_slave == True:
                               if int(me["balance"]) >= 39214:
                                buySlave(randomid)
                                while int(userProfile(randomid)['price']/1.49998088027)  < 26151:
                                      saleSlave(randomid)
                                      sleep(randint(config["min_delay"],config["max_delay"]))
                                      buySlave(randomid)
                                      if int(userProfile(randomid)['price']/1.49998088027) >= 26151:
                                         print(f'Upgrade done. Slave: {randomid}')
                                         if telegram_notifications == True:
                                            requests.get(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_user_id}&text=Upgrade done. Slave: {randomid}")
                               else:
                                buySlave(randomid)
                                sleep(randint(config["min_delay"],config["max_delay"]))
                            else:
                                sleep(randint(config["min_delay"],config["max_delay"]))
                                buySlave(randomid)
                            sleep(randint(config["min_delay"],config["max_delay"]))
                            jobSlave(randomid)
                            if buy_fetter == True:
                                sleep(randint(config["min_delay"],config["max_delay"]))
                                buyFetter(randomid)

    except Exception as inst:
        try:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            inst = None
            del inst