#!/usr/bin/env python
import argparse
from delimiter_converter import converter
import os

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", default=False, help="Converts the list to JSON.")
    parser.add_argument("--yml", action="store_true", default=False, help="Converts the list to YAML.")
    parser.add_argument("--sql", action="store_true", default=False, help="Converts the list to SQL Schema.")
    parser.add_argument("-p", action="store_true", default=False, help="Accepts the first line of the file as column names.")
    parser.add_argument("-f", required=True, default=False, help="File input.", type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()
    converter.Converter(args=vars(args))

