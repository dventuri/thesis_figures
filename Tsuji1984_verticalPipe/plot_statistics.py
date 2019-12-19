import os
import re
import glob
import shutil
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
              cycler('linestyle', ['-', '--', ':', '-.']))
plt.rc('axes', prop_cycle=monochrome)


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def copy_rename(old_file_name, new_file_name):
        src_dir = "/mnt/c/Users/Pichau/Documents/run/OLD/paper01/tsuji_1984/results/data"
        dst_dir = "/mnt/c/Users/Pichau/Documents/run/OLD/paper01/tsuji_1984/results/dataFinal"
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file,dst_dir)

        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)


input_folder = "/mnt/c/Users/Pichau/Documents/run/OLD/paper01/tsuji_1984/"
output_folder = input_folder+"results/data/"

variables = [
             'w_particle_average',
             'w_average',
             'vol_frac_average',
             'w_particle_rms'
             ]

ylabels = [
          '$W_P/W_{in}$',
          '$W_f/W_{in}$',
          '$\\alpha_p/\\alpha_{p,av}$',
          '$W_{P,rms}$'
          ]

sims = [
        '1way_ke',
        '2way_ke',
        '4way_ke'
        ]

cases = [
         'case01',
         'case02',
         'case03',
         'case04',
         'case05',
         'case06'
         ]


plt.style.use('oneHalfColumn.mplstyle')

for case in cases:

    for sim in sims:

        timesteps = []
        filename = input_folder+case+"/"+sim+'/01_VISIT/'+sim+'_*_average.case'
        for db in sorted(glob.glob(filename), key=numericalSort):

            aux = [int(x) for x in numbers.findall(db)]
            timestep = str(aux[-1]).zfill(6)

            timesteps.append(timestep)

        for i in range(len(variables)):

            plt.figure(i)
            fig, ax = plt.subplots()

            ax.set_ylabel(ylabels[i])
            ax.set_xlabel('$x/R$')

            for timestep in timesteps[-4:]:

                var = []
                pos = []
                pos, var = np.loadtxt(output_folder+sim+'_'+case+'_'+timestep+'_'+variables[i]+'.curve',
                                      dtype='float',
                                      delimiter=' ',
                                      unpack=True,
                                      skiprows=2)

                R = np.max(pos)/2.
                pos = (pos-R)/R
#                var_center = np.interp(0., pos, var)
#                var = var/var_center

                ax.plot(pos, var, label=sim+' '+timestep)

            ax.legend()
            ax.set_xlim(-1,1)
#            ax.set_ylim(0,2)

            fig.tight_layout(pad=0.2)

            figName = sim+'_'+case+'_'+variables[i]+'_stats'

            # plt.savefig('./png/stats/'+figName+'.png',
            #                 dpi=1200,
            #                 format='png')

            copy_rename(sim+'_'+case+'_'+timestep+'_'+variables[i]+'.curve',
                        sim+'_'+case+'_'+variables[i]+'.curve')
