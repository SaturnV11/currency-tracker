from analysis import calc_percentage_change, calc_median
from storage import write_data, read_data
 
 
# analysis.py ----------
 
def test_calc_percentage_change():
    data = [{"rate": "2.00"}, {"rate": "2.50"}]
    assert calc_percentage_change(data) == 0.25
 
 
def test_calc_percentage_change_negative():
    data = [{"rate": "5.00"}, {"rate": "4.00"}]
    assert calc_percentage_change(data) == -0.2
 
 
def test_calc_median_odd():
    data = [{"rate": "1.0"}, {"rate": "3.0"}, {"rate": "2.0"}]
    assert calc_median(data) == 2.0
 
 
def test_calc_median_even():
    data = [{"rate": "1.0"}, {"rate": "2.0"}, {"rate": "3.0"}, {"rate": "4.0"}]
    assert calc_median(data) == 2.5
 
 
# storage.py ----------
 
def test_write_and_read_data(tmp_path):
    data = [
        {"date": "2024-01-01", "base": "USD", "quote": "BRL", "rate": "5.00"},
        {"date": "2024-01-02", "base": "USD", "quote": "BRL", "rate": "5.10"},
    ]
    filepath = tmp_path / "test_output.csv"
 
    write_data(data, str(filepath))
    result = read_data(str(filepath))
 
    assert result == data
 
 
def test_read_data_empty(tmp_path):
    # tmp_path: fixture do pytest, cria uma pasta temporária isolada
    filepath = tmp_path / "test_output.csv"
    filepath = tmp_path / "empty.csv"
    write_data([], str(filepath))
 
    result = read_data(str(filepath))
 
    assert result == []