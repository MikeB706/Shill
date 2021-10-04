# coding=utf8
import sys 
from telethon import TelegramClient
import time
import datetime
starttime =time.time()

# Use your own values from my.telegram.org
api_id = 8556459
api_hash = 'ac3382d514647ccfe2c6bf7d94e1370f'

groups = ['AlldayEveryDay11,OutlawsBSCGems']

#groups =['']

failcount = 0;

# The first parameter is the .session file name (absolute path allowed)
while True:
    with TelegramClient('anon', api_id, api_hash) as client:
        for x in groups:
            try:
                client.loop.run_until_complete(client.send_message(x, "hey peeps!"))
            except: 
                print(x, sys.exc_info()[0])
                failcount += 1
    print(datetime.datetime.now(), str(failcount/len() * 100) + '%')
    time.sleep(100 -((time.time() - starttime) % 100))
