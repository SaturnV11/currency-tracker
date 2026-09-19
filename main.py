"""
    main()
    │
    ├── recebe moeda e período __check__
    │
    ├── buscar_cotacoes() __check__
    │       └── API: Frankfurter (url= https://api.frankfurter.dev)
    │
    ├── salvar_csv() __check__
    │
    ├── ler_csv() __check__
    │
    ├── calcular_variacao_percentual() __check__
    ├── calcular_media_periodo() __check__
    │
    └── gerar_grafico() __TODO__

    ** implementar argparse
    # FOR ARGUMENT PARSING: python main.py --base USD --quote BRL --start 2025-01-01 --end 2025-01-31 --output rates.csv

    API: 
"""
from cli_input import get_currency, get_date_range
from api_client import build_request, fetch_data
from storage import write_data, read_data
from analysis import calc_percentage_change, calc_median
from chart import plot_graph

def main():
    url, params = build_request(*get_currency(), *get_date_range())

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