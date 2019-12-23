import os
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
              cycler('linestyle', ['-', '--', ':', '-.']))
plt.rc('axes', prop_cycle=monochrome)
plt.style.use('default')


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


plt.style.use(os.path.join(os.environ['HOME'],
              'Templates',
              'matplotlib',
              'oneHalfColumn.mplstyle'))

for case in cases:

    plt.figure(1)
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.set_xlabel('$\\alpha_p$')
    ax.set_ylabel('$z$ (m)')
    ax.set_xlim([0.,0.2])
    ax.set_ylim([0.,1.5])

    var = []
    pos = []
    pos, var = np.loadtxt('dataFinal/'+case+'_solHold_exp.csv',
                          dtype=float,
                          delimiter=',',
                          unpack=True)
    ax.scatter(pos, var, label='Carlos Varas et al. (2017) - Exp.')

    for sim in sims:

        pos = []
        var = []
        pos, var = np.loadtxt('dataFinal/'+sim+'_'+case+'_solHold',
                              unpack=True)
        ax.plot(var[1:], pos[1:], label=sim)

    # var = []
    # pos = []
    # pos, var = np.loadtxt('dataFinal/'+case+'_solHold_sim.csv',
    #                       dtype=float,
    #                       delimiter=',',
    #                       unpack=True)
    # ax.plot(pos, var, label='Carlos Varas et al. (2017) - Sim.')

    ax.legend()
    fig.tight_layout(pad=0.05)

    figName = case+'_solHold'

    plt.savefig('./png/comp/'+figName+'.png',
                    dpi=1200,
                    format='png')

    for i in range(3):
        plt.figure(i+2)
        fig, ax = plt.subplots(figsize=(6,4))
        ax.set_xlabel('$x/W$')
        ax.set_ylabel('$\\alpha_p$')
        ax.set_xlim([0.,1.])
        ax.set_ylim([0.,0.06])

        var = []
        pos = []
        pos, var = np.loadtxt('dataFinal/'+case+'_solVolFrac_l'+str(i+1)+'_exp.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
        ax.scatter(pos, var, label='Carlos Varas et al. (2017) - Exp.')

        for sim in sims:

            pos = []
            var = []
            pos, var = np.loadtxt('dataFinal/'+sim+'_'+case+'_solVolFrac_l'+str(i+1)+'.curve',
                                  skiprows=2,
                                  unpack=True)
            pos /= 0.07
            # pos = -pos/0.07+1
            ax.plot(pos, var, label=sim)

        # var = []
        # pos = []
        # pos, var = np.loadtxt('dataFinal/'+case+'_solVolFrac_l'+str(i+1)+'_sim.csv',
        #                       dtype=float,
        #                       delimiter=',',
        #                       unpack=True)
        # ax.plot(pos, var, label='Carlos Varas et al. (2017) - Sim.')

        ax.legend()
        fig.tight_layout(pad=0.2)

        figName = case+'_solVolFrac_l'+str(i+1)

        plt.savefig('./png/comp/'+figName+'.png',
                    dpi=1200,
                    format='png')
