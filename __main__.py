import logging
import time
import argparse
import keyring
from tadoHelper import TadoHelper

logging.basicConfig(filename='log/tado.log', format='%(asctime)s - %(message)s', level=logging.INFO)
_LOG_ = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Tado Assistant")
    parser.add_argument("-c", "--configure", action="store_true", help="Configure account settings")
    parser.add_argument("--email", help="Tado user id", default="user_id")
    parser.add_argument("--pwd", help="Tado password", default="password")
    args = parser.parse_args()

    if args.configure:
        keyring.set_password('tado.com', args.email, args.pwd)
        print('Account settings configure')
        return

    my_tado = TadoHelper(args.email, keyring.get_password('tado.com', args.email))

    while True:
        wait_time = 60

        try:
            my_tado.checkWindowState()
        except Exception as err:
            logging.warning(repr(err))

        _LOG_.info(f'Idle for {wait_time} seconds')
        time.sleep(wait_time)


main()
