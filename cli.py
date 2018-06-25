#! /usr/bin/env python
import argparse

def run(args):
    filename = args.input # these match the "dest": dest="input"
    num_products = args.n #match "dest": dest="n"
    output_filename = args.output # from dest="output"

    # Do stuff
    for line in open(filename):
        print(line,end='')


def main():
    parser=argparse.ArgumentParser(description="detects top sellers, provided customer receipts files")
    parser.add_argument("-d",help="String filepath (absolute or relative) to the directory of receipt files" ,dest="input", type=str, required=True)
    parser.add_argument("-n",help="Integer number of best-selling products to return" ,dest="n", type=str, required=True)
    parser.add_argument("-o",help="String filepath (absolute or relative) to the output file" ,dest="output", type=str, required=True)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
    main()