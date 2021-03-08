#!/usr/bin/python3.8
#coded by : zerf-003
#script name : Domains Checker

import os
import requests as rq
import sys
try:
    import colorama
except:
    os.system('pip install colorama')
from colorama import init, Fore


#const
UA = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
CYAN='\033[1;36m'
GREEN="\033[0;32m"
END='\033[0m'
RED="\033[0;31m"
GREY='\033[0;37m'
DGREY='\033[1;30m'

def checker():
    
    get_file = input(RED+'[*]'+ DGREY+'Enter Domains List:'+END)
    file = open(get_file, 'rb')
    file = file.read().splitlines()
    for i in file:
        i = i.decode('utf-8')
        if i.startswith('htt'):
            try:
                req = rq.get(i, verify=True, headers=UA)
                if req.status_code == 200:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive'.format(i))
                    with open('LiveDomain.txt', 'a') as f:
                        f.writelines(i + "\n")
                   
                elif req.status_code== 401 or req.status_code==403:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive \033[1;36m[Detail]\033[0m: \033[0;31mForbidden'.format(i))
                    with open('LiveDomain.txt', 'a') as file:
                        file.writelines(i+'\n')
                
                elif req.status_code==404:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive \033[1;36m[Detail]\033[0m: \033[0;31mResource Not Found On server'.format(i))
                    with open('LiveDomain.txt', 'a') as file:
                        file.writelines(i+'\n')
                
                elif req.status_code==500 or req.status_code==503:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive \033[1;36m[Detail]\033[0m: \033[0;31mInternal Server Error, Temporary Unavailable'.format(i))
                    with open('LiveDomain.txt', 'a') as file:
                        file.writelines(i+'\n')
                      
                else:
                    print(RED+'[-]'+ '\033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[0;31mDead'.format(i))
                
            except rq.exceptions.ChunkedEncodingError:
                pass
            except rq.exceptions.TooManyRedirects:
                pass
            except rq.exceptions.ConnectionError:
                pass
        else:
            i = 'http//:' + i
            try:
                req = rq.get(i, verify=True, headers=UA)
                if req.status_code == 200:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive'.format(i))
                    with open('LiveDomain.txt', 'a') as f:
                        f.writelines(i + "\n")
                   
                elif req.status_code== 401 or req.status_code==403:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive \033[1;36m[Detail]\033[0m: \033[0;31mForbidden'.format(i))
                    with open('LiveDomain.txt', 'a') as file:
                        file.writelines(i+'\n')
                
                elif req.status_code==404:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive \033[1;36m[Detail]\033[0m: \033[0;31mResource Not Found On server'.format(i))
                    with open('LiveDomain.txt', 'a') as file:
                        file.writelines(i+'\n')
                
                elif req.status_code==500 or req.status_code==503:
                    print('\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive \033[1;36m[Detail]\033[0m: \033[0;31mInternal Server Error, Temporary Unavailable'.format(i))
                    with open('LiveDomain.txt', 'a') as file:
                        file.writelines(i+'\n')
                      
                else:
                        print(RED+'[-]'+ '\033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[0;31mDead'.format(i))
                
            except rq.exceptions.ChunkedEncodingError:
                pass
            except rq.exceptions.TooManyRedirects:
                pass
            except rq.exceptions.ConnectionError:
                pass
    
def clear():
    o_s = os.uname()[0]
    if o_s=='Linux':
        os.system('clear')
    elif o_s=="Windows":
        os.system('cls')

my_banner = RED+"""

  / /(_)_   _____     /   \___  _ __ ___   __ _(_)_ __  
 / / | \ \ / / _ \   / /\ / _ \| '_ ` _ \ / _` | | '_ \ 
/ /__| |\ V /  __/  / /_// (_) | | | | | | (_| | | | | |
\____/_| \_/ \___| /___,' \___/|_| |_| |_|\__,_|_|_| |_|
                                                        
   ___ _               _             
  / __\ |__   ___  ___| | _____ _ __ 
 / /  | '_ \ / _ \/ __| |/ / _ \ '__|
/ /___| | | |  __/ (__|   <  __/ |   
\____/|_| |_|\___|\___|_|\_\___|_|   
 
                    \033[0;32m[@]Coded By: \033[0;31mZ3rf-003
                    \033[0;32m[@]Greetz To: \033[0;31mBylka_InJ

"""
clear()
print(my_banner)
checker()