import requests  # type: ignore[import-untyped]

def build_request(base_currency, quote_currency, start_date, end_date) -> tuple[str, dict]:
    url = "https://api.frankfurter.dev/v2/rates"

    params = {
        "base": base_currency,
        "quotes": quote_currency,
        "from": start_date,
        "to": end_date
    }

    return url, params


def fetch_data(url: str, params: dict) -> list[dict]:
    response = requests.get(url= url, params= params, timeout= 10)

    response.raise_for_status()

    return response.json()