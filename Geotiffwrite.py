
## method2

import rasterio
import rasterio.mask
from rasterio import plot
import matplotlib.pyplot as plt

with rasterio.open("D:/ACProgramML/InputforANN/TOAref_13Aug2019_Westlake.tif") as src:
    out_meta = src.meta

out_meta.update({"driver": "GTiff",
                 "height": src.shape[1],
                 "width": src.shape[2]})
with rasterio.open(r"D:\ACProgramML\InputforANN\TOAref_13Aug2019_shape.tif", "w", **out_meta) as dest:
    dest.write(src)

# plotting
img=rasterio.open('D:/ACProgramML/iCORoutput/13Aug2019/iCOR_SR_WestLake13Aug2019.tif')
plot.show(img)