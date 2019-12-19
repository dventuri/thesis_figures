import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.style.use('default')
plt.style.use('six.mplstyle')

from cycler import cycler
monochrome = (cycler('linestyle', ['-.', '--', '-']))
plt.rc('axes', prop_cycle=monochrome)

R = 0.042/2.0

def readData(file,R,norm):
    opts = {'dtype': float,
            'delimiter': ' ',
            'unpack': True,
            'usecols': (0, 1),
            'skiprows': 2}

    x, y = np.loadtxt(file, **opts)

    x = (x-R)/R
    if (norm=='mean'):
        yM = np.mean(y)
        y /= yM
    else:
        y = y/norm

    return [x, y]


#---------------------------------------------------------------------------------------

fig, ax = plt.subplots(3,2)
#
ax[0,0].set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax[0,0].set_xlabel('$x/R$')
ax[0,0].axis([-1, 1, 0, 1.2])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case01_w_particle_average.curve',
                    R,'mean')
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case01_w_particle_average.curve',
                    R,'mean')
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case01_w_particle_average.curve',
                    R,'mean')
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Mathisen2008_verticalPipe/data/case01_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
varMean = np.mean(var_exp)
var_exp /= varMean
ax[0,0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Mathisen et al.\n (2008)')
ax[0,0].annotate(r'$\eta=3.1$',(0.17,0.21),fontsize=8)
ax[0,0].annotate(r'$U_{g,\mathrm{in}}=6.0\,$m/s',(0.17,0.12),fontsize=8)
ax[0,0].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
ax[0,0].legend(loc='lower left')
#
ax[0,1].set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax[0,1].set_xlabel('$x/R$')
ax[0,1].axis([-1, 1, 0, 1.2])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case03_w_particle_average.curve',
                    R,'mean')
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case03_w_particle_average.curve',
                    R,'mean')
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case03_w_particle_average.curve',
                    R,'mean')
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Mathisen2008_verticalPipe/data/case03_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
varMean = np.mean(var_exp)
var_exp /= varMean
ax[0,1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Mathisen et al. (2008)')
ax[0,1].annotate(r'$\eta=3.1$',(0.17,0.21),fontsize=8)
ax[0,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[0,1].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[1,0].set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax[1,0].set_xlabel('$x/R$')
ax[1,0].axis([-1, 1, 0, 1.2])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case04_w_particle_average.curve',
                    R,'mean')
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case04_w_particle_average.curve',
                    R,'mean')
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case04_w_particle_average.curve',
                    R,'mean')
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Mathisen2008_verticalPipe/data/case04_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
varMean = np.mean(var_exp)
var_exp /= varMean
ax[1,0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Mathisen et al. (2008)')
ax[1,0].annotate(r'$\eta=4.2$',(0.17,0.21),fontsize=8)
ax[1,0].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[1,0].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[1,1].set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax[1,1].set_xlabel('$x/R$')
ax[1,1].axis([-1, 1, 0, 1.2])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case05_w_particle_average.curve',
                    R,'mean')
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case05_w_particle_average.curve',
                    R,'mean')
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case05_w_particle_average.curve',
                    R,'mean')
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Mathisen2008_verticalPipe/data/case05_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
varMean = np.mean(var_exp)
var_exp /= varMean
ax[1,1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Mathisen et al. (2008)')
ax[1,1].annotate(r'$\eta=5.2$',(0.17,0.21),fontsize=8)
ax[1,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[1,1].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,0].set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax[2,0].set_xlabel('$x/R$')
ax[2,0].axis([-1, 1, 0, 1.2])
ax[2,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case09_w_particle_average.curve',
                    R,'mean')
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case09_w_particle_average.curve',
                    R,'mean')
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case09_w_particle_average.curve',
                    R,'mean')
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Mathisen2008_verticalPipe/data/case09_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
varMean = np.mean(var_exp)
var_exp /= varMean
ax[2,0].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Mathisen et al. (2008)')
ax[2,0].annotate(r'$\eta=6.3$',(0.17,0.21),fontsize=8)
ax[2,0].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[2,0].annotate(r'$d_{p,\mathrm{mean}}=530 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,1].set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax[2,1].set_xlabel('$x/R$')
ax[2,1].axis([-1, 1, 0, 1.2])
ax[2,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case10_w_particle_average.curve',
                    R,'mean')
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case10_w_particle_average.curve',
                    R,'mean')
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case10_w_particle_average.curve',
                    R,'mean')
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
pos_exp, var_exp = np.loadtxt('Mathisen2008_verticalPipe/data/case10_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
varMean = np.mean(var_exp)
var_exp /= varMean
ax[2,1].scatter(pos_exp, var_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Mathisen et al. (2008)')
ax[2,1].annotate(r'$\eta=7.9$',(0.17,0.21),fontsize=8)
ax[2,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[2,1].annotate(r'$d_{p,\mathrm{mean}}=530 \, \mu$m',(0.17,0.03),fontsize=8)
ax[2,1].arrow(-0.9, 0.3, 0, -0.2, head_width=0.05, head_length=0.08, fc='k', ec='k')
ax[2,1].annotate(r'$g$',(-0.88,0.2),fontsize=8)
#
fig.tight_layout(pad=0.01)
# plt.savefig('Mathisen2008_verticalPipe/Mathisen2008_verticalPipe_allCases_uPartAverage.pdf',
#             format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(3,2)
#
ax[0,0].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[0,0].set_xlabel('$x/R$')
ax[0,0].axis([-1, 1, 0, 1.2])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case01_w_average.curve',
                    R,'mean')
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case01_w_average.curve',
                    R,'mean')
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case01_w_average.curve',
                    R,'mean')
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,0].annotate(r'$\eta=3.1$',(0.17,0.21),fontsize=8)
ax[0,0].annotate(r'$U_{g,\mathrm{in}}=6.0\,$m/s',(0.17,0.12),fontsize=8)
ax[0,0].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
ax[0,0].legend(loc='lower left')
#
ax[0,1].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[0,1].set_xlabel('$x/R$')
ax[0,1].axis([-1, 1, 0, 1.2])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case03_w_average.curve',
                    R,'mean')
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case03_w_average.curve',
                    R,'mean')
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case03_w_average.curve',
                    R,'mean')
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,1].annotate(r'$\eta=3.1$',(0.17,0.21),fontsize=8)
ax[0,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[0,1].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[1,0].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[1,0].set_xlabel('$x/R$')
ax[1,0].axis([-1, 1, 0, 1.2])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case04_w_average.curve',
                    R,'mean')
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case04_w_average.curve',
                    R,'mean')
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case04_w_average.curve',
                    R,'mean')
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,0].annotate(r'$\eta=4.2$',(0.17,0.21),fontsize=8)
ax[1,0].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[1,0].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[1,1].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[1,1].set_xlabel('$x/R$')
ax[1,1].axis([-1, 1, 0, 1.2])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case05_w_average.curve',
                    R,'mean')
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case05_w_average.curve',
                    R,'mean')
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case05_w_average.curve',
                    R,'mean')
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,1].annotate(r'$\eta=5.2$',(0.17,0.21),fontsize=8)
ax[1,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[1,1].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,0].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[2,0].set_xlabel('$x/R$')
ax[2,0].axis([-1, 1, 0, 1.2])
ax[2,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,0].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,0].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case09_w_average.curve',
                    R,'mean')
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case09_w_average.curve',
                    R,'mean')
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case09_w_average.curve',
                    R,'mean')
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[2,0].annotate(r'$\eta=6.3$',(0.17,0.21),fontsize=8)
ax[2,0].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[2,0].annotate(r'$d_{p,\mathrm{mean}}=530 \, \mu$m',(0.17,0.03),fontsize=8)
#
ax[2,1].set_ylabel(r'$U_g/U_{g,\mathrm{mean}}$')
ax[2,1].set_xlabel('$x/R$')
ax[2,1].axis([-1, 1, 0, 1.2])
ax[2,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,1].yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[2,1].yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case10_w_average.curve',
                    R,'mean')
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case10_w_average.curve',
                    R,'mean')
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case10_w_average.curve',
                    R,'mean')
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[2,1].annotate(r'$\eta=7.9$',(0.17,0.21),fontsize=8)
ax[2,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.12),fontsize=8)
ax[2,1].annotate(r'$d_{p,\mathrm{mean}}=530 \, \mu$m',(0.17,0.03),fontsize=8)
ax[2,1].arrow(-0.9, 0.3, 0, -0.2, head_width=0.05, head_length=0.08, fc='k', ec='k')
ax[2,1].annotate(r'$g$',(-0.88,0.2),fontsize=8)
#
fig.tight_layout(pad=0.01)
# plt.savefig('Mathisen2008_verticalPipe/Mathisen2008_verticalPipe_allCases_uAverage.pdf',
#             format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(3,2)
#
ax[0,0].set_ylabel(r'$\alpha_p$')
ax[0,0].set_xlabel('$x/R$')
ax[0,0].axis([-1, 1, 0, 5e-3])
ax[0,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(1e-3))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-3))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case01_vol_frac_average.curve',
                    R,1)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case01_vol_frac_average.curve',
                    R,1)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case01_vol_frac_average.curve',
                    R,1)
ax[0,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,0].annotate(r'$\eta=3.1$',(0.17,0.9e-3),fontsize=8)
ax[0,0].annotate(r'$U_{g,\mathrm{in}}=6.0\,$m/s',(0.17,0.5e-3),fontsize=8)
ax[0,0].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.1e-3),fontsize=8)
ax[0,0].legend(loc='lower left')
#
ax[0,1].set_ylabel(r'$\alpha_p$')
ax[0,1].set_xlabel('$x/R$')
ax[0,1].axis([-1, 1, 0, 4e-3])
ax[0,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(1e-3))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-3))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case03_vol_frac_average.curve',
                    R,1)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case03_vol_frac_average.curve',
                    R,1)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case03_vol_frac_average.curve',
                    R,1)
ax[0,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,1].annotate(r'$\eta=3.1$',(0.17,0.65e-3),fontsize=8)
ax[0,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.35e-3),fontsize=8)
ax[0,1].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.075e-3),fontsize=8)
#
ax[1,0].set_ylabel(r'$\alpha_p$')
ax[1,0].set_xlabel('$x/R$')
ax[1,0].axis([-1, 1, 0, 5e-3])
ax[1,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(1e-3))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-3))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case04_vol_frac_average.curve',
                    R,1)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case04_vol_frac_average.curve',
                    R,1)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case04_vol_frac_average.curve',
                    R,1)
ax[1,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,0].annotate(r'$\eta=4.2$',(0.17,0.9e-3),fontsize=8)
ax[1,0].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.5e-3),fontsize=8)
ax[1,0].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.1e-3),fontsize=8)
#
ax[1,1].set_ylabel(r'$\alpha_p$')
ax[1,1].set_xlabel('$x/R$')
ax[1,1].axis([-1, 1, 0, 6e-3])
ax[1,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(1e-3))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-3))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case05_vol_frac_average.curve',
                    R,1)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case05_vol_frac_average.curve',
                    R,1)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case05_vol_frac_average.curve',
                    R,1)
ax[1,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,1].annotate(r'$\eta=5.2$',(0.17,1.1e-3),fontsize=8)
ax[1,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.6e-3),fontsize=8)
ax[1,1].annotate(r'$d_{p,\mathrm{mean}}=518 \, \mu$m',(0.17,0.2e-3),fontsize=8)
#
ax[2,0].set_ylabel(r'$\alpha_p$')
ax[2,0].set_xlabel('$x/R$')
ax[2,0].axis([-1, 1, 0, 5e-3])
ax[2,0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,0].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,0].yaxis.set_major_locator(plt.MultipleLocator(1e-3))
ax[2,0].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-3))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case09_vol_frac_average.curve',
                    R,1)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case09_vol_frac_average.curve',
                    R,1)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case09_vol_frac_average.curve',
                    R,1)
ax[2,0].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[2,0].annotate(r'$\eta=6.3$',(0.17,0.9e-3),fontsize=8)
ax[2,0].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.5e-3),fontsize=8)
ax[2,0].annotate(r'$d_{p,\mathrm{mean}}=530 \, \mu$m',(0.17,0.1e-3),fontsize=8)
#
ax[2,1].set_ylabel(r'$\alpha_p$')
ax[2,1].set_xlabel('$x/R$')
ax[2,1].axis([-1, 1, 0, 6e-3])
ax[2,1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax[2,1].xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[2,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[2,1].yaxis.set_major_locator(plt.MultipleLocator(1e-3))
ax[2,1].yaxis.set_minor_locator(plt.MultipleLocator(0.5e-3))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_case10_vol_frac_average.curve',
                    R,1)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
pos, var = readData('Mathisen2008_verticalPipe/data/2way_ke_case10_vol_frac_average.curve',
                    R,1)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
pos, var = readData('Mathisen2008_verticalPipe/data/4way_ke_case10_vol_frac_average.curve',
                    R,1)
ax[2,1].plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[2,1].annotate(r'$\eta=7.9$',(0.17,1.1e-3),fontsize=8)
ax[2,1].annotate(r'$U_{g,\mathrm{in}}=8.0\,$m/s',(0.17,0.6e-3),fontsize=8)
ax[2,1].annotate(r'$d_{p,\mathrm{mean}}=530 \, \mu$m',(0.17,0.2e-3),fontsize=8)
ax[2,1].arrow(-0.9, 1.5e-3, 0, -1e-3, head_width=0.07, head_length=0.0004, fc='k', ec='k')
ax[2,1].annotate(r'$g$',(-0.88,1.2e-3),fontsize=8)
#
fig.tight_layout(pad=0.01)
# plt.savefig('Mathisen2008_verticalPipe/Mathisen2008_verticalPipe_allCases_pVolFrac.pdf',
#             format='pdf')


#---------------------------------------------------------------------------------------

plt.style.use('oneHalfColumn.mplstyle')

fig, ax = plt.subplots()
ax.set_ylabel(r'$U_p/U_{p,\mathrm{mean}}$')
ax.set_xlabel('$x/R$')
ax.axis([0, 1, 0, 1.2])
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax.xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01_w_particle_average.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Smooth wall - all forces')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01a_w_particle_average.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Smooth wall - no Saffman')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01b_w_particle_average.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Smooth wall - no Saffman and Magnus')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01c_w_particle_average.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle=':',
        label='Smooth wall - no turbulent dispersion')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01d_w_particle_average.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        marker='o',
        markevery=(0.1),
        markersize=3,
        label='Rough wall - all forces')
ax.arrow(0.9, 0.25, 0, -0.15, head_width=0.03, head_length=0.04, fc='k', ec='k')
ax.annotate(r'$g$',(0.91,0.2),fontsize=10)
ax.legend(loc='lower left')
fig.tight_layout(pad=0.01)
plt.savefig('Mathisen2008_verticalPipe/Mathisen2008_verticalPipe_case01_pVel.pdf',
            format='pdf')

fig, ax = plt.subplots()
ax.set_ylabel(r'$C_p/C_{p,\mathrm{mean}}$')
ax.set_xlabel('$x/R$')
ax.axis([0, 1, 0, 2])
ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax.xaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01_p_concentration.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Smooth wall - all forces')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01a_p_concentration.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Smooth wall - no Saffman')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01b_p_concentration.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Smooth wall - no Saffman and Magnus')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01c_p_concentration.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle=':',
        label='Smooth wall - no turbulent dispersion')
pos, var = readData('Mathisen2008_verticalPipe/data/1way_ke_mathisen_case01d_p_concentration.curve',
                    R,'mean')
ax.plot(pos, var,
        color='black',
        linewidth=1,
        linestyle='-',
        marker='o',
        markevery=(0.1),
        markersize=3,
        label='Rough wall - all forces')
ax.arrow(0.9, 0.4, 0, -0.25, head_width=0.03, head_length=0.06, fc='k', ec='k')
ax.annotate(r'$g$',(0.91,0.3),fontsize=10)
ax.legend(loc='lower left')
fig.tight_layout(pad=0.01)
plt.savefig('Mathisen2008_verticalPipe/Mathisen2008_verticalPipe_case01_pConc.pdf',
            format='pdf')
