import argparse
import re
from curses.ascii import isdigit
from collections import defaultdict

class Currency:
    def __init__(self, amount = 0, type = '$', visible = True):
        self.amount = amount
        self.type = type
        self.visible = visible
    
    def __repr__(self):
        return f'{self.type} {self.amount} {self.visible}'


def get_data(lines):
    data = defaultdict(list)
    date = ''
    description = ''
    sum_money = 0

    for line in lines:
        line = line.partition(';')[0]

        current_date = get_str_from_regex(r'\d{4}/\d{1,2}/\d{1,2}', line)
        if current_date:
            date = current_date
            description = line.replace(f'{current_date} ', '').replace('\n','')
            sum_money = 0
            continue

        account = get_str_from_regex(r'[^\d]*(\s\s|\s)', line).replace('\t','').replace('\n', '')
        money = line.replace(account, '').replace('\n', '').replace('\t', '')

        if account and money:
            money = get_money(money)
            sum_money += money
            data[(date, description)].append((account, Currency(money)))
        elif account:
            data[(date, description)].append((account, Currency(sum_money * -1, '$', visible=False)))
            

    return data


def get_money(str):
    money = ''
    for c in str:
        if isdigit(c) or c == '.':
            money += c

    if '-' in str:
        return float(money) * -1
    return float(money)

def get_str_from_regex(regex, str):
    str_from_regex = re.match(regex, str)
    if str_from_regex:
        return str_from_regex.group() 
    return ''

def read_file(file_path):
    f = open(file_path, 'r')
    return f.readlines()

def print_report(args):
    lines = read_file(args.file)
    report = get_data(lines)
    
    for key, value in report.items():
        date, description = key
        print(f'{date} {description}')

        for account, currency in value:
            if currency.visible:
                print(f'\t{account}\t\t{currency.type}{currency.amount}')
            else:
                print(f'\t{account}')

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