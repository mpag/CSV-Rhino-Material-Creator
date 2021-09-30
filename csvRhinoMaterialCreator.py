import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
import System.Drawing
import csv
import os

file_to_open = "F:\CDG\01_Templates\Rhino\Admin\RevitMaterialLibrary\CSV-Rhino-Material-Creator\RevitMaterialAudit_MP.csv"
matName = []
matCol = []
matDiffPath = []
matTransPath = []
matBumpPath = []


def AddMaterial(name, colour, diffPath, transPath, bumpPath):
    #Create the Material, sub this out for CSV read
    rhino_material = Rhino.DocObjects.Material();
    rhino_material.Name = name;
    rhino_material.DiffuseColor = System.Drawing.Color.FromArgb(1, colour[0], colour[1], colour[2]);
    rhino_material.SpecularColor = System.Drawing.Color.WhiteSmoke;
    
    #diff texture
    texture = Rhino.DocObjects.Texture();
    texture.FileName = diffPath
    rhino_material.SetTexture(texture, Rhino.DocObjects.TextureType.Bitmap)
    
    #gloss texture
#    glossTexture = Rhino.DocObjects.Texture();
#    texture.FileName = glossPath
#    rhino_material.SetBumpTexture(texture)
#    rhino_material.
    
    #trans texture
    transTexture = Rhino.DocObjects.Texture();
    texture.FileName = transPath
    rhino_material.SetTransparencyTexture(texture)
    
    #alpha texture
#    bumpTexture = Rhino.DocObjects.Texture();
#    texture.FileName = bumpPath
#    rhino_material.SetBumpTexture(texture)
    
    #bump texture
    bumpTexture = Rhino.DocObjects.Texture();
    texture.FileName = bumpPath
    rhino_material.SetBumpTexture(texture)
    
    #Create the Render Material
    render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, scriptcontext.doc)
    scriptcontext.doc.RenderMaterials.Add(render_material);
    
    #Return result
    scriptcontext.doc.Views.Redraw();
    return Rhino.Commands.Result.Success;


def pathSplitter(path):
    if path is None:
        mattDiffPath.append("")
    else:
        mattBumpPath.append(path)


with open(file_to_open, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            
            #Attribute Name String
            if matName is not None:
                matName.append("Revit_" + row[0])
            else:
                matName.append("None")
            
            #Split Shading Colour String
            if (row[1] != '') :
                cols = row[1].split('/')
                colsRGB = []
                for i in cols:
                    colsRGB.append(int(i))
                matCol.append(colsRGB)
                print (colsRGB)
            
            #Append Diff Path
            if row[2] is None:
                matDiffPath.append("")
            else :
                matDiffPath.append(row[2])
            
            #Append Trans Path
            if row[5] is None:
                matTransPath.append("")
            else :
                matTransPath.append(row[5])
            
            #Append Bump Path
            if row[6] is None:
                matBumpPath.append("")
            else :
                matBumpPath.append(row[6])
            
        line_count += 1
#    print (line_count)
#    print "Complete"

for count, i in enumerate(matName):
    print (count, i)
    AddMaterial(i, matCol[count], matDiffPath[count], matTransPath[count], matBumpPath[count])

#Path Checking Routines
#pathTest = os.path.normpath(matDiffPath[0])
#print pathTest