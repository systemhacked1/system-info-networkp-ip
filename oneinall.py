
from geoip import geolite2
from socket import *
from googlesearch import *
from hashlib import * 
import pyfiglet
from termcolor import colored
import os
from time import sleep 
screen=pyfiglet.figlet_format('No System Is Safe ')
print('''
            Follow Me in Telegram https://t.me/System_Hac
         **************************************************  
    ''')
print(screen)
print('\033[34m','''
    [1] Locate IP

    [2] Get Dns From IP

    [3] Get IP from Dns

    [4] Get Port From Number

    [5] Search in Dorks about Sqli

    [6] hash 

    ''')

user=input(' Choice Number > ')
def locate():
    if user =="1":
        
        os.system('clear')
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(2)
            
        user1=input("Enter a {Victim IP}  > ")
        ip=geolite2.lookup(user1)
        print(ip)
locate()

def dns():
    if user=="2":
        os.system('clear')
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(1)
        sleep(2)
            
        for i in user:    
            user2=input("Enter a {IP} > ")
            get=gethostbyaddr(user2)
            print(get)
            print(i)
                
dns()

def IP():
    if user =="3":
        
        os.system('clear')
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(1)
        sleep(2)
            
        user3=input("Enter a {DNS} > ")
        GETIP=gethostbyname(user3)
        print(GETIP)
IP()

def port():
    if user =="4":
            os.system('clear')
            print('\033[31m','Loading ... ')
            sleep(1)
            print('\033[31m','Loading ... ')
            sleep(1)
            print('\033[31m','Loading ... ')
            sleep(2)
            user4=input("Enter a Number > ")
            port_num=getservbyport(int(user4))
            print(port_num)
port()


def sqli():
    if user =="5":
        os.system('clear')
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
        sleep(1)
        print('\033[31m','Loading ... ')
            
        sleep(2)
        for i in search("php?id="):
            print('>>>>>>>',i)

sqli()


def hashm():
    if user =="6":
        
        os.system('clear')
            
        user6=input(" Enter a Text :> " )
        sleep(1)
        print('\033[31m','Now You see Encryption ! ')
        sleep(1)
        print('\033[36m','Choose ($!$)')
        sleep(2)
        print('''

    [1] md5

    [2] sha1

    [3] sha224

    [4] sha256

    [5] sha384

    [6] sha512

    [7] blake2b

    [8] blake2s



    ''')
        user9=input(" Choose any Encryption type : ")
        

        if user9 =="1":
    
            
            MD5=md5(user6.encode()).hexdigest()
            print(MD5)
        if user9 =="2":
            SHa1=sha1(user6.encode()).hexdigest()
            print(SHa1)
        if user9=="3":
            SHA224=sha224(user6.encode()).hexdigest()
            print(SHA224)
        if user9=="4":
            SHA256=sha256(user6.encode()).hexdigest()
            print(SHA256)
        if user9=="5":
            SHA384=sha384(user6.encode()).hexdigest()
            print(SHA384)
        if user9=="6":

            SHA512=sha512(user6.encode()).hexdigest()
            print(SHA512)
        if user9=="7":
            bLAKE2b=blake2b(user6.encode()).hexdigest()
            print(bLAKE2b)
        if user9=="8":
            
            BLAKE2s=blake2s(user6.encode()).hexdigest()
            print(BLAKE2s)
hashm()
         
                
           
          
       



           
              
            
          
    
        
      
            
           
