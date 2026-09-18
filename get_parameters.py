from datetime import datetime as dt

def get_date_range():
    start_date = get_date(request="Start")
    while True:            
        end_date = get_date(request="End")
        if start_date > end_date:
            print("<Error>: Start date cannot be later than end date.")
            continue

        break

    return start_date, end_date


def get_currency():
    currency_to_exchange = get_currency_code(request= "exchange")
    while True:
        currency_to_receive = get_currency_code(request= "receive")
        if currency_to_receive == currency_to_exchange:
            print("<Error>: Currency parameters need to be of a different type.")
            continue

        break

    return currency_to_exchange, currency_to_receive


########## AUXILIARY METHODS:


def get_date(request: str):
    while True:
        try:
            date = input(f"{request} date (YYYY-MM-DD): ")
            date = dt.strptime(date, "%Y-%m-%d")
            return date.strftime("%Y-%m-%d") # return the YY-MM-DD format without hh:mm (time)

        except ValueError:
            print("<Error>: Invalid date. Use YYYY-MM-DD.\n")


def get_currency_code(request: str):
    while True:
        currency = input(f"Currency to {request}: ").upper()

        # I'd rather keep get_currency_code() limited to validating the syntax and let the API determine whether 'XYZ' is a supported currency
        if len(currency) == 3 and currency.isalpha():
            return currency

        print(f"Error: currency must be a 3-letter code\n")
        # USD   → valid
        # BRL   → valid
        # XYZ   → valid (API decides whether it exists)
        # AB    → invalid
        # USDD  → invalid
        # 123   → invalid
        # U$D   → invalid