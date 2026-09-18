from statistics import median


def calc_percentage_change(data):
    first_rate = float(data[0]["rate"])
    last_rate = float(data[-1]["rate"])

    change = last_rate - first_rate

    return (change / first_rate)


def calc_median(data):
    rates = [float(i["rate"]) for i in data]

    return median(rates)