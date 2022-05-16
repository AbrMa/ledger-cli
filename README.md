# ledger-cli

Simple implementation of the ledger-cli.

Ledger is a command-line accounting tool based on the power and completeness of double-entry accounting. It is only a reporting tool, which means it never modifies your data files, but it does offer a large selection of reports, and different ways to customize them to your needs.

## Installation

Clone this repo and move to the script file

```
git clone https://github.com/AbrMa/ledger-cli.git
cd ledger-cli/
```

## usage

```
ledger-cli.py [-h] -f FILE [-s SORT] {print}
```

## optional arguments

+ ```-h, --help```           

show this help message and exit

+ ```-f FILE, --file FILE```  

Read journal data from FILE.

+ ```-s SORT, --sort SORT``` 

Sort postings by evaluating the given value-expression. For example, to search by date one would use: ```ledger-cli.py -f FILE -s date print```

## COMMANDS:

ledger accepts several top-level commands, each of which generates a different kind of basic report.

```{print}``` 

```print``` Print out the full transactions of any matching postings using the same format as they would appear in a data file. This can be used to extract subsets from a ledger file to transfer to other files.