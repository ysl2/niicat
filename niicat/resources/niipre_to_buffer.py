import matplotlib.pyplot as plt
from niicat.plotter import plot


def main(iFile, dpi, oFile):
    dpi = int(dpi)
    plot(iFile)
    plt.savefig(oFile, dpi=dpi)
