import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, rows):
        fig, axs = plt.subplots(rows)
        self.fig = fig
        self.axs = axs

    def setTitle(self, text):
        self.fig.suptitle(text)

    def setSubplotTitle(self, row, text):
        self.axs[row].set_title(text)

    def show(self):
        plt.show()

    def plotLine(self, row, x, y):
        self.axs[row].plot(x, y)

    def plotMarker(self, row, x, y, color="Green", marker="o", markersize=8):
        self.axs[row].plot(x, y, color=color, marker=marker, markersize=markersize)

    def enableGrid(self, row):
        self.axs[row].grid()
