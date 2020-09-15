import argparse
from config import configure
from connect import connect


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