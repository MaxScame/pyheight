import argparse
import logging

import pyheight.cli
import pyheight.web


if __name__ == "__main__":
    logging.basicConfig(filename='app.log',
                        filemode='w',
                        level=logging.DEBUG,
                        format='[%(levelname)s] %(asctime)s - %(message)s',
                        datefmt='%d-%m-%YT%H:%M:%SZ%z')

    parser = argparse.ArgumentParser(description="PyHeight")

    parser.add_argument("-m",
                        dest="mode",
                        default='web',
                        type=str,
                        help='web/cli')

    args = parser.parse_args()

    # Maybe can use match-case later
    if args.mode == 'web':
        logging.info('Web mode')
        pyheight.web.run()
    elif args.mode == 'cli':
        logging.info('CLI mode')
        pyheight.cli.run()
    else:
        logging.warning('Invalid mode')
