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
    matTexBitmapPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexBitmap)
    matDiffPath.append(matTexBitmapPath)
    
    matTexBump = Rhino.DocObjects.Material.GetBumpTexture(material)
    matTexBumpPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexBump)
    matBumpPath.append(matTexBumpPath)
    
    matTexTrans = Rhino.DocObjects.Material.GetTransparencyTexture(material)
    matTexTransPath = Rhino.DocObjects.Texture.FileName.GetValue(matTexTrans)    
    matTransPath.append(matTexTransPath)
    
    
print (matName[0], matCol[0], matDiffPath[0], matTransPath[0], matBumpPath[0])



#with open(file_to_open, mode='r') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader: