import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Sample data
x = [1000000, 2000000, 3000000, 4000000]
y = [10, 20, 30, 40]

plt.plot(x, y)

# Define the formatter function
def format_func(value, tick_number):
    return f'{int(value / 1000000)}M'

plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_func))

plt.xlabel('Millions')
plt.ylabel('Values')
plt.title('Numbers formatted in Millions')
plt.show()
