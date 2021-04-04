import math
import shapely.geometry as sg

from pcbflow import *


if __name__ == "__main__":
    brd = Board((40, 30))
    brd.outline()
    brd.fill_any("GTL", "GND")
    brd.fill_any("GBL", "GND")
    brd.save("%s" % (__file__[:-3]))
