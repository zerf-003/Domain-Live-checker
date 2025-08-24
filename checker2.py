import os,sys
import time
import requests as req



def checkDomain(domain):
    domain =domain.decode("utf-8")
    if domain.startswith("http"):
        return domain
    else:
        domain = "http://"  + domain
        return domain  


def testDomain(domain):
    try:
        rq  = req.get(domain, verify=True)
        if  rq.status_code == 200:
            print("\033[0;32m[+] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[1;33mLive.".format(domain))
        else:
            print("\033[0;31m[-] \033[1;36m[Domain]\033[0m: {} \033[1;36m[Result]\033[0m: \033[0;31mDead.".format(domain))
    except rq.ConnectionError:
        pass
    except rq.ChunkedEncodingError:
        pass
    except rq.TooManyRedirects:
            pass

def openDomainsFile(file):
    try:
        with open(file, "rb") as DomainFile:
            Domain = DomainFile.read().decode().splitlines()
            
            return Domain
    except FileNotFoundError:
        print("\033[0;31m[-] \033[1;36m[Error]\033[0m: File Not Found.")
        sys.exit()

def main():
    DomainsFile = input("\033[0;36m[?] \033[1;36m[Input]\033[0m: Enter Your Domains File: ")
    Domains = openDomainsFile(DomainsFile)
    for domain in Domains:
        check = checkDomain(domain)
        testDomain(check)

if __name__ == "__main__": 
    os.system("cls" if os.name == "nt" else "clear")
    main()