import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
import System.Drawing
import csv
import os

file_to_open = 'F:/CDG/01_Templates/Rhino/Admin/RevitMaterialLibrary/CSV-Rhino-Material-Creator/RhinoSimpleMaterialAudit.csv'

header = ['Name', 'Colour', 'DiffuseMapPath', 'BumpMapPath', 'TransparencyMapPath']
matName = []
matCol = []
matDiffPath = []
matTransPath = []
matBumpPath = []

mats = sc.doc.Materials

for material in mats:
    matTitle = Rhino.DocObjects.Material.Name.GetValue(material)
    matName.append(matTitle)
    
    #Get Material Diffuse Colour
    matDiff = Rhino.DocObjects.Material.DiffuseColor.GetValue(material)
    matDiffCol = System.Drawing.ColorTranslator.ToString(matDiff)
    matCol.append(matDiffCol)
    
    #Get Material Diffuse Bitmap Path
    matTexBitmap = Rhino.DocObjects.Material.GetBitmapTexture(material)
    if matTexBitmap is None:
        matDiffPath.append("None")
    else:
        matTexBitmapPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexBitmap)
        matDiffPath.append(matTexBitmapPath)
    
    #Get Material Bump Bitmap Path
    matTexBump = Rhino.DocObjects.Material.GetBumpTexture(material)
    if matTexBump is None:
        matBumpPath.append("None")
    else:
        matTexBumpPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexBump)
        matBumpPath.append(matTexBumpPath)
    
    #Get Material Diffuse Transparency Path
    matTexTrans = Rhino.DocObjects.Material.GetTransparencyTexture(material)
    if matTexTrans is None:
        matTransPath.append("None")
    else:
        matTexTransPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexTrans)
        matTransPath.append(matTexTransPath)


with open(file_to_open, 'wb') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    for i, j in enumerate(matName):
        row = (matName[i], matCol[i], matDiffPath[i], matBumpPath[i], matTransPath[i])
        print(row)
        csv_writer.writerow(row)