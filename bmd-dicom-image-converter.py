#!/user/bin/env python3 
# coding: utf-8

# bmd-dicom-image-converter
# Converts Ultrasound DICOM images to JPG with high quality. 
#
# bmd 2021-05-12 
#
# pre-reqs: pydicom, PIL

#Imports
import os
import pydicom
import pydicom_PIL

def convertFolderOfDICOMImagesToJPG():
    """ Converts folder of DICOM images into JPEGs"""
    inputPath = "/Users/duivesteyn/Downloads/BabyScans/ExportedStudy/Dicom/pics/"           #Get Folder Path
    outputPath = "/Users/duivesteyn/Downloads/BabyScans/_outputs/"

    #Loop images in path, save into output folder
    for image_path in os.listdir(inputPath):
        inputPathFull = os.path.join(inputPath, image_path)
        outputPathFull = os.path.join(outputPath, image_path)

        if image_path[0] != "." :
            ds = pydicom.filereader.dcmread(inputPathFull)                                  #Read Image using pydicom
            print(ds)

            im = pydicom_PIL.get_PIL_image(ds)
            #im.show()                                                                      #Display image in computer UI
            im.save(outputPathFull + '.jpg', "JPEG", quality=100)                           #Save image as high quality jpeg

#Converts DICOM Images to JPEGS
convertFolderOfDICOMImagesToJPG()