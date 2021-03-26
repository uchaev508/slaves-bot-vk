import requests, json, schedule, threading, random, time
print('Enter your authorization: ')
authorization = str(input()).rstrip().lstrip()

anticooldown = random.randint(0, 0) # Анти кд, настраивать можете сами.
job_name = 'Вьетнам' # Имя работы

min_price = 40 # Минимальная цена
max_price = 1000000 # Максимальная цена

buy_slave = True # Покупать рабов?
buy_fetter = True # Покупать оковы? 

print(f'Job name: {job_name}')
print(f'Min price: {min_price}, max price: {max_price}')
print(f'Buy slave: {buy_slave}')
print(f'Buy fetter: {buy_fetter}')

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
     'name':job_name})
    headers = {'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
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
     'authorization':authorization, 
     'sec-ch-ua-mobile':'?0', 
     'content-type':'application/json',
     'origin':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com',
     'referer':'https://prod-app7794757-29d7bd3253fe.pages-ac.vk-apps.com/',
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.request('POST', url, headers=headers, data=payload)
    return response.json()

def findSlave(slaves):
    for slave in slaves:
        schedule.run_pending()
        print('Slave:', str(slave['id']))
        if int(slave['profit_per_min']) * 60 * int(slave['fetter_hour']) > int(slave['fetter_price']):
            if int(myProfile()['me']['balance']) >= int(slave['fetter_price']):
                if int(slave['fetter_to']) == 0:
                    if int(slave['price']) >= min_price:
                        if int(slave['price']) <= max_price:
                            time.sleep(anticooldown)
                            if buy_slave == True:
                               slaveid = str(slave['id']).replace('-','')
                               print(f'Buy: ' + slaveid)
                               buySlave(int(slaveid))
                               time.sleep(anticooldown)
                               jobSlave(int(slaveid))
                               if buy_fetter == True:
                                  time.sleep(anticooldown)
                                  print('Buy fetter: ' + slaveid)
                                  buyFetter(int(slaveid))
        if int(slave['slaves_count']) != 0:
            print('findSlave -> ' + int(slaveid))
            findSlave(slave['slaves'])

def Profile():
    print('Profile')
    me = myProfile()['me']
    if me['fetter_to'] != 0:
        if me['price'] <= me['balance']:
            if buy_slave == True:
               buySlave(me['id'])
    me = myProfile()['me']
    slaves = myProfile()['slaves']
    for slave in slaves:
        slaveid = str(slave['id']).replace('-','')
        print('Profile -> ' + str(slave['id']))
        if slave['job']['name'] != job_name:
            time.sleep(anticooldown)
            jobSlave(int(slaveid))
        if slave['profit_per_min'] * 60 * slave['fetter_hour'] > slave['fetter_price'] and me['balance'] >= slave['fetter_price'] and slave['fetter_to'] == 0:
            if buy_fetter == True:
                           time.sleep(anticooldown)
                           buyFetter(int(slaveid))

def ThreadProfile():
    my_thread = threading.Thread(target=Profile)
    my_thread.start()

me = myProfile()['me']
print('Your ID:', str(me['id']), 'Slaves:', str(me['slaves_count']), 'Profit:', str(me['slaves_profit_per_min']))
schedule.every(2).minutes.do(ThreadProfile)

while True:
    try:
        tops = list(topUsers()['list'])
        tops.reverse()
        for top in tops:
            print(top)
            findSlave(slaveList(int(top['id'])))

    except Exception as inst:
        try:
            print(type(inst))
            print(inst.args)
            print(inst)
        finally:
            inst = None
            del inst