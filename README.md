# Currency Tracker

Final project for CS50P (Harvard). A command-line program that fetches historical exchange rates between two currencies over a chosen period, saves the data to a CSV file, and plots the exchange rate variation with `matplotlib`.

## Features

- Fetches real historical exchange rates via the [Frankfurter API](https://frankfurter.dev/) (free, no API key required)
- Saves the retrieved data to a `.csv` file
- Calculates the percentage change and median exchange rate over the period
- Generates a chart of the exchange rate over time, with the median highlighted
- Accepts parameters via command-line arguments (`argparse`) or interactively for anything not provided

## How to run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run with all parameters via command line:

```bash
python main.py --base USD --quote BRL --start 2025-01-01 --end 2025-01-31
```

Or run without arguments and answer the prompts interactively:

```bash
python main.py
```

Any parameter omitted from the command line will be requested interactively.

### Available arguments

| Argument | Description |
|---|---|
| `-b`, `--base` | Base currency code (e.g. `USD`) |
| `-q`, `--quote` | Quote currency code (e.g. `BRL`) |
| `-s`, `--start` | Start date (`YYYY-MM-DD`) |
| `-e`, `--end` | End date (`YYYY-MM-DD`) |

## Project structure

```
main.py          # orchestrates the main pipeline
argpar.py        # defines and parses command-line arguments
cli_input.py      # collects and validates currencies/dates interactively
api_client.py     # builds the request and fetches data from the API
storage.py        # saves and reads data to/from CSV
analysis.py       # calculates percentage change and median
chart.py          # generates the chart with matplotlib
test_project.py   # automated tests (pytest)
```

## Execution flow

```
command-line arguments
        │
        ├── provided values ──────┐
        │                          │
        └── missing values         │
                │                  │
                ▼                  ▼
          interactive input ──► parameter resolution
                                     │
                                     ▼
                              build API request
                                     │
                                     ▼
                                fetch data
                                     │
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
                save to CSV                    calculate statistics
                                                     │
                                       ┌─────────────┴─────────────┐
                                       ▼                           ▼
                                  display results             generate chart
```

## Tests

```bash
pytest
```

Tests cover the pure calculation functions (`analysis.py`) and CSV reading/writing (`storage.py`).

## Design decisions

- `get_currency_code` only validates the *syntax* of the currency code (3 letters); whether the currency actually exists is left for the API itself to validate.
- Data-fetching (`fetch_data`) and chart-generation (`plot_graph`) functions are not covered by automated tests, since they depend on an external API and visual rendering, respectively.