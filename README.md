# ledger-cli

Simple implementation of the ledger-cli.

Ledger is a command-line accounting tool based on the power and completeness of double-entry accounting. It is only a reporting tool, which means it never modifies your data files, but it does offer a large selection of reports, and different ways to customize them to your needs.

## usage

```ledger-cli.py [-h] -f FILE {print}```

## optional arguments

```-h, --help```           show this help message and exit

```-f FILE, --file FIL```  Read journal data from FILE.

## COMMANDS:

ledger accepts several top-level commands, each of which generates a different kind of basic report.

```{print}``` 

```print``` Print out the full transactions of any matching postings using the same format as they would appear in a data file. This can be used to extract subsets from a ledger file to transfer to other files.