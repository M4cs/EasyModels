import requests, time
from easymodels.utils import *
import sys

__version__ = "1.3.1"

def start():
    sys.stdout.flush()
    print('Checking For Updates...')
    r = requests.get('https://raw.githubusercontent.com/M4cs/EasyModels/master/version.txt').text.replace('\n', '').replace('\r', '')
    if r != __version__:
        print('Update Available Please Run "pip install easymodules --upgrade --no-cache-dir" to update to the latest version!')
        time.sleep(1)
    else:
        print('All Up To Date! Starting EasyModels CLI')
    Menu.main()

if __name__ == "__main__":
    start()