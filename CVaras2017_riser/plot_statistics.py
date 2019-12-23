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
plt.style.use('default')


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def copy_rename(old_file_name, new_file_name):
        src_dir = "/mnt/c/Users/Pichau/Documents/run/CVaras2017_riser/results/data"
        dst_dir = "/mnt/c/Users/Pichau/Documents/run/CVaras2017_riser/results/dataFinal"
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file,dst_dir)

        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)


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


plt.style.use('oneHalfColumn.mplstyle')

for case in cases:

    for sim in sims:

        timesteps = []
        filename = input_folder+case+"/"+sim+'/01_VISIT/'+sim+'_*_average.case'
        for db in sorted(glob.glob(filename), key=numericalSort):

            aux = [int(x) for x in numbers.findall(db)]
            timestep = str(aux[-1]).zfill(6)

            timesteps.append(timestep)

        # First plot

        plt.figure()
        fig, ax = plt.subplots(figsize=(4, 6))
        ax.set_xlabel('$<\\phi_s>$')
        ax.set_ylabel('$z$ (m)')
        ax.set_xlim([0.,0.2])
        ax.set_ylim([0.,1.5])

        # for timestep in timesteps[-4:]:
        for timestep in timesteps[-10::3]:

            pos = []
            var = []
            pos, var = np.loadtxt(output_folder+sim+'_'+case+'_'+timestep+'_solHold',
                                  unpack=True)
            ax.plot(var, pos, label=sim+' '+timestep, markevery=20)

        ax.legend()
        fig.tight_layout(pad=0.2)

        figName = sim+'_'+case+'_solHold_stats'

        plt.savefig(input_folder+'results/png/stats/'+figName+'.png',
                    dpi=1200,
                    format='png')

        # move last file to /dataFinal
        copy_rename(sim+'_'+case+'_'+timesteps[-1]+'_solHold',
                    sim+'_'+case+'_solHold')

        # Second plot

        for i in range(3):
            plt.figure()
            fig, ax = plt.subplots(figsize=(6,4))
            ax.set_xlabel('$x/W$')
            ax.set_ylabel('$<\\phi_s>$')
            ax.set_xlim([0.,1.])
            ax.set_ylim([0.,0.05])

            # for timestep in timesteps[-4:]:
            for timestep in timesteps[-10::3]:

                pos = []
                var = []
                pos, var = np.loadtxt(output_folder+sim+'_'+case+'_'+timestep+'_solVolFrac_l'+str(i+1)+'.curve',
                                      skiprows=2,
                                      unpack=True)
                pos /= 0.07
                ax.plot(pos, var, label=sim+' '+timestep, markevery=20)

            ax.legend()
            fig.tight_layout(pad=0.2)

            figName = sim+'_'+case+'_solVolFrac_l'+str(i+1)+'_stats.curve'

            plt.savefig(input_folder+'results/png/stats/'+figName+'.png',
                        dpi=1200,
                        format='png')

            # move last file to /dataFinal
            copy_rename(sim+'_'+case+'_'+timesteps[-1]+'_solVolFrac_l'+str(i+1)+'.curve',
                        sim+'_'+case+'_solVolFrac_l'+str(i+1)+'.curve')
