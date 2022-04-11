# CS175L-01
# Kevin Botwinick
# Expense_pie_chart

import matplotlib.pyplot as plt


def main():
    infile = open('expenses.txt', 'r')
    labels = []
    values = []
    for line in infile.readlines():
        line = line.replace("Payment", " ")
        labels.append(str(line.split()[0]))
        values.append(int(line.split()[1]))
    plt.pie(values, labels=labels, colors=("r", "g", "y", "m", "c", "b"))
    plt.show()


main()
