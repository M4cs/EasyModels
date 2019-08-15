from easymodels.utils import *
import requests, time
import sys
def start():
    Menu.main()
    
__version__ = "1.3"

if __name__ == "__main__":
    sys.stdout.flush()
    print('Checking For Updates...')
    r = requests.get('https://raw.githubusercontent.com/M4cs/EasyModels/master/version.txt').text.replace('\n', '').replace('\r', '')
    if r != __version__:
        print('Update Available Please Run "pip install easymodules --upgrade" to update to the latest version!')
        time.sleep(1)
    else:
        print('All Up To Date! Starting EasyModels CLI')
    start()