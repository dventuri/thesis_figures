import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.style.use('default')
plt.style.use('six.mplstyle')

from cycler import cycler
monochrome = (cycler('linestyle', ['-.', '--', '-']))
plt.rc('axes', prop_cycle=monochrome)

R = 0.0305/2.0

def readData(file,R,norm):
    opts = {'dtype': float,
            'delimiter': ' ',
            'unpack': True,
            'usecols': (0, 1),
            'skiprows': 2}

    x, y = np.loadtxt(file, **opts)

    x = (x-R)/R
    y = y/norm

    return [x, y]


#---------------------------------------------------------------------------------------

fig, ax = plt.subplots(3,2)
#
ax[0,0].set_ylabel(r'$U_p/U_{g,\mathrm{mean}}$')
ax[0,0].set_xlabel('$x/R$')
ax[0,0].axis([-1, 1, 0, 1.2])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case01_w_particle_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case01_w_particle_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case01_w_particle_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case01_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 15.6
ax[0,0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[0,0].annotate(r'$\eta=1.0$',(0.17,0.21),fontsize=8)
ax[0,0].annotate(r'$U_{g,\mathrm{mean}}=15.6\,$m/s',(0.17,0.12),fontsize=8)
ax[0,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(0.17,0.03),fontsize=8)
ax[0,0].legend(loc='lower left')
#
ax[1,0].set_ylabel(r'$U_p/U_{g,\mathrm{mean}}$')
ax[1,0].set_xlabel('$x/R$')
ax[1,0].axis([-1, 1, 0, 1.2])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case02_w_particle_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case02_w_particle_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case02_w_particle_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case02_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 15.3
ax[1,0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[1,0].annotate(r'$\eta=2.1$',(0.17,0.21),fontsize=8)
ax[1,0].annotate(r'$U_{g,\mathrm{mean}}=15.3\,$m/s',(0.17,0.12),fontsize=8)
ax[1,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,0].set_ylabel(r'$U_p/U_{g,\mathrm{mean}}$')
ax[2,0].set_xlabel('$x/R$')
ax[2,0].axis([-1, 1, 0, 1.2])
ax[2,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case03_w_particle_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case03_w_particle_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case03_w_particle_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case03_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 14
ax[2,0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[2,0].annotate(r'$\eta=4.2$',(0.17,0.21),fontsize=8)
ax[2,0].annotate(r'$U_{g,\mathrm{mean}}=14.0\,$m/s',(0.17,0.12),fontsize=8)
ax[2,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[0,1].set_ylabel(r'$U_p/U_{g,\mathrm{mean}}$')
ax[0,1].set_xlabel('$x/R$')
ax[0,1].axis([-1, 1, 0, 1.2])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case06_w_particle_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case06_w_particle_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case06_w_particle_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case06_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 7.89
ax[0,1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[0,1].annotate(r'$\eta=1.1$',(0.17,0.21),fontsize=8)
ax[0,1].annotate(r'$U_{g,\mathrm{mean}}=7.96\,$m/s',(0.17,0.12),fontsize=8)
ax[0,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[1,1].set_ylabel(r'$U_p/U_{g,\mathrm{mean}}$')
ax[1,1].set_xlabel('$x/R$')
ax[1,1].axis([-1, 1, 0, 1.2])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case05_w_particle_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case05_w_particle_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case05_w_particle_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case05_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 8
ax[1,1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[1,1].annotate(r'$\eta=2.0$',(0.17,0.21),fontsize=8)
ax[1,1].annotate(r'$U_{g,\mathrm{mean}}=8.00\,$m/s',(0.17,0.12),fontsize=8)
ax[1,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,1].set_ylabel(r'$U_p/U_{g,\mathrm{mean}}$')
ax[2,1].set_xlabel('$x/R$')
ax[2,1].axis([-1, 1, 0, 1.2])
ax[2,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case04_w_particle_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case04_w_particle_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case04_w_particle_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case04_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 7.96
ax[2,1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[2,1].annotate(r'$\eta=3.6$',(0.17,0.21),fontsize=8)
ax[2,1].annotate(r'$U_{g,\mathrm{mean}}=7.89\,$m/s',(0.17,0.12),fontsize=8)
ax[2,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(0.17,0.03),fontsize=8)
ax[2,1].arrow(-0.9, 0.3, 0, -0.2, head_width=0.05, head_length=0.08, fc='k', ec='k')
ax[2,1].annotate(r'$g$',(-0.88,0.2),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1984_verticalPipe/Tsuji1984_verticalPipe_allCases_uPartAverage.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(3,2)
#
ax[0,0].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[0,0].set_xlabel('$x/R$')
ax[0,0].axis([-1, 1, 0, 1.4])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case01_w_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case01_w_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case01_w_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case01_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 15.6
ax[0,0].scatter(pos_exp[::2], var_exp[::2], s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[0,0].annotate(r'$\eta=1.0$',(0.17,0.21),fontsize=8)
ax[0,0].annotate(r'$U_{g,\mathrm{mean}}=15.6\,$m/s',(0.17,0.12),fontsize=8)
ax[0,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(0.17,0.03),fontsize=8)
ax[0,0].legend(loc='lower left')
#
ax[1,0].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[1,0].set_xlabel('$x/R$')
ax[1,0].axis([-1, 1, 0, 1.4])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case02_w_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case02_w_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case02_w_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case02_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 15.3
ax[1,0].scatter(pos_exp[::2], var_exp[::2], s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[1,0].annotate(r'$\eta=2.1$',(0.17,0.21),fontsize=8)
ax[1,0].annotate(r'$U_{g,\mathrm{mean}}=15.3\,$m/s',(0.17,0.12),fontsize=8)
ax[1,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,0].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[2,0].set_xlabel('$x/R$')
ax[2,0].axis([-1, 1, 0, 1.4])
ax[2,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case03_w_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case03_w_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case03_w_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case03_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 14
ax[2,0].scatter(pos_exp[::2], var_exp[::2], s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[2,0].annotate(r'$\eta=4.2$',(0.17,0.21),fontsize=8)
ax[2,0].annotate(r'$U_{g,\mathrm{mean}}=14.0\,$m/s',(0.17,0.12),fontsize=8)
ax[2,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[0,1].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[0,1].set_xlabel('$x/R$')
ax[0,1].axis([-1, 1, 0, 1.4])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case06_w_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case06_w_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case06_w_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case06_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 7.89
ax[0,1].scatter(pos_exp[::2], var_exp[::2], s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[0,1].annotate(r'$\eta=1.1$',(0.17,0.21),fontsize=8)
ax[0,1].annotate(r'$U_{g,\mathrm{mean}}=7.96\,$m/s',(0.17,0.12),fontsize=8)
ax[0,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[1,1].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[1,1].set_xlabel('$x/R$')
ax[1,1].axis([-1, 1, 0, 1.4])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case05_w_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case05_w_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case05_w_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case05_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 8
ax[1,1].scatter(pos_exp[::2], var_exp[::2], s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[1,1].annotate(r'$\eta=2.0$',(0.17,0.21),fontsize=8)
ax[1,1].annotate(r'$U_{g,\mathrm{mean}}=8.00\,$m/s',(0.17,0.12),fontsize=8)
ax[1,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,1].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[2,1].set_xlabel('$x/R$')
ax[2,1].axis([-1, 1, 0, 1.4])
ax[2,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case04_w_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case04_w_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case04_w_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Tsuji1984_verticalPipe/data/case04_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
var_exp /= 7.96
ax[2,1].scatter(pos_exp[::2], var_exp[::2], s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji et al. (1984)')
ax[2,1].annotate(r'$\eta=3.6$',(0.17,0.21),fontsize=8)
ax[2,1].annotate(r'$U_{g,\mathrm{mean}}=7.89\,$m/s',(0.17,0.12),fontsize=8)
ax[2,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(0.17,0.03),fontsize=8)
ax[2,1].arrow(-0.9, 0.3, 0, -0.2, head_width=0.05, head_length=0.08, fc='k', ec='k')
ax[2,1].annotate(r'$g$',(-0.88,0.2),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1984_verticalPipe/Tsuji1984_verticalPipe_allCases_uAverage.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(3,2)
#
ax[0,0].set_ylabel(r'$\alpha_p$')
ax[0,0].set_xlabel('$x/R$')
ax[0,0].axis([-1, 1, 0, 2.e-4])
ax[0,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.5e-4))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1e-4))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case01_vol_frac_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case01_vol_frac_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case01_vol_frac_average.curve',
                    R,15.6)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,0].annotate(r'$\eta=1.0$',(-0.95,1.85e-4),fontsize=8)
ax[0,0].annotate(r'$U_{g,\mathrm{mean}}=15.6\,$m/s',(-0.95,1.70e-4),fontsize=8)
ax[0,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(-0.95,1.55e-4),fontsize=8)
ax[0,0].legend(loc='upper right')
#
ax[1,0].set_ylabel(r'$\alpha_p$')
ax[1,0].set_xlabel('$x/R$')
ax[1,0].axis([-1, 1, 0, 4.e-4])
ax[1,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(1.e-4))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.2e-4))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case02_vol_frac_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case02_vol_frac_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case02_vol_frac_average.curve',
                    R,15.3)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,0].annotate(r'$\eta=2.1$',(-0.95,3.75e-4),fontsize=8)
ax[1,0].annotate(r'$U_{g,\mathrm{mean}}=15.3\,$m/s',(-0.95,3.40e-4),fontsize=8)
ax[1,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(-0.95,3.1e-4),fontsize=8)
#
ax[2,0].set_ylabel(r'$\alpha_p$')
ax[2,0].set_xlabel('$x/R$')
ax[2,0].axis([-1, 1, 0, 8.e-4])
ax[2,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,0].yaxis.set_major_locator(plt.MultipleLocator(2e-4))
ax[2,0].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-4))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case03_vol_frac_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case03_vol_frac_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case03_vol_frac_average.curve',
                    R,14)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[2,0].annotate(r'$\eta=4.2$',(-0.95,7.55e-4),fontsize=8)
ax[2,0].annotate(r'$U_{g,\mathrm{mean}}=14.0\,$m/s',(-0.95,6.95e-4),fontsize=8)
ax[2,0].annotate(r'$d_{p,\mathrm{mean}}=200 \, \mu$m',(-0.95,6.35e-4),fontsize=8)
#
ax[0,1].set_ylabel(r'$\alpha_p$')
ax[0,1].set_xlabel('$x/R$')
ax[0,1].axis([-1, 1, 0, 5e-4])
ax[0,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(1e-4))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.2e-4))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case06_vol_frac_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case06_vol_frac_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case06_vol_frac_average.curve',
                    R,7.89)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,1].annotate(r'$\eta=1.1$',(-0.95,4.75e-4),fontsize=8)
ax[0,1].annotate(r'$U_{g,\mathrm{mean}}=7.96\,$m/s',(-0.95,4.4e-4),fontsize=8)
ax[0,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(-0.95,4e-4),fontsize=8)
#
ax[1,1].set_ylabel(r'$\alpha_p$')
ax[1,1].set_xlabel('$x/R$')
ax[1,1].axis([-1, 1, 0, 1e-3])
ax[1,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.2e-3))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.05e-3))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case05_vol_frac_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case05_vol_frac_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case05_vol_frac_average.curve',
                    R,8)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,1].annotate(r'$\eta=2.0$',(-0.95,0.95e-3),fontsize=8)
ax[1,1].annotate(r'$U_{g,\mathrm{mean}}=8.00\,$m/s',(-0.95,0.865e-3),fontsize=8)
ax[1,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(-0.95,0.78e-3),fontsize=8)
#
ax[2,1].set_ylabel(r'$\alpha_p$')
ax[2,1].set_xlabel('$x/R$')
ax[2,1].axis([-1, 1, 0, 2.e-3])
ax[2,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,1].yaxis.set_major_locator(plt.MultipleLocator(0.5e-3))
ax[2,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1e-3))
pos, var = readData('Tsuji1984_verticalPipe/data/1way_ke_case04_vol_frac_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Tsuji1984_verticalPipe/data/2way_ke_case04_vol_frac_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Tsuji1984_verticalPipe/data/4way_ke_case04_vol_frac_average.curve',
                    R,7.96)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[2,1].annotate(r'$\eta=3.6$',(-0.95,1.85e-3),fontsize=8)
ax[2,1].annotate(r'$U_{g,\mathrm{mean}}=7.89\,$m/s',(-0.95,1.70e-3),fontsize=8)
ax[2,1].annotate(r'$d_{p,\mathrm{mean}}=500 \, \mu$m',(-0.95,1.55e-3),fontsize=8)
ax[2,1].arrow(0.85, 0.4e-3, 0, -0.30e-3, head_width=0.06, head_length=0.00009, fc='k', ec='k')
ax[2,1].annotate(r'$g$',(0.87,0.30e-3),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1984_verticalPipe/Tsuji1984_verticalPipe_allCases_pVolFrac.pdf',
            format='pdf')
