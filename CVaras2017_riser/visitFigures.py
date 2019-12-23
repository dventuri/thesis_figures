import numpy as np
import re
import glob

import sys
sys.path.insert(0,"/home/dventuri/Software/visit2_13_2.linux-x86_64/2.13.2/linux-x86_64/lib/site-packages/")
import visit
visit.Launch(vdir="/home/dventuri/Software/visit2_13_2.linux-x86_64/bin")


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


input_folder = "/home/dventuri/run/CVaras2017_riser/"
output_folder = input_folder+"results/png/comp/"

cases = ['case01']

sims = [
        '4w_01',
        '4w_02',
        '4w_03',
        '4w_04',
        '4w_05',
        '4w_06',
        '4w_07'
       ]


for case in cases:

    for sim in sims:

        filename = input_folder+case+"/"+sim+'/01_VISIT/'+sim+'_*_average.case'
        db = sorted(glob.glob(filename), key=numericalSort)[-1]
        print "Current File Being Processed is: " + db

        aux = [int(x) for x in numbers.findall(db)]
        timestep = str(aux[-1]).zfill(6)

        visit.OpenDatabase(db)

        # First fig

        for alpha in (0.05,0.6):

            visit.AddPlot("Pseudocolor", "vol_frac_average", 1, 1)

            visit.AddOperator("Slice", 1)
            SliceAtts = visit.SliceAttributes()
            SliceAtts.originType = SliceAtts.Point
            SliceAtts.originPoint = (0, 0, 0)
            SliceAtts.normal = (0, 0, -1)
            SliceAtts.axisType = SliceAtts.ZAxis
            SliceAtts.upAxis = (1, 0, 0)
            SliceAtts.project2d = 1
            SliceAtts.flip = 1
            visit.SetOperatorOptions(SliceAtts, 1)

            PseudocolorAtts = visit.PseudocolorAttributes()
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.min = 0.
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.max = alpha
            visit.SetPlotOptions(PseudocolorAtts)

            View2DAtts = visit.View2DAttributes()
            View2DAtts.windowCoords = (-0.01, 0.07, 0, 1.58)
            View2DAtts.viewportCoords = (0.7, 0.95, 0.1, 0.95)
            visit.SetView2D(View2DAtts)

            AnnotationAtts = visit.AnnotationAttributes()
            AnnotationAtts.axes2D.autoSetTicks = 0
            AnnotationAtts.axes2D.autoSetScaling = 0
            AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside
            AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft
            AnnotationAtts.axes2D.xAxis.title.visible = 0
            AnnotationAtts.axes2D.xAxis.label.visible = 0
            AnnotationAtts.axes2D.xAxis.tickMarks.visible = 0
            AnnotationAtts.axes2D.xAxis.grid = 0
            AnnotationAtts.axes2D.yAxis.title.visible = 0
            AnnotationAtts.axes2D.yAxis.label.visible = 1
            AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
            AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
            AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1.58
            AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.1
            AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.5
            AnnotationAtts.userInfoFlag = 0
            AnnotationAtts.databaseInfoFlag = 0
            AnnotationAtts.legendInfoFlag = 1
            visit.SetAnnotationAttributes(AnnotationAtts)

            visit.DrawPlots()

            SaveWindowAtts = visit.SaveWindowAttributes()
            SaveWindowAtts.outputToCurrentDirectory = 0
            SaveWindowAtts.outputDirectory = output_folder
            SaveWindowAtts.fileName = case+'_'+sim+'_vol_frac_'+str(alpha).replace('.', '')
            SaveWindowAtts.family = 0
            SaveWindowAtts.format = SaveWindowAtts.PNG
            SaveWindowAtts.width = 300
            SaveWindowAtts.height = 1024
            SaveWindowAtts.screenCapture = 0
            SaveWindowAtts.quality = 80
            SaveWindowAtts.compression = SaveWindowAtts.PackBits  # None, PackBits, Jpeg, Deflate
            SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint  # NoConstraint, EqualWidthHeight, ScreenProportions
            SaveWindowAtts.advancedMultiWindowSave = 0
            visit.SetSaveWindowAttributes(SaveWindowAtts)
            visit.SaveWindow()

            visit.DeleteAllPlots()
