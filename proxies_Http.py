import requests
from colorama import Fore, init
init(convert=True)
textcol = f"{Fore.BLACK}"

print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.GREEN}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Scaning....")
f = open("./socks5.txt",'wb')
try:
 r = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
 f.write(r.content)
except:
 pass
try:
 r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all")
 f.write(r.content)
except:
 f.close()
try:#credit to All3xJ
 r = requests.get("https://www.socks-proxy.net/")
 part = str(r.content)
 part = part.split("<tbody>")
 part = part[1].split("</tbody>")
 part = part[0].split("<tr><td>")
 proxies = ""
 for proxy in part:
  proxy = proxy.split("</td><td>")
  try:
   proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
  except:
   pass
 out_file = open("./http.txt","a")
 out_file.write(proxies)
 out_file.close()
except:
 pass
print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.GREEN}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Proxy List Downloaded as http.txt")
#ndbiaw end
input("Press Anykey to exit...")
exit()