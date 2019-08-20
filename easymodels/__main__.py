import requests, time
from easymodels.utils import *
import argparse
import sys
import os
from crayons import *
    

__version__ = "1.6"

def create_config():
    with open('config.ini', 'w') as f:
        config = ConfigParser()
        config['DEFAULTS'] = {
            'dark-mode': False
        }
        config.write(f)
        f.close()


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gd', '--gui-dark', help='Start with GUI in Dark Mode and Set To Default', action='store_true')
    parser.add_argument('-g', '--gui', help='Start with GUI in Light Mode and Set To Default', action='store_true')
    parser.add_argument('-d', '--disable-update', help='Start without checking for updates.', action='store_true')
    args = parser.parse_args()
    try:
        if args.gui_dark == True:
            dark = True
            args.gui = True
        else:
            dark = False
        sys.stdout.flush()
        if args.disable_update == False:
            print(yellow('Checking For Updates...', bold=True))
            r = requests.get('https://raw.githubusercontent.com/M4cs/EasyModels/master/version.txt').text.replace('\n', '').replace('\r', '')
            if r != __version__:
                print(green('Update Available Please Run "pip install easymodels --upgrade --no-cache-dir" to update to the latest version!', bold=True))
                time.sleep(1)
            else:
                print(green('All Up To Date! Starting EasyModels', bold=True))
        if args.gui:
            GUI.gui(dark=dark)
        print(green('Starting EasyModels...', bold=True))
        Menu.main()
    except KeyboardInterrupt:
        print(red('Exiting...', bold=True))

if __name__ == "__main__":
    start()