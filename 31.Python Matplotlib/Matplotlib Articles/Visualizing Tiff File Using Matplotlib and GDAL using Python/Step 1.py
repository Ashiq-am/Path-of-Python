from osgeo import gdal
import matplotlib.pyplot as plt


dataset = gdal.Open(r'land_shallow_topo_2048.tif')
