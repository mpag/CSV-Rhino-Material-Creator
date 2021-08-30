import Rhino
import rhinoscriptsyntax as rs
import scriptcontext
import System.Drawing
import csv
import os

file_to_open = "F:\CDG\01_Templates\Rhino\Admin\RevitMaterialLibrary\CSV-Rhino-Material-Creator\RevitMaterialAudit_Test.csv"
matName = []
matCol = []
matDiffPath = []
matBumpPath = []
matAlphaPath = []

def AddMaterial(name, colour, diffPath, bumpPath):
    #Create the Material, sub this out for CSV read
    rhino_material = Rhino.DocObjects.Material();
    rhino_material.Name = name;
    rhino_material.DiffuseColor = System.Drawing.Color.FromArgb(colour[3], colour[0], colour[1], colour[2]);
    rhino_material.SpecularColor = System.Drawing.Color.WhiteSmoke;
    
    #diff texture
    texture = Rhino.DocObjects.Texture();
    texture.FileName = diffPath
    #texture.FileName = "F:/CDG/01_Templates/Rhino/Material Collation/Library/Textures/TexturesCom_Cobblestone2_Pink.jpg"
    rhino_material.SetTexture(texture, Rhino.DocObjects.TextureType.Bitmap)
    
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
        a = path.split('$')
        if len(a) = 3:
            mattBumpPath.append(a[0])
            matt

with open(file_to_open, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 1:
            
            #Attribute Name String
            matName.append("Revit_" + row[0])
            
            #Split Shading Colour String
            cols = row[1].split(',')
            colsRGB = []
            for i in cols:
                a = i.split('= ')
                cols2 = a[1]
                cols3 = cols2.split(')')
                colsRGB.append(int(cols3[0]))
            matCol.append(colsRGB)
            
            #Append Diff Path
            if row[10] is None:
                matDiffPath.append("")
            else :
                matDiffPath.append(row[10])
            
            #Append Bump Path
            if row[10] is None:
                matBumpPath.append("")
            else :
                matBumpPath.append(row[10])
            
        line_count += 1
    print "Complete"

for count, i in enumerate(matName):
    AddMaterial(i, matCol[count], matDiffPath[count], matBumpPath[count])

#Path Checking Routines
#pathTest = os.path.normpath(matDiffPath[0])
#print pathTest