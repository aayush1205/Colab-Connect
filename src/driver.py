import argparse
from config import configure
from connect import connect
'''
opening a ssh tunnel for 
futher communications

'''
def testconnection():
    import requests
    Flag = True
    try:
        url = "https://google.com"
        obj = requests.get(url)
    except Exception as e:
        Flag = False
    return Flag
    
def drive(args):

    if args.connect:
        connect()


def parse_args():

    parser = argparse.ArgumentParser(description='Establishes SSH connection')
    parser.add_argument('-c', '--connect', action='store_true', required=True)
    return parser.parse_args()


if __name__ == "__main__":

    arguments = parse_args()
    drive(arguments)