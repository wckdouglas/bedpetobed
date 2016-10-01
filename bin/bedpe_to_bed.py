#!/usr/bin/env python

import sys
from pybedtools import BedTool
from bedpetobed.filter_bed import filterBed, processFile
import argparse

def getopt():
    parser = argparse.ArgumentParser(description='To convert bedpe file to bed file')
    parser.add_argument('-i',default='-',help='Input bedpe file, must have no unmapped bedpe record (default: -)')
    parser.add_argument('-o',default='-',help='Output bed file (default: -)')
    parser.add_argument('--min', default = 10, type=int, help = 'Minimum length of fragment (default = 10)' )
    parser.add_argument('--max', default = 10000, type=int, help = 'Maximum length of fragment (default = 10000)' )
    args = parser.parse_args()
    return args

def main():
    args = getopt()
    bed_file = args.i
    out_file = args.o
    min_length = args.min
    max_length = args.max
    in_handle = bed_file if bed_file != '/dev/stdin' and bed_file != '-' else sys.stdin
    out_handle = open(out_file,'w') if bed_file != '-' and bed_file != '/dev/stdout' else sys.stdout
    bed_iterator = BedTool(in_handle)
    done = processFile(bed_iterator, min_length, max_length, out_handle)


if __name__=='__main__':
    main()
