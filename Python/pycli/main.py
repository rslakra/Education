#
# Author: Rohtash Lakra
#
import sys

from core.time import convert_utc_to_pst


def main():
    # args = sys.argv
    # exclude the 'pycli' command
    args = sys.argv[1:]
    # print('args => {}'.format(len(args)))
    # for arg in args:
    #     print('arg={}'.format(arg))

    # print()
    # print('{} = {}'.format(args[0], args[1]))
    # print()
    if len(sys.argv) > 1:
        match args[0]:
            case '-utp':
                print()
                utc_time = args[1]
                print(f"utc_time={utc_time}, utc_to_pst={convert_utc_to_pst(utc_time)}")
                print()
            case _:
                print()
                print('pycli --help')
                print("pycli -utp '2024-11-09 03:24:34'")
                print()
    else:
        print('pycli --help')


if __name__ == '__main__':
    main()
