import argparse

def read_file(file):
    pass

def print_report(args):
    f = open(args.file, "r")
    print(f.read())

def main():
    parser = argparse.ArgumentParser(description='ledger is a command-line accounting tool based on the power and completeness of double-entry accounting.  It is only a reporting tool, which means it never modifies your data files, but it does offer a large selection of reports, and different ways to customize them to your needs.')
    subparsers = parser.add_subparsers(title='COMMANDS', description='ledger accepts several top-level commands, each of which generates a different kind of basic report.')

    parser.add_argument('-f', '--file', help='Read journal data from FILE.', required=True)

    parser_print = subparsers.add_parser('print', help='Print out the full transactions of any matching postings using the same format as they would appear in a data file.  This can be used to extract subsets from a ledger file to transfer to other files.')
    parser_print.set_defaults(func=print_report)

    args = parser.parse_args()

    if 'func' in args:
        args.func(args)
    else:
        parser.print_usage()

if __name__ ==  '__main__':
    main()