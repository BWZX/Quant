#!/usr/bin/python
# -*- coding: utf-8 -*-

from time_series.crawl_data import config
# import config
import json
import urllib, urllib.request


def insertList(data): 
    printmsg=data[1]
    printmsg='code={code}, period={period}, price={price}'.format(code=printmsg['tags'].get('code'),period=printmsg['tags'].get('period'),price=printmsg['tags'].get('price'))
    if not data:   
        return
    url='http://10.8.0.5:4242/api/put'   

    request=urllib.request.Request(url) 
    index=0
    length=len(data)
    loop=True
    while loop:
        if length>index+30:
            tempdt = json.dumps(data[index:index+30])  
            tempdt=bytes(tempdt,'utf8') 
            result=urllib.request.urlopen(request, tempdt)
        else:
            tempdt = json.dumps(data[index:])
            # print(tempdt)  
            tempdt=bytes(tempdt,'utf8') 
            # print(tempdt)
            result=urllib.request.urlopen(request, tempdt)
            loop=False
        
        feedback=str(result.getcode())
        
        if feedback == '204' or '200':
            index=index+30
            print(feedback+' '+printmsg) 
    pass    

def getPriceData(code, period, price):    
    url='http://10.8.0.5:4242/api/query?start=1980/01/01-00:00:00&m=none:security.price%7Bperiod={period},code={code},price={price}%7D'.format(period=period, code=code, price=price)    
    print(url)
    request=urllib.request.Request(url)  
    result=urllib.request.urlopen(request, timeout=25)
    if result.code == 200 or 204:
        jstr=str(result.read(),encoding='utf-8')
        result=json.loads(jstr)
        return result[0]['dps']
    else:
        print('\n数据还未保存！！\n')
    #print(data)
    pass

def getVolumeData(code, period):    
    url='http://10.8.0.5:4242/api/query?start=1980/01/01-00:00:00&m=none:security.volume%7Bperiod={period},code={code}%7D'.format(period=period, code=code)    
    request=urllib.request.Request(url)  
    result=urllib.request.urlopen(request)
    if result.code == 200 or 204:
        jstr=str(result.read(),encoding='utf-8')
        result=json.loads(jstr)
        return result[0]['dps'] 
    #print(data)
    pass


'''
async def fetchData(url):
    conn = aiohttp.TCPConnector(limit=config.REQ_AMOUNTS)    
    s = aiohttp.ClientSession(headers = config.HEADERS, connector=conn)
    
    dat = {
        "metric": "test.t1",
        "timestamp": 1346846405,
        "value": 34,
        "tags": {
           "host": "web01",
           "dc": "lgs"
        }
    }

    # print(da.value)
    async with s.post(url, data=json.dumps(dat)) as r:    
        txt = await r.text(encoding='utf-8')
        print(r.status)
        print(txt)
        # await callback(data, s)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url='http://10.8.0.5:4242/api/put'
    #coroutine in tasks will run 
    tasks = [fetchData(url)]  
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close() 
'''
