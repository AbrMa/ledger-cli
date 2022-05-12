import argparse
import re

def generate_report(file_name):
    f = open(file_name, 'r')
    reports = {}
    date = ''
    description = ''

    for line in f.readlines():
        line = line.partition(';')[0]

        curr_date = get_str_from_regex(r'\d{4}/\d{1,2}/\d{1,2}', line)
        if curr_date:
            date = curr_date
            description = line.replace(f'{curr_date} ', '').replace('\n','')
            continue

        account = get_str_from_regex(r'[^\d]*(\s\s|\s)', line).replace('\t','')
        money = line.replace(account, '').replace('\n', '').replace('\t', '')

        if account and money:
            reports[(date, description)] = (account, money)

    return reports

def get_str_from_regex(regex, str):
    str_from_regex = re.match(regex, str)
    if str_from_regex:
        return str_from_regex.group() 
    return ''

def print_report(args):
    report = generate_report(args.file)

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