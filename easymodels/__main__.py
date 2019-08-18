import requests, time
from easymodels.utils import *
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-g', '--gui', help='Start with GUI rather than CLI', action='store_true')
args = parser.parse_args()
    

__version__ = "1.4.4"

def start():
    sys.stdout.flush()
    print('Checking For Updates...')
    r = requests.get('https://raw.githubusercontent.com/M4cs/EasyModels/master/version.txt').text.replace('\n', '').replace('\r', '')
    print(r)
    if r != __version__:
        print('Update Available Please Run "pip install easymodels --upgrade --no-cache-dir" to update to the latest version!')
        time.sleep(1)
    else:
        print('All Up To Date! Starting EasyModels CLI')
    if args.gui:
        GUI.gui()
    Menu.main()

if __name__ == "__main__":
    start()