import re
import glob

import sys
sys.path.insert(0,"/home/dventuri/visit/visit2_13_3.linux-x86_64/2.13.3/linux-x86_64/lib/site-packages/")
import visit
visit.Launch(vdir="/home/dventuri/visit/visit2_13_3.linux-x86_64/bin")


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


input_folder = "/mnt/c/Users/Pichau/Documents/run/OLD/paper01/tsuji_1984/"
output_folder = input_folder+"results/data/"

cases = [
         'case01',
         'case02',
         'case03',
         'case04',
         'case05',
         'case06'
         ]

sims = [
        '1way_ke',
        '2way_ke',
        '4way_ke'
       ]

variables = [
             'w_particle_average',
             'w_average',
             'vol_frac_average',
             'w_particle_rms'
             ]

l1 = [(0, -0.0305/2, 5.11),
      (0, 0.0305/2, 5.11)]
locations = [l1]


for case in cases:

    for sim in sims:

        filename = input_folder+case+"/"+sim+'/01_VISIT/'+sim+'_*_average.case'
        for db in sorted(glob.glob(filename), key=numericalSort):
            print "Current File Being Processed is: " + db

            aux = [int(x) for x in numbers.findall(db)]
            timestep = str(aux[-1]).zfill(6)

            visit.OpenDatabase(db)

            for variable in variables:

                i = 0

                for location in locations:

                    i+=1

                    LineoutAtts = visit.LineoutAttributes()
                    LineoutAtts.point1 = location[0]
                    LineoutAtts.point2 = location[1]
                    LineoutAtts.samplingOn = 1
                    LineoutAtts.numberOfSamplePoints = 1000

                    visit.AddPlot("Curve", "operators/Lineout/"+variable)
                    visit.SetOperatorOptions(LineoutAtts, 1)
                    visit.DrawPlots()
                    e = visit.ExportDBAttributes()
                    e.filename = sim+'_'+case+'_'+timestep+'_'+variable
                    e.dirname = output_folder
                    e.db_type = "Curve2D"
                    visit.ExportDatabase(e)

                    visit.DeleteAllPlots()

            visit.CloseDatabase(db)
