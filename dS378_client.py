#!/usr/bin/env python3
'''dS378 client'''
import sys

from ocs.matched_client import MatchedClient
from dS378 import RelayStatus

def usage():
    print('usage: dS378_client.py op_type [ch_num] [on_off]', file=sys.stderr)

def main():
    '''dS378 client'''
    ds_client = MatchedClient('dS378', args=[])

    op_type = sys.argv[1]

    if op_type == 'get':
        _, _, session = ds_client.get_relays()
        for key, val in session['data']:
            print(key, val)
    elif op_type == 'set':
        relay_num = int(sys.argv[2])
        on_off = sys.argv[3]

        if on_off in ['on', '1']:
            on_off = RelayStatus.on
        elif on_off in ['off', '0']:
            on_off = RelayStatus.off
        else:
            usage()
            sys.exit(1)

        ds_client.set_relay(relay_num=relay_num, on_off=on_off)
    else:
        usage()


if __name__ == '__main__':
    main()
