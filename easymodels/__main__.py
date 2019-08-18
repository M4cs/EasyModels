import requests, time
from easymodels.utils import *
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-gd', '--gui-dark', help='Start with GUI in Dark Mode and Set To Default', action='store_true')
parser.add_argument('-g', '--gui', help='Start with GUI in Light Mode and Set To Default', action='store_true')
args = parser.parse_args()
    

__version__ = "1.5.1"

def create_config():
    with open('config.ini', 'w') as f:
        config = ConfigParser()
        config['DEFAULTS'] = {
            'dark-mode': False
        }
        config.write(f)
        f.close()


def start():
    if args.gui_dark == True:
        dark = True
        args.gui = True
    else:
        dark = False
    sys.stdout.flush()
    print('Checking For Updates...')
    r = requests.get('https://raw.githubusercontent.com/M4cs/EasyModels/master/version.txt').text.replace('\n', '').replace('\r', '')
    print(r)
    if r != __version__:
        print('Update Available Please Run "pip install easymodels --upgrade --no-cache-dir" to update to the latest version!')
        time.sleep(1)
    else:
        print('All Up To Date! Starting EasyModels')
    if args.gui:
        GUI.gui(dark=dark)
    Menu.main()

if __name__ == "__main__":
    start()