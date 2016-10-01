#!/usr/bin/env python

import sys
from pybedtools import BedTool
from bedpetobed.filter_bed import filterBed, processFile
import argparse

def getopt():
    parser = argparse.ArgumentParser(description='convert bedpe file to bed file')
    parser.add_argument('-i',required=True,help='Input bed file, must have no unmapped bedpe record')
    parser.add_argument('--min', default = 10, type=int, help = 'Minimum length of fragment' )
    parser.add_argument('--max', default = 10000, type=int, help = 'Maximum length of fragment' )
    args = parser.parse_args()
    return args

def main():
    args = getopt()
    bed_file = args.i
    min_length = args.min
    max_length = args.max
    handle = bed_file if bed_file != '/dev/stdin' and bed_file != '-' else sys.stdin
    bed_iterator = BedTool(handle)
    done = processFile(bed_iterator, min_length, max_length)


if __name__=='__main__':
    main()
