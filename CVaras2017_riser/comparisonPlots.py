import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.style.use('default')

from cycler import cycler
monochrome = (cycler('linestyle', ['-.', '--', '-']))
plt.rc('axes', prop_cycle=monochrome)


def readData(file,R,norm):
    opts = {'dtype': float,
            'delimiter': ' ',
            'unpack': True,
            'usecols': (0, 1),
            'skiprows': 2}

    x, y = np.loadtxt(file, **opts)

    x = x/R
    if (norm=='mean'):
        yM = np.mean(y)
        y /= yM
    else:
        y = y/norm

    return [x, y]


#---------------------------------------------------------------------------------------


plt.style.use('fourStretched.mplstyle')
fig, ax = plt.subplots(2,2)
#
ax[0,0].set_ylabel(r'$\alpha_p$')
ax[0,0].set_xlabel('$z (m)$')
ax[0,0].axis([0, 0.2, 0, 1.5])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.05/2))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.3))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solHold',
                    1,1)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
var_sim, pos_sim = np.loadtxt('CVaras2017_riser/data/case01_solHold_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0,0].plot(var_sim, pos_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Sim. \n (LES + DEM)')
var_exp, pos_exp = np.loadtxt('CVaras2017_riser/data/case01_solHold_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0,0].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Exp.')
ax[0,0].legend(loc='upper right',title=r'$U_{g,\mathrm{in}} = 6.74$ m/s')
#
ax[0,1].set_ylabel(r'$\alpha_p$')
ax[0,1].set_xlabel('$z (m)$')
ax[0,1].axis([0, 0.2, 0, 1.5])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.05/2))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.3))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('CVaras2017_riser/data/c02_ext_case02_solHold',
                    1,1)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
var_sim, pos_sim = np.loadtxt('CVaras2017_riser/data/case02_solHold_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0,1].plot(var_sim, pos_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
var_exp, pos_exp = np.loadtxt('CVaras2017_riser/data/case02_solHold_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0,1].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[0,1].annotate(r'$U_{g,\mathrm{in}} = 6.35$ m/s',
                 (0.075,1.425),fontsize=10)
#
ax[1,0].set_ylabel(r'$\alpha_p$')
ax[1,0].set_xlabel('$z (m)$')
ax[1,0].axis([0, 0.2, 0, 1.5])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.05/2))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.3))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('CVaras2017_riser/data/c03_ext_case03_solHold',
                    1,1)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
var_sim, pos_sim = np.loadtxt('CVaras2017_riser/data/case03_solHold_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1,0].plot(var_sim, pos_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
var_exp, pos_exp = np.loadtxt('CVaras2017_riser/data/case03_solHold_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1,0].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1,0].annotate(r'$U_{g,\mathrm{in}} = 5.95$ m/s',
                 (0.075,1.425),fontsize=10)
#
ax[1,1].set_ylabel(r'$\alpha_p$')
ax[1,1].set_xlabel('$z (m)$')
ax[1,1].axis([0, 0.2, 0, 1.5])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.05))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.05/2))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.3))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('CVaras2017_riser/data/c04_ext_case04_solHold',
                    1,1)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
var_sim, pos_sim = np.loadtxt('CVaras2017_riser/data/case04_solHold_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1,1].plot(var_sim, pos_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
var_exp, pos_exp = np.loadtxt('CVaras2017_riser/data/case04_solHold_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1,1].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1,1].annotate(r'$U_{g,\mathrm{in}} = 5.55$ m/s',
                 (0.075,1.425),fontsize=10)
#
fig.tight_layout(pad=0.01)
plt.savefig('CVaras2017_riser/CVaras2017_riser_allCases_solHoldup.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


plt.style.use('three.mplstyle')
fig, ax = plt.subplots(3,1)
#
ax[0].set_ylabel(r'$\alpha_p$')
ax[0].set_xlabel('$x/W$')
ax[0].axis([0, 1, 0, 0.12])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l3_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l3_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[0].legend(loc='upper left',title='height = 1.4 m')
#
ax[1].set_ylabel(r'$\alpha_p$')
ax[1].set_xlabel('$x/W$')
ax[1].axis([0, 1, 0, 0.12])
ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l2_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Present work - Simulation')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l2_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1].annotate('height = 1.1 m',(0.25,0.11),fontsize=10)
#
ax[2].set_ylabel(r'$\alpha_p$')
ax[2].set_xlabel('$x/W$')
ax[2].axis([0, 1, 0, 0.12])
ax[2].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[2].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l1_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l1_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[2].annotate('height = 0.8 m',(0.25,0.11),fontsize=10)
#
fig.tight_layout(pad=0.01)
plt.savefig('CVaras2017_riser/CVaras2017_riser_case01_allHeights_solVolFrac.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


plt.style.use('three.mplstyle')
fig, ax = plt.subplots(3,1)
#
ax[0].set_ylabel(r'$\alpha_p$')
ax[0].set_xlabel('$x/W$')
ax[0].axis([0, 1, 0, 0.12])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c02_ext_case02_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case02_solVolFrac_l3_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case02_solVolFrac_l3_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[0].legend(loc='upper left',title='height = 1.4 m')
#
ax[1].set_ylabel(r'$\alpha_p$')
ax[1].set_xlabel('$x/W$')
ax[1].axis([0, 1, 0, 0.12])
ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c02_ext_case02_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case02_solVolFrac_l2_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Present work - Simulation')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case02_solVolFrac_l2_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1].annotate('height = 1.1 m',(0.25,0.11),fontsize=10)
#
ax[2].set_ylabel(r'$\alpha_p$')
ax[2].set_xlabel('$x/W$')
ax[2].axis([0, 1, 0, 0.12])
ax[2].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[2].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c02_ext_case02_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case02_solVolFrac_l1_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case02_solVolFrac_l1_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[2].annotate('height = 0.8 m',(0.25,0.11),fontsize=10)
#
fig.tight_layout(pad=0.01)
plt.savefig('CVaras2017_riser/CVaras2017_riser_case02_allHeights_solVolFrac.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


plt.style.use('three.mplstyle')
fig, ax = plt.subplots(3,1)
#
ax[0].set_ylabel(r'$\alpha_p$')
ax[0].set_xlabel('$x/W$')
ax[0].axis([0, 1, 0, 0.12])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c03_ext_case03_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case03_solVolFrac_l3_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case03_solVolFrac_l3_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[0].legend(loc='upper left',title='height = 1.4 m')
#
ax[1].set_ylabel(r'$\alpha_p$')
ax[1].set_xlabel('$x/W$')
ax[1].axis([0, 1, 0, 0.12])
ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c03_ext_case03_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case03_solVolFrac_l2_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Present work - Simulation')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case03_solVolFrac_l2_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1].annotate('height = 1.1 m',(0.25,0.11),fontsize=10)
#
ax[2].set_ylabel(r'$\alpha_p$')
ax[2].set_xlabel('$x/W$')
ax[2].axis([0, 1, 0, 0.12])
ax[2].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[2].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c03_ext_case03_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case03_solVolFrac_l1_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case03_solVolFrac_l1_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[2].annotate('height = 0.8 m',(0.25,0.11),fontsize=10)
#
fig.tight_layout(pad=0.01)
plt.savefig('CVaras2017_riser/CVaras2017_riser_case03_allHeights_solVolFrac.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


plt.style.use('three.mplstyle')
fig, ax = plt.subplots(3,1)
#
ax[0].set_ylabel(r'$\alpha_p$')
ax[0].set_xlabel('$x/W$')
ax[0].axis([0, 1, 0, 0.12])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c04_ext_case04_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case04_solVolFrac_l3_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case04_solVolFrac_l3_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[0].legend(loc='upper left',title='height = 1.4 m')
#
ax[1].set_ylabel(r'$\alpha_p$')
ax[1].set_xlabel('$x/W$')
ax[1].axis([0, 1, 0, 0.12])
ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c04_ext_case04_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case04_solVolFrac_l2_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Present work - Simulation')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case04_solVolFrac_l2_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1].annotate('height = 1.1 m',(0.25,0.11),fontsize=10)
#
ax[2].set_ylabel(r'$\alpha_p$')
ax[2].set_xlabel('$x/W$')
ax[2].axis([0, 1, 0, 0.12])
ax[2].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[2].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c04_ext_case04_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work - Simulation \n ($k$-$\\varepsilon$ + stochastic collision)')
pos_sim, var_sim = np.loadtxt('CVaras2017_riser/data/case04_solVolFrac_l1_sim.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].plot(pos_sim, var_sim,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Carlos Varas et al. (2017) - Simulation \n (LES + DEM)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case04_solVolFrac_l1_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[2].annotate('height = 0.8 m',(0.25,0.11),fontsize=10)
#
fig.tight_layout(pad=0.01)
plt.savefig('CVaras2017_riser/CVaras2017_riser_case04_allHeights_solVolFrac.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


plt.style.use('three.mplstyle')
fig, ax = plt.subplots(3,1)
#
ax[0].set_ylabel(r'$\alpha_p$')
ax[0].set_xlabel('$x/W$')
ax[0].axis([0, 1, 0, 0.06])
ax[0].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[0].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[0].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Base case')
pos, var = readData('CVaras2017_riser/data/c01_eDiv_case01_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='No transient $\\alpha_p$')
pos, var = readData('CVaras2017_riser/data/c01_eLift_case01_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='With lift forces')
pos, var = readData('CVaras2017_riser/data/c01_extNoDivTau_case01_solVolFrac_l3.curve',
                    0.07,1)
ax[0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle=':',
        label=r'No resolved forces term ($\nabla \cdot \tau_g$)')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l3_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[0].legend(loc='upper left',title='height = 1.4 m')
#
ax[1].set_ylabel(r'$\alpha_p$')
ax[1].set_xlabel('$x/W$')
ax[1].axis([0, 1, 0, 0.06])
ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[1].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[1].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-')
pos, var = readData('CVaras2017_riser/data/c01_eDiv_case01_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.')
pos, var = readData('CVaras2017_riser/data/c01_eLift_case01_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--')
pos, var = readData('CVaras2017_riser/data/c01_extNoDivTau_case01_solVolFrac_l2.curve',
                    0.07,1)
ax[1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle=':')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l2_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[1].annotate('height = 1.1 m',(0.25,0.055),fontsize=10)
#
ax[2].set_ylabel(r'$\alpha_p$')
ax[2].set_xlabel('$x/W$')
ax[2].axis([0, 1, 0, 0.06])
ax[2].xaxis.set_major_locator(plt.MultipleLocator(0.25))
ax[2].xaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax[2].yaxis.set_major_locator(plt.MultipleLocator(0.02))
ax[2].yaxis.set_minor_locator(plt.MultipleLocator(0.01))
pos, var = readData('CVaras2017_riser/data/c01_ext_case01_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-')
pos, var = readData('CVaras2017_riser/data/c01_eDiv_case01_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.')
pos, var = readData('CVaras2017_riser/data/c01_eLift_case01_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--')
pos, var = readData('CVaras2017_riser/data/c01_extNoDivTau_case01_solVolFrac_l1.curve',
                    0.07,1)
ax[2].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle=':')
pos_exp, var_exp = np.loadtxt('CVaras2017_riser/data/case01_solVolFrac_l1_exp.csv',
                               dtype=float,
                               delimiter=',',
                               unpack=True)
ax[2].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Carlos Varas et al. (2017) - Experimental')
ax[2].annotate('height = 0.8 m',(0.25,0.055),fontsize=10)
#
fig.tight_layout(pad=0.01)
plt.savefig('CVaras2017_riser/CVaras2017_riser_case01_allHeights_comparisons_solVolFrac.pdf',
            format='pdf')
