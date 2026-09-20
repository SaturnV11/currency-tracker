import argparse

parser = argparse.ArgumentParser(description= "Check historical quotation of coins and plots its chart")

parser.add_argument("-b", "--base", 
    metavar="CURRENCY", help="Base currency code (e.g. USD)"
)
parser.add_argument("-q", "--quote", 
    metavar="CURRENCY", help="Quote currency code (e.g. BRL)"
)
parser.add_argument("-s", "--start", 
    metavar="DATE", help="Start date in YYYY-MM-DD format"
)
parser.add_argument("-e", "--end", 
    metavar="DATE", help="End date in YYYY-MM-DD format"
)

def parse_arguments():
    return parser.parse_args()