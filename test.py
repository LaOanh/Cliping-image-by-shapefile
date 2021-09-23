#
# import numpy as np
# import pandas as pd
# from sklearn import preprocessing
# from osgeo import gdal
# import fiona
# import rasterio.mask
# import rasterio as rio
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
# from pathlib import Path
# import tensorflow as tf
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Input, Conv3D, Activation, BatchNormalization, Dense, Dropout,Flatten, Reshape
# from tensorflow.keras.layers import Concatenate
# from tensorflow.keras.regularizers import l2
# import keras_tuner as kt
# import matplotlib.pyplot as plt


root = Tk()
root.title('AC-Net')

class ACNet_app(object):
     def __init__(self,root):
         self.root = root
         self.txt_frm = Frame(self.root, width=900, height=900)
         self.txt_frm.pack(fill="both", expand=True)
         input_label = Label(self.txt_frm, text="Image Inputs", font=('Calibri', 12, 'bold')).grid(row=0, column=0)
         mtl_label = Label(self.txt_frm, text="Choose MTL file").grid(row=1, column=0)
         mtl_button = Button(self.txt_frm,text="open", command=self.openMTL).grid(row=1, column=2)
         self.entry_var_mtl = StringVar()
         mtl_entry = Entry(self.txt_frm, textvariable=self.entry_var_mtl, width=50, borderwidth=5).grid(row=1, column=1)

         bands_label = Label(self.txt_frm, text="Choose band list").grid(row=2, column=0)
         bands_button = Button(self.txt_frm,text="open", command=self.openbandlist).grid(row=2, column=2)
         self.entry_var_bands = StringVar()
         bands_entry = Entry(self.txt_frm, textvariable=self.entry_var_bands, width=50, borderwidth=5).grid(row=2, column=1, ipady=60)

         angles_label = Label(self.txt_frm, text="Choose angles files").grid(row=3, column=0)
         anlges_button = Button(self.txt_frm,text="open", command=self.openangles).grid(row=3, column=2)
         self.entry_var_angles = StringVar()
         angles_entry = Entry(self.txt_frm, textvariable=self.entry_var_angles, width=50, borderwidth=5).grid(row=3, column=1)

         aot_label = Label(self.txt_frm, text="Choose aerosol file").grid(row=4, column=0)
         aot_button = Button(self.txt_frm,text="open", command=self.openAOT).grid(row=4, column=2)
         self.entry_var_aot = StringVar()
         aot_entry = Entry(self.txt_frm, textvariable=self.entry_var_aot, width=50, borderwidth=5).grid(row=4, column=1)

         shp_label = Label(self.txt_frm, text="Lake shapefile input", font=('Calibri', 12, 'bold')).grid(row=6,column=0)
         shp_label1 = Label(self.txt_frm, text="Choose shapefile").grid(row = 7, column=0)
         shp_button = Button(self.txt_frm,text="open", command=self.openSHP).grid(row=7, column=2)
         self.entry_var_shp = StringVar()
         shp_entry = Entry(self.txt_frm, textvariable=self.entry_var_shp, width=50, borderwidth=5).grid(row=7, column=1)

         output_label1 = Label(self.txt_frm, text="Image Output", font=('Calibri', 12, 'bold')).grid(row=10, column=0)
         output_label2 = Label(self.txt_frm, text="Choose output filename").grid(row=11, column=0)
         output_button = Button(self.txt_frm, text="save", command=self.saveoutput).grid(row=11, column=2)
         self.entry_var_output = StringVar()
         output_entry = Entry(self.txt_frm, textvariable=self.entry_var_output, width=50, borderwidth=5).grid(row=11, column=1)

         # runAC_label = Label(self.txt_frm, text="Run AC-Net").grid(row=13, column=1)
         # run_button = Button(self.txt_frm, text="run", command=self.runANN).grid(row=14, column=1)
         #
         # preview_label = Label(self.txt_frm, text="Output preview").grid(row=13, column=5, padx=30)
         # preview_button = Button(self.txt_frm, text="see", command=self.plot_result).grid(row=13, column=6)
     def openMTL(self):
         global metadata
         Root = tkinter.Tk()  # Create a Tkinter.Tk() instance
         Root.withdraw()  # Hide the Tkinter.Tk() instance
         # read MTL file to get rescaling parameters and sun_elevation angle
         metadata = askopenfilename(title=u'Open MTL file', filetypes=[("MTL", ".txt")])
         self.entry_var_mtl.set(metadata)
         # return metadata
     # metadata = openMTL(self)

     def openbandlist(self):
         global bandlist
         bandlist = filedialog.askopenfilenames(title='Choose band 1 to 7 and band 9 files', filetypes=[("TIF", ".tif")])
         self.entry_var_bands.set(bandlist)
         # return bandlist
     # bandlist = openbandlist(self)

     def openangles(self):
         global angles_path
         angles_path = filedialog.askopenfilenames(title='Choose SAA, SZA, VAA, VZA files', filetypes=[("TIF", ".tif")])
         self.entry_var_angles.set(angles_path)
         # return angles_path
     # angles_path = openangles(self)

     def openAOT(self):
         global AOT_path
         AOT_path = askopenfilename(title=u'Open sr_aerosol file', filetypes=[("TIF", ".tif")])
         self.entry_var_aot.set(AOT_path)
         # return AOT_path
     # AOT_path = openAOT(self)

     def openSHP(self):
         global shp_path
         shp_path = askopenfilename(title=U'Open lake shapefile', filetypes=[("SHP", ".shp")])
         self.entry_var_shp.set(shp_path)
         # return shp_path
     # shp_path = openSHP(self)

     def saveoutput(self):
         global save_path
         save_path = filedialog.askdirectory(title=U'Select output folder')
         self.entry_var_output.set(save_path)
         # return save_path
     # save_path = saveoutput(self)

app = ACNet_app(root)
root.mainloop()