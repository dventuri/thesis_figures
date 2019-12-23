import os
import re
import glob

import sys
sys.path.insert(0,"/home/dventuri/visit/visit2_13_3.linux-x86_64/2.13.3/linux-x86_64/lib/site-packages/")
import visit
visit.Launch(vdir="/home/dventuri/visit/visit2_13_3.linux-x86_64/bin")

import numpy as np


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


input_folder = "/mnt/c/Users/Pichau/Documents/run/CVaras2017_riser/"
output_folder = input_folder+"results/data/"

cases = [
        #  'case01',
        #  'case02',
        #  'case03',
         'case04'
        ]

sims = [
        # 'c01_base',
        # 'c01_bDiv',
        # 'c01_bLift',
        # 'c01_ext',
        # 'c01_eDiv',
        # 'c01_eLift',
        # 'c01_noDivTau',
        # 'c01_noDivSigma',
        # 'c01_extNoDivTau',
        # 'c01_extNoDivSigma',
        # 'c02_base',
        # 'c02_bDiv',
        # 'c02_ext',
        # 'c03_ext',
        'c04_ext'
       ]

Zmin = 0.
Zmax = 1.5
N = 100

l1 = [(0.8, 0.00, 0.),
      (0.8, 0.07, 0.)]
l2 = [(1.1, 0.00, 0.),
      (1.1, 0.07, 0.)]
l3 = [(1.4, 0.00, 0.),
      (1.4, 0.07, 0.)]
locations = ['l1', 'l2', 'l3']

for case in cases:

    for sim in sims:

        filename = input_folder+case+"/"+sim+'/01_VISIT/'+sim+'_*_average.case'
        for db in sorted(glob.glob(filename), key=numericalSort):
            print "Current File Being Processed is: " + db

            aux = [int(x) for x in numbers.findall(db)]
            timestep = str(aux[-1]).zfill(6)

            if os.path.isfile('./data/'+sim+'_'+case+'_'+timestep+'_solHold'):
                print "File already exists"
                continue

            visit.OpenDatabase(db)

            # First plot

            i = 0
            sol_hold = np.zeros(N)
            Zs = np.linspace(Zmin, Zmax, num=N)

            visit.AddPlot("Pseudocolor", "vol_frac_average", 1, 1)
            
            visit.AddOperator("Clip", 1)
            ClipAtts = visit.ClipAttributes()
            ClipAtts.quality = ClipAtts.Fast  # Fast, Accurate
            ClipAtts.funcType = ClipAtts.Plane  # Plane, Sphere
            ClipAtts.plane1Status = 1
            ClipAtts.plane2Status = 0
            ClipAtts.plane3Status = 0
            ClipAtts.plane1Origin = (0, 0, 0)
            ClipAtts.plane1Normal = (0, 1, 0)
            ClipAtts.planeInverse = 1
            ClipAtts.planeToolControlledClipPlane = ClipAtts.Plane1  # None, Plane1, Plane2, Plane3
            visit.SetOperatorOptions(ClipAtts, 1)
            
            visit.AddOperator("Slice", 1)
            PseudocolorAtts = visit.PseudocolorAttributes()
            PseudocolorAtts.minFlag = 1
            PseudocolorAtts.min = 0.
            PseudocolorAtts.maxFlag = 1
            PseudocolorAtts.max = 0.05
            visit.SetPlotOptions(PseudocolorAtts)
            SliceAtts = visit.SliceAttributes()
            SliceAtts.originType = SliceAtts.Point
            SliceAtts.normal = (-1, 0, 0)
            SliceAtts.axisType = SliceAtts.XAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
            SliceAtts.upAxis = (0, 1, 0)
            SliceAtts.project2d = 1

            for Z in Zs:
                SliceAtts.originPoint = (Z, 0, 0)
                visit.SetOperatorOptions(SliceAtts, 1)
                visit.DrawPlots()

                visit.Query("Average Value")
                sol_hold[i] = visit.GetQueryOutputValue()

                i += 1

            visit.DeleteAllPlots()

            np.savetxt(output_folder+sim+'_'+case+'_'+timestep+'_solHold',
                       np.asarray([Zs, sol_hold]).T)

            # Second plot

            visit.AddPlot("Curve", "operators/Lineout/vol_frac_average")

            LineoutAtts = visit.LineoutAttributes()
            LineoutAtts.samplingOn = 1
            LineoutAtts.numberOfSamplePoints = 1000

            for location in locations:

                LineoutAtts.point1 = eval(location)[0]
                LineoutAtts.point2 = eval(location)[1]
                visit.SetOperatorOptions(LineoutAtts, 1)
                visit.DrawPlots()

                e = visit.ExportDBAttributes()
                e.filename = sim+'_'+case+'_'+timestep+'_solVolFrac_'+location
                e.dirname = output_folder
                e.db_type = "Curve2D"
                visit.ExportDatabase(e)

            visit.DeleteAllPlots()

            visit.CloseDatabase(db)
