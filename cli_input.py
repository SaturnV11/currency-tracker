from datetime import datetime as dt

def get_date_range(start_date=None, end_date=None):
    # Validate or prompt for each date if not givven through argparse
    start_date = get_date(request="Start", date=start_date)
    end_date = get_date(request="End", date=end_date)

    # Ensures the start date does not come after the end date
    while start_date > end_date:            
        print("<Error>: Start date cannot be later than end date.")
        end_date = get_date(request="End")

    return start_date, end_date


# Base: currency being exchanged
# Quote: currency being received
def get_currency(base=None, quote=None):
    # Prompts for any code not provided through the cmd line (argparse)
    if base is None:
        base = get_currency_code(request="exchange")

    if quote is None:
        quote = get_currency_code(request="receive")

    # Ensures both codes are different
    while quote == base:
        print("<Error>: Currency parameters need to be different.")
        quote = get_currency_code(request="receive")

    return base, quote


########## AUXILIARY METHODS ##########:


def get_date(request: str, date=None):
    while True:
        try:
            if date is None:
                date = input(f"{request} date (YYYY-MM-DD): ")
            date = dt.strptime(date, "%Y-%m-%d")
            return date.strftime("%Y-%m-%d") # return the YY-MM-DD format without hh:mm (time)

        except ValueError:
            print("<Error>: Invalid date. Use YYYY-MM-DD.\n")
            date = None


def get_currency_code(request: str):
    while True:
        currency = input(f"Currency to {request}: ").upper()

        # I'd rather keep get_currency_code() limited to validating the syntax and let the API determine whether 'XYZ' is a supported currency
        if len(currency) == 3 and currency.isalpha():
            return currency

        print(f"Error: currency must be a 3-letter code\n")
        # USD   → valid
        # BRL   → valid
        # XYZ   → valid (API decides whether its valid or not)
        # AB    → invalid
        # USDD  → invalid
        # 123   → invalid
        # U$D   → invalid