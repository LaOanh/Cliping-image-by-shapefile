
'''
Created on 22 April 2021 by Oanh Thi La
Purposes:
Clip raster image using a shapefile
'''


import fiona
import rasterio.mask
import rasterio as rio
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


Root = tkinter.Tk() # Create a Tkinter.Tk() instance
Root.withdraw() # Hide the Tkinter.Tk() instance
shp_list = askopenfilename(title=U'Open lake shapefile', filetypes=[("SHP", ".shp")])
img_path = askopenfilename(title=u'Open image file', filetypes=[("TIF", ".tif")])

with fiona.open(shp_list, "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]

with rio.open(img_path) as src:
    out_image, out_transform = rio.mask.mask(src, shapes=shapes, crop=True)
    out_meta = src.meta
    out_meta['dtype'] = "float32"
    out_meta['No Data'] = 0.0
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})

Fname = tkinter.filedialog.asksaveasfilename(title=u'Save clip image file', filetypes=[("TIF", ".tif")])
with rio.open(Fname, "w", **out_meta) as dst:
    dst.write(out_image)





