#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date


expirydate = datetime.date(2021, 9, 24)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(20)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    clear()
    y=1
    newperiod=period
    banner='figlet RXCEV5.0|lolcat'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print(f"{red}Contact me on telegram @RXCE_LOVER")
        print(f"{yellow}Enter ",newperiod," Parity Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        #samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
          
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @RXCE_LOVER")
            #print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=16, minute=25, second=0, microsecond=0)
    Secondend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>Third and now<Thirdend):
            period=320
            hero()
    elif(now):
            period=340
            hero()
    elif(False):
            period=340
            hero()
    elif(False):
            period=360
            hero()
    else:
        banner='figlet RXCEV5.0'
        system(banner)
        #print(f"{red}"Hi!! Thanks for buying the hack")
        print("Hi! thanks for trying our DEMO")
        print("----------Your play time-----------")
        #print("31st Aug 2021, 11:00 AM- 11:30 AM")
        #print("31st Aug 2021, 02:00 PM- 02:30 PM")
        print("23rd Sept 2021, 04:00 PM- 04:30 PM")
        #print("31st Aug 2021, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @RXCE_LOVER ")



else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    banner='figlet RXCEV5.0|lolcat'
    rava=0
    now = datetime.datetime.now()
    Second = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=55, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=30, second=0, microsecond=0)
    Thirdend = now.replace(hour=18, minute=34, second=0, microsecond=0)
    Final = now.replace(hour=18, minute=35, second=0, microsecond=0)
    Finalend = now.replace(hour=22, minute=35, second=0, microsecond=0)

    if(now>Second and now<Secondend):
            rava=292
    elif(now>Third and now<Thirdend):
            rava=352
    elif(now>Final and now<Finalend):
            rava=412
    system(banner)
    print(f"{neon}*--------*--------*-------*---------*---------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@RXCE_LOVER for activating")
    print("     Plan Amount --    Total limit " )
    print(" 1.  1000 INR -------  1 Day (30 Games")
    print(" 2.  2500 INR -------  3 Days(90 Games")
    print(" 2.  5000 INR ------- 7 Days(210 Games")
    print("*---------*----------*-------------*----------*")
    print("If you need any discount contact me")
    print("Beware of fraudsters!!!")
    while(True):
        print("My banking name is ............")
        print(f"{red}After You Pay to The UPI ID above You Can Automatically")
        print(f"Activate Hack By Entering The Correct ")
        print(f"{green}(UTR) Or Upi Reference Number") 
        print(f"{neon}To Activate The Hack")
        print(f"If It Does'nt Open Contact Me On Telegram {yellow}@RXCE_LOVER")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{red}*---------*----------*-------------*----------*")
        print("payhere--- UPI : ")
        print(f"{yellow}UPI1 : fixxer786@okaxis")
        print("UPI2 : fixxer786@okaxis")
        print("If you have already paid to above UPI")
        print(f"{neon}Enter Your Activation Code Or Upi Reference for Opening Hack")
        bhai=input(": ")