'''
Наш телеграм: @theblacklegion

Автор(re-автор): @vebix

Лицензия: да в рот я ебал ваши лицензии))
'''
import os, sys
import time
import requests
import argparse
import random
import json
from colorama import Fore as F
from headers.agents import Headers
from banner.banner import Banner
class Colors:
    w = F.WHITE
    r = F.RED
    g = F.GREEN
    b = F.BLUE  
class Configuration:
    BLACKNET_ERROR_CODE_STANDARD = -1
    BLACKNET_SUCCESS_CODE_STANDARD = 0
    BLACKNET_MIN_DATA_RETRIEVE_LENGTH = 1
    BLACKNET_RUNNING = False
    BLACKNET_OS_UNIX_LINUX = False
    BLACKNET_OS_WIN32_64 = False
    BLACKNET_OS_DARWIN = False
    BLACKNET_REQUESTS_SUCCESS_CODE = 200
    __blacknet_api__ = "https://darksearch.io/api/search"
class Platform(object):
    def __init__(self, execpltf):
        self.execpltf = execpltf
    def get_operating_system_descriptor(self):
        cfg = Configuration()
        clr = Colors()
        if self.execpltf:
            if sys.platform == "linux" or sys.platform == "linux2":
                cfg.BLACKNET_OS_UNIX_LINUX = True
            if sys.platform == "win64" or sys.platform == "win32":
                cfg.BLACKNET_OS_WIN32_64 = True
            if sys.platform == "darwin":
                cfg.BLACKNET_OS_DARWIN = True
            print(f'OS: {clr.r}{sys.platform}{clr.w}')
                
        else: pass
    def clean_screen(self):
        if self.execpltf:
            if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
                os.system('clear')
            else: os.system('cls')
        else: pass
f = open('saved.txt', 'w')
f.close()
class Blacknet(object):
    def __init__(self, api, query):
        self.api = api
        self.query = query

    def crawl_api(self):
        hdrs = Headers()
        clr = Colors()
        cfg = Configuration()
        try:
            darksearch_url_response = requests.get(self.api, params=self.query)
            json_data = darksearch_url_response.json()
            #json_dump = json.dumps(json_data, indent=2)
            darksearch_url_response.headers["User-Agent"] = random.choice(hdrs.useragent)
        except requests.RequestException as e:
            print(f'{clr.r}{str(e)}{clr.w}')
        try:
            if json_data["total"] >= cfg.BLACKNET_MIN_DATA_RETRIEVE_LENGTH: # data >= 1
                for key in range(0, 18):             
                    site_title = json_data['data'][key]['title']
                    site_onion_link = json_data['data'][key]['link']
                    with open('saved.txt', 'r') as f:                        
                        if not site_title in f.read():
                            print(f'[{clr.r}+{clr.w}] Сайт: {site_title}\n>>> Onion-ссылка: {clr.r}{site_onion_link}{clr.w}')

                            try:
                                with open('saved.txt', 'a') as f:
                                    f.write(f'Site: {site_title}\nOnion-link: {site_onion_link}\n')
                            except Exception as e:
                                print(f'{clr.g}{str(e)}{clr.w}')

                print(f'\n[{clr.r}?{clr.w}] Результаты поиска сохранены в {clr.r}saved.txt{clr.w}.')   
        except IndexError:
            print(f'[{clr.r}-{clr.w}] Нет результатов по: {self.query}\n')
def blacknet_main():
    cfg = Configuration()
    clr = Colors()
    bn = Banner()
    Platform(True).clean_screen()
    Platform(True).get_operating_system_descriptor()
    bn.LoadBlackNetBanner()
    time.sleep(1.5)

    parser = argparse.ArgumentParser()
    parser.add_argument("-q",
                        "--query",
                        help="поиск по ключевому слову/словам",
                        type=str,
                        required=True)
    parser.add_argument("-p",
                        "--page",
                        help="кол-во страниц вывода результатов поиска, дефолт 1",
                        type=int)
    args = parser.parse_args()
    if args.query:
        if args.page: 
            query = {
                    'query': args.query,
                    'page': args.page
                    }
            print(f'Поиск {clr.r}{args.query}{clr.w} на странице {args.page}...\n')
            Blacknet(cfg.__blacknet_api__, query).crawl_api()
            cfg.BLACKNET_RUNNING = True
        else:
            query = {
                'query': args.query,
                'page': 1
                }           
            print(f'Поиск {clr.r}{args.query}{clr.w} на странице: 1...\n')
            Blacknet(cfg.__blacknet_api__, query).crawl_api()
            cfg.BLACKNET_RUNNING = True
if __name__ == "__main__":
    blacknet_main()
    f.close()


