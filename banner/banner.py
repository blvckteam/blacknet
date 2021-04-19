class Banner(object):
    def LoadBlackNetBanner(self):
        from colorama import Fore as F, Back as B
        import sys
        try:
            print(f'{F.RED}    ____  __    ___   ________ __{F.WHITE} _   ______________')
            print(f'{F.RED}   / __ )/ /   /   | / ____/ //_/{F.WHITE}/ | / / ____/_  __/')
            print(f'{F.RED}  / __  / /   / /| |/ /   / ,< {F.WHITE} /  |/ / __/   / /   ')
            print(f'{F.RED} / /_/ / /___/ ___ / /___/ /| |{F.WHITE}/ /|  / /___  / /    ')
            print(f'{F.RED}/_____/_____/_/  |_\____/_/ |_/{F.WHITE}_/ |_/_____/ /_/  {B.RED}1.2{B.RESET}')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print(f'OS: {F.RED}{sys.platform}{F.WHITE}                         by {F.RED}@theblacklegion{F.WHITE}')
            print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print('')

        except ImportError as ie:
            print(banner)