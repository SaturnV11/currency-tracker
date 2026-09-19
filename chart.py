import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]
import datetime as dt

def plot_graph(data, median):

    dates = [dt.datetime.strptime(i["date"], "%Y-%m-%d") for i in data]
    rates = [float(i["rate"]) for i in data]

    fig, ax = plt.subplots()

    ax.plot(dates, rates)
    plt.axhline(median, linestyle= "--", color="red", label="Average price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Exchange rate")
    plt.legend()


    plt.show()