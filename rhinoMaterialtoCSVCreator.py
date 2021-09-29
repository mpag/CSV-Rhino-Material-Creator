import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
import System.Drawing
import csv
import os

file_to_open = "F:/CDG/01_Templates/Rhino/Admin/RevitMaterialLibrary/RevitMaterialAudit_MP.csv"

matName = []
matCol = []
matDiffPath = []
matTransPath = []
matBumpPath = []

mats = sc.doc.Materials

for material in mats:
    matTitle = Rhino.DocObjects.Material.Name.GetValue(material)
    matName.append(matTitle)
    
    matDiff = Rhino.DocObjects.Material.DiffuseColor.GetValue(material)
    matDiffCol = System.Drawing.ColorTranslator.ToString(matDiff)
    matCol.append(matDiffCol)
    
    matTexBitmap = Rhino.DocObjects.Material.GetBitmapTexture(material)
    if matTexBitmap is None:
        matDiffPath.append("None")
    else:
        matTexBitmapPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexBitmap)
        pathTest = os.path.normpath(matTexBitmapPath)
#        print (str(pathTest))
        matDiffPath.append(matTexBitmapPath)
    
    matTexBump = Rhino.DocObjects.Material.GetBumpTexture(material)
    if matTexBump is None:
        matBumpPath.append("None")
    else:
        matTexBumpPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexBump)
        matBumpPath.append(matTexBumpPath)
    
    matTexTrans = Rhino.DocObjects.Material.GetTransparencyTexture(material)
    if matTexTrans is None:
        matTransPath.append("None")
    else:
        matTexTransPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexTrans)
        matTransPath.append(matTexTransPath)


for i, j in enumerate(matName):
    print (matName[i], matCol[i], matDiffPath[i], matBumpPath[i], matTransPath[i])



#with open(file_to_open, mode='r') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader: