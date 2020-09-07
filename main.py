import argparse
import locale
import logging
from process_text import MainBot

def main():
    logging.basicConfig(filename='logfile.log')
    Processor=MainBot()
    Processor.start()

if __name__ == '__main__':
    main()

