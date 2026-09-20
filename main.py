"""
Main application pipeline:

1. Parse optional command-line arguments with argparse.
2. Resolve currency and date inputs:
   - Use values provided through the command line when available.
   - Prompt interactively for any missing values.
   - Validate all resolved inputs.
3. Build the API request from the resolved parameters.
4. Fetch historical exchange-rate data from the API.
5. Save the retrieved data to a CSV file.
6. Calculate the percentage change and median exchange rate.
7. Display the calculated results.
8. Generate a graph from the retrieved data.

Input flow:

    command-line arguments
            │
            ├── provided values ──────┐
            │                          │
            └── missing values         │
                    │                  │
                    ▼                  ▼
              interactive input ──► input resolution
                                         │
                                         ▼
                                  build API request
                                         │
                                         ▼
                                    fetch data
                                         │
                         ┌───────────────┴───────────────┐
                         ▼                               ▼
                    save to CSV                    analyze data
                                                         │
                                           ┌─────────────┴─────────────┐
                                           ▼                           ▼
                                      display results             generate graph
"""
from cli_input import get_currency, get_date_range
from api_client import build_request, fetch_data
from storage import write_data, read_data
from analysis import calc_percentage_change, calc_median
from chart import plot_graph
from argpar import parse_arguments

def main():
    args = parse_arguments()

    base, quote = get_currency(base=args.base, quote=args.quote)
    start_date, end_date = get_date_range(start_date=args.start, end_date=args.end)   

    url, params = build_request(base, quote, start_date, end_date)

    data = fetch_data(url, params)

    write_data(data)

    percentage_change = calc_percentage_change(data)
    median = calc_median(data)

    print(data[0]["rate"])
    print(data[-1]["rate"])
    print(f"\nPercentage change: {percentage_change:.2%}")
    print(f"Median exchange rate: {median:.2f}")
    plot_graph(data, median)

if __name__ == "__main__":
    main()