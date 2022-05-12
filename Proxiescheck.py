#HTTP CHECKER 
#Code By Success
#ping proxy = ms

import colorama
import requests
import time
import threading
import os
from threading import Thread
from colorama import Fore

pingproxy = int("5000")
timeout = float(pingproxy/1000)
proxy = open("socks4.txt", "r").read().splitlines()
os.system("cls")
print(f"HTTP CHECKER CODE BY SUCCESS{Fore.RESET}")
print("PROXIES COUNT >> %d" %len(proxy) + "\n")
input("Enter to start")
def check(proxy , times):
    try:
        start = time.time()
        r = requests.get("http://www.google.com/",proxies={"http" : f"http://{proxy}"},timeout=(times))
    except:
        print(f"{Fore.LIGHTRED_EX}HTTP Dead > {proxy}{Fore.RESET}")
    else:
        end = time.time()
        if r.status_code == 200:
            ping = end - start
            s = ping * 1000
            if s <= timeout*1000:
                outfile = open(f'HTTP.txt', 'a')
                print(f"{Fore.LIGHTGREEN_EX}{proxy} {Fore.RESET}| {Fore.LIGHTGREEN_EX}{round(s)}ms {Fore.RESET}| {Fore.LIGHTGREEN_EX}HTTP{Fore.RESET}")
                outfile.write(proxy + '\n')
                outfile.close
            else:
                print(f"{Fore.LIGHTGREEN_EX}{proxy} {Fore.RESET}| {Fore.LIGHTGREEN_EX}{round(ping)}ms {Fore.RESET}| {Fore.LIGHTGREEN_EX}HTTP{Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}HTTP Working > {proxy}   {round(s)}ms{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTRED_EX}HTTP Dead > {proxy}{Fore.RESET}")

for i in proxy:
    threading.Thread(target=check,args=(i, timeout)).start()