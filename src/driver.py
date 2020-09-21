'''
File is the main driver of the project. Calls relevant methods and logics. 

'''

import argparse
from config import configure
from connect import connect


def testconnection():
    '''
    Checks internet connection and prompts if not connected already.  
    '''
    
    import requests
    Flag = True
    try:
        url = "https://google.com"
        obj = requests.get(url)
    except Exception as e:
        Flag = False
    return Flag
    
def drive(args):

    if testconnection():
        if args.connect:
            connect()
        

    else:
        print("Check your network connection")


def parse_args():

    parser = argparse.ArgumentParser(description='Establishes SSH connection')
    parser.add_argument('-c', '--connect', action='store_true', required=True)
    return parser.parse_args()


if __name__ == "__main__":

    arguments = parse_args()
    drive(arguments)
