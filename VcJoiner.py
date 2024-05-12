import ctypes
import json
import time
import random
import string
import os
import getpass
import sys
import base64
import concurrent.futures
import logging

try:
    import requests
    import colored
    import pystyle
    import datetime
    import keyboard
    import tkinter
    import tls_client
    import threading
    import easygui
    import colorama
    import pynput
    import websocket
    import fake_useragent
    import httpx
    import emoji as emojizer
    import bs4
    import discum
    import discord
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colored')
    os.system('pip install pystyle')
    os.system('pip install datetime')
    os.system('pip install keyboard')
    os.system('pip install tkinter')
    os.system('pip install tls_client')
    os.system('pip install threading')
    os.system('pip install easygui')
    os.system('pip install colorama')
    os.system('pip install pynput')
    os.system('pip install websocket')
    os.system('pip install fake_useragent')
    os.system('pip install httpx')
    os.system('pip install emoji')
    os.system('pip install bs4')
    os.system('pip install discum==1.1.0')
    os.system('pip install discord')

from bs4 import BeautifulSoup
from colorama import Fore, Style
from random import choice
from data.solver import Solver
from data.plugins import *
from websocket import WebSocket
from tls_client import Session
from pystyle import Write, System, Colors, Colorate, Anime
from colored import fg
from json import dumps
from pynput import keyboard as ks
from concurrent.futures import ThreadPoolExecutor
from os.path import isfile, join
from discord.ext import commands

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

owners = "yzl1337"
toolname = "DcAVM TOOLS"
date = datetime.datetime.now()
date_now = date.strftime("%d/%m/%Y")
chrome_version = "116"
xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

with open("config.json") as f:
    data = json.load(f)
    check = data.get("auto_proxy_scraper")
    if check == "y":
        def save_proxies(proxies):
            with open("proxies.txt", "w") as file:
                file.write("\n".join(proxies))

        def get_proxies():
            with open('proxies.txt', 'r', encoding='utf-8') as f:
                proxies = f.read().splitlines()
            if not proxies:
                proxy_log = {}
            else:
                proxy = random.choice(proxies)
                proxy_log = {
                    "http://": f"http://{proxy}", "https://": f"http://{proxy}"
                }
            try:
                url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
                response = httpx.get(url, proxies=proxy_log, timeout=60)

                if response.status_code == 200:
                    proxies = response.text.splitlines()
                    save_proxies(proxies)
                else:
                    time.sleep(1)
                    get_proxies()
            except httpx.ProxyError:
                get_proxies()
            except httpx.ReadError:
                get_proxies()
            except httpx.ConnectTimeout:
                get_proxies()
            except httpx.ReadTimeout:
                get_proxies()
            except httpx.ConnectError:
                get_proxies()
            except httpx.ProtocolError:
                get_proxies()
            
        def check_proxies_file():
            file_path = "proxies.txt"
            if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
                get_proxies()
    
        check_proxies_file()
    else:
        pass

def get_nonce():
    date = datetime.datetime.now()
    unixts = time.mktime(date.timetuple())
    return str((int(unixts)*1000-1420070400000)*4194304)

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def random2(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def get_random_proxy():
    with open("proxies.txt", "r") as f:
        proxies = f.readlines()
    if len(proxies) != 0:
        proxy = random.choice(proxies).strip()
        return proxy
    else:
        return None

session = tls_client.Session(
    client_identifier="chrome_116",
)

proxy_lines = open("proxies.txt", "r").readlines()
proxies = random.choice(proxy_lines).strip() if proxy_lines else None

if proxies and (":" in proxies):
    proxy = "http://" + proxies
else:
    proxy = None

if proxy:
    session.proxies = {
        "http": proxy,
        "https": proxy
    }
else:
    session_class = tls_client.Session
    kwargs = {}

    session = session_class(
        client_identifier="chrome_116",
    )

def dcavm_tool():
    username = getpass.getuser()
    System.Clear()
    tokens = len(open('tokens.txt').readlines())
    ctypes.windll.kernel32.SetConsoleTitleW(f'Made By {owners}  Kullanici :{username} | Tokens : {tokens} | ')
    Write.Print(f"""
\t____   ____   ______      _____   ___   _____  ____  _____  ________  _______     
\t|_  _| |_  _|.' ___  |    |_   _|.'   `.|_   _||_   \|_   _||_   __  ||_   __ \    
\t \ \   / / / .'   \_|      | | /  .-.  \ | |    |   \ | |    | |_ \_|  | |__) |   
\t   \ \ / /  | |         _   | | | |   | | | |    | |\ \| |    |  _| _   |  __ /    
\t    \ ' /   \ `.___.'\ | |__' | \  `-'  /_| |_  _| |_\   |_  _| |__/ | _| |  \ \_  
\t     \_/     `.____ .' `.____.'  `.___.'|_____||_____|\____||________||____| |___| 
                                                                                                        
                                                                                            
                                          Hos Geldin {username} !
------------------------------------------------------------------------------------------------------------
           \t                             (1) VOICE JOINER
           \t                             ($) PREMIUM MENU     
        
""", Colors.green_to_cyan, interval=0.0000)
    Write.Print(f"""------------------------------------------------------------------------------------------------------------""", Colors.green_to_cyan, interval=0.0000)
    Write.Print(f"\nSecim  ~> ", Colors.red_to_blue, interval=0.000); opc = input(magenta).lower()
    if opc=="x" or opc=="exit" or opc=="esc":
        System.Clear()
        bye_bye(username, date_now)
    if opc=="$":
        Write.Print(f"""
[!] Yeterli Uyeliginiz Yok / Her Hangi Bir Sorunda mail atabilirsiniz.

Discord : apolaxtube
Email : apolaxtube905iletisim@gmail.com
""", Colors.purple_to_red, interval=0.000); input()
        dcavm_tool()
    if opc=="+":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By {owners}  Kullanici :{username} |  Update System')
   
    if opc=="!":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By {owners}  Kullanici :{username} |  Send Suggestion')
        open('data\send_suggest.py')
        os.system("data\send_suggest.py")
        dcavm_tool()
    if opc=="1":
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By {owners}  Kullanici :{username} |  Voice Joiner')
        Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
        Write.Print(f"channel_id ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        Write.Print(f"Defean? y/n ~> ", Colors.purple_to_red, interval=0.000); defean = input().lower()
        Write.Print(f"Mute? y/n ~> ", Colors.purple_to_red, interval=0.000); mute = input().lower()
        Write.Print(f"Stream? y/n ~> ", Colors.purple_to_red, interval=0.000); stream = input().lower()
        Write.Print(f"Video? y/n ~> ", Colors.purple_to_red, interval=0.000); video = input().lower()

        output_lock = threading.Lock()
        defean_voice = False
        mute_voice = False
        stream_voice = False
        video_voice = False
        if defean == "y":
            defean_voice = True
        if mute == "y":
            mute_voice = True
        if stream == "y":
            stream_voice = True
        if video == "y":
            video_voice = True
        print()
        def voice_joiner(token):
            while True:
                ws_voice = WebSocket()
                ws_voice.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                ws_voice.send(dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": "windows",
                                "$browser": "Discord",
                                "$device": "desktop"
                            }
                        }
                    }))
                ws_voice.send(dumps({
                    "op": 4,
                    "d": {
                        "guild_id": server_id,
                        "channel_id": channel_id,
                        "self_mute": mute_voice,
                        "self_deaf": defean_voice, 
                        "self_stream?": stream_voice, 
                        "self_video": video_voice
                    }
                }))
                ws_voice.send(dumps({
                    "op": 18,
                    "d": {
                        "type": "guild",
                        "guild_id": server_id,
                        "channel_id": channel_id,
                        "preferred_region": "spain"
                    }
                }))
                ws_voice.send(dumps({
                    "op": 1,
                    "d": None
                }))

        def process_token(token):
            voice_joiner(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()
                for token in tokens:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Joined Voice {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        dcavm_tool()
dcavm_tool()
