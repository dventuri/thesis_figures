import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.style.use('default')
plt.style.use('four.mplstyle')

from cycler import cycler
monochrome = (cycler('linestyle', ['-.', '--', '-']))
plt.rc('axes', prop_cycle=monochrome)

R = 0.030/2.0
Uin = 15.

def readData(file,R,norm):
    opts = {'dtype': float,
            'delimiter': ' ',
            'unpack': True,
            'usecols': (0, 1),
            'skiprows': 2}

    x, y = np.loadtxt(file, **opts)

    x = (x-R)/R
    y = y/norm

    return [y, x]




xlabels = [
           r'$U_p/U_{g,\mathrm{in}}$',
           r'$U_g/U_{g,\mathrm{in}}$',
           r'$C_p/C_{p,\mathrm{mean}}$',
           r'$d_p/d_{p,\mathrm{mean}}$'
          ]



#---------------------------------------------------------------------------------------

fig, ax = plt.subplots(2,2)
#
ax[0,0].set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
ax[0,0].set_ylabel('$y/R$')
ax[0,0].axis([0, 1.4, -1, 1])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case01_w_particle_average.curve',
                    R,Uin)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case01_w_particle_average.curve',
                    R,Uin)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case01_w_particle_average.curve',
                    R,Uin)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case01_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[0,0].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[0,0].annotate(r'$\eta=0.4$',(0.1,0.75),fontsize=10)
ax[0,0].legend(loc='lower left')
#
ax[0,1].set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
ax[0,1].set_ylabel('$y/R$')
ax[0,1].axis([0, 1.4, -1, 1])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case08_w_particle_average.curve',
                    R,Uin)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case08_w_particle_average.curve',
                    R,Uin)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case08_w_particle_average.curve',
                    R,Uin)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case08_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[0,1].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[0,1].annotate(r'$\eta=0.9$',(0.1,0.75),fontsize=10)
#
ax[1,0].set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
ax[1,0].set_ylabel('$y/R$')
ax[1,0].axis([0, 1.4, -1, 1])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case09_w_particle_average.curve',
                    R,Uin)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case09_w_particle_average.curve',
                    R,Uin)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case09_w_particle_average.curve',
                    R,Uin)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case09_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[1,0].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[1,0].annotate(r'$\eta=2.2$',(0.1,0.75),fontsize=10)
#
ax[1,1].set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
ax[1,1].set_ylabel('$y/R$')
ax[1,1].axis([0, 1.4, -1, 1])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case10_w_particle_average.curve',
                    R,Uin)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case10_w_particle_average.curve',
                    R,Uin)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case10_w_particle_average.curve',
                    R,Uin)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case10_w_particle_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[1,1].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[1,1].annotate(r'$\eta=2.8$',(0.1,0.75),fontsize=10)
ax[1,1].arrow(0.1, -0.6, 0, -0.25, head_width=0.035, head_length=0.08, fc='k', ec='k')
ax[1,1].annotate(r'$g$',(0.11,-0.75),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1982_horizontalPipe/Tsuji1982_horizontalPipe_allCases_uPartAverage.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(2,2)
#
ax[0,0].set_xlabel(r'$U_g/U_{g,\mathrm{in}}$')
ax[0,0].set_ylabel('$y/R$')
ax[0,0].axis([0, 1.4, -1, 1])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case01_w_average.curve',
                    R,Uin)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case01_w_average.curve',
                    R,Uin)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case01_w_average.curve',
                    R,Uin)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case01_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[0,0].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[0,0].annotate(r'$\eta=0.4$',(0.1,0.75),fontsize=10)
ax[0,0].legend(loc='lower left')
#
ax[0,1].set_xlabel(r'$U_g/U_{g,\mathrm{in}}$')
ax[0,1].set_ylabel('$y/R$')
ax[0,1].axis([0, 1.4, -1, 1])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case08_w_average.curve',
                    R,Uin)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case08_w_average.curve',
                    R,Uin)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case08_w_average.curve',
                    R,Uin)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case08_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[0,1].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[0,1].annotate(r'$\eta=0.9$',(0.1,0.75),fontsize=10)
#
ax[1,0].set_xlabel(r'$U_g/U_{g,\mathrm{in}}$')
ax[1,0].set_ylabel('$y/R$')
ax[1,0].axis([0, 1.4, -1, 1])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case09_w_average.curve',
                    R,Uin)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case09_w_average.curve',
                    R,Uin)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case09_w_average.curve',
                    R,Uin)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case09_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[1,0].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[1,0].annotate(r'$\eta=2.2$',(0.1,0.75),fontsize=10)
#
ax[1,1].set_xlabel(r'$U_g/U_{g,\mathrm{in}}$')
ax[1,1].set_ylabel('$y/R$')
ax[1,1].axis([0, 1.4, -1, 1])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case10_w_average.curve',
                    R,Uin)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case10_w_average.curve',
                    R,Uin)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case10_w_average.curve',
                    R,Uin)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case10_w_average.csv',
                              dtype=float,
                              delimiter=',',
                              unpack=True)
ax[1,1].scatter(var_exp, pos_exp, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Tsuji and\nMorikawa (1982)')
ax[1,1].annotate(r'$\eta=2.8$',(0.1,0.75),fontsize=10)
ax[1,1].arrow(0.1, -0.6, 0, -0.25, head_width=0.035, head_length=0.08, fc='k', ec='k')
ax[1,1].annotate(r'$g$',(0.11,-0.75),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1982_horizontalPipe/Tsuji1982_horizontalPipe_allCases_uAverage.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(2,2)
#
ax[0,0].set_xlabel(r'$C_p/C_{p,\mathrm{mean}}$')
ax[0,0].set_ylabel('$y/R$')
ax[0,0].axis([0, 5, -1, 1])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(1))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case01_p_concentration.curve',
                    R,1)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case01_p_concentration.curve',
                    R,1)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case01_p_concentration.curve',
                    R,1)
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,0].annotate(r'$\eta=0.4$',(0.1,-0.9),fontsize=10)
ax[0,0].legend(loc='upper right')
#
ax[0,1].set_xlabel(r'$C_p/C_{p,\mathrm{mean}}$')
ax[0,1].set_ylabel('$y/R$')
ax[0,1].axis([0, 5, -1, 1])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(1))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case08_p_concentration.curve',
                    R,1)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case08_p_concentration.curve',
                    R,1)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case08_p_concentration.curve',
                    R,1)
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,1].annotate(r'$\eta=0.9$',(0.1,-0.9),fontsize=10)
#
ax[1,0].set_xlabel(r'$C_p/C_{p,\mathrm{mean}}$')
ax[1,0].set_ylabel('$y/R$')
ax[1,0].axis([0, 5, -1, 1])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(1))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case09_p_concentration.curve',
                    R,1)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case09_p_concentration.curve',
                    R,1)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case09_p_concentration.curve',
                    R,1)
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,0].annotate(r'$\eta=2.2$',(0.1,-0.9),fontsize=10)
#
ax[1,1].set_xlabel(r'$C_p/C_{p,\mathrm{mean}}$')
ax[1,1].set_ylabel('$y/R$')
ax[1,1].axis([0, 5, -1, 1])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(1))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case10_p_concentration.curve',
                    R,1)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case10_p_concentration.curve',
                    R,1)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case10_p_concentration.curve',
                    R,1)
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,1].annotate(r'$\eta=2.8$',(0.1,-0.9),fontsize=10)
ax[1,1].arrow(4.5, 0.9, 0, -0.25, head_width=0.15, head_length=0.08, fc='k', ec='k')
ax[1,1].annotate(r'$g$',(4.54,0.75),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1982_horizontalPipe/Tsuji1982_horizontalPipe_allCases_pConcentration.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------


fig, ax = plt.subplots(2,2)
#
ax[0,0].set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax[0,0].set_ylabel('$y/R$')
ax[0,0].axis([0.6, 1.4, -1, 1])
ax[0,0].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case01_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case01_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case01_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[0,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,0].annotate(r'$\eta=0.4$',(0.615,-0.9),fontsize=10)
ax[0,0].legend(loc='upper left')
#
ax[0,1].set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax[0,1].set_ylabel('$y/R$')
ax[0,1].axis([0.6, 1.4, -1, 1])
ax[0,1].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[0,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[0,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[0,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case08_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case08_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case08_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[0,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[0,1].annotate(r'$\eta=0.9$',(0.615,-0.9),fontsize=10)
#
ax[1,0].set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax[1,0].set_ylabel('$y/R$')
ax[1,0].axis([0.6, 1.4, -1, 1])
ax[1,0].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,0].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,0].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,0].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case09_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case09_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case09_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[1,0].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,0].annotate(r'$\eta=2.2$',(0.615,-0.9),fontsize=10)
#
ax[1,1].set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax[1,1].set_ylabel('$y/R$')
ax[1,1].axis([0.6, 1.4, -1, 1])
ax[1,1].xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax[1,1].xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax[1,1].yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax[1,1].yaxis.set_minor_locator(plt.MultipleLocator(0.25))
var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case10_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='1 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case10_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='--',
        label='2 way')
var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case10_mean_diameter.curve',
                    R,1)
varMean = np.mean(var)
var /= varMean
ax[1,1].plot(var, pos,
        color='black',
        linewidth=1,
        linestyle='-',
        label='4 way')
ax[1,1].annotate(r'$\eta=2.8$',(0.615,-0.9),fontsize=10)
ax[1,1].arrow(1.35, -0.6, 0, -0.25, head_width=0.03, head_length=0.08, fc='k', ec='k')
ax[1,1].annotate(r'$g$',(1.37,-0.75),fontsize=8)
#
fig.tight_layout(pad=0.01)
plt.savefig('Tsuji1982_horizontalPipe/Tsuji1982_horizontalPipe_allCases_meanDiameter.pdf',
            format='pdf')


#---------------------------------------------------------------------------------------
# Uin = 6.

# fig = plt.figure()
# gs = gridspec.GridSpec(nrows=2, ncols=4)

# #
# ax1 = fig.add_subplot(gs[0, :2])
# ax1.set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
# ax1.set_ylabel('$y/R$')
# ax1.axis([0.0, 1.6, -1, 1])
# ax1.xaxis.set_major_locator(plt.MultipleLocator(0.2))
# ax1.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
# ax1.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax1.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
# var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case12_w_average.curve',
#                     R,Uin)
# varMean = np.mean(var)
# var /= varMean
# ax1.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='-.',
#         label='1 way')
# var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case12_w_average.curve',
#                     R,Uin)
# varMean = np.mean(var)
# var /= varMean
# ax1.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='--',
#         label='2 way')
# var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case12_w_average.curve',
#                     R,Uin)
# varMean = np.mean(var)
# var /= varMean
# ax1.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='-',
#         label='4 way')
# var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case12_w_average.csv',
#                               dtype=float,
#                               delimiter=',',
#                               unpack=True)
# ax1.scatter(var_exp, pos_exp, s=20,
#             color='none',
#             marker='o',
#             edgecolor='black',
#             label='Tsuji and\nMorikawa (1982)')
# ax1.annotate(r'$\eta=0.4$',(0.615,-0.9),fontsize=10)
# ax1.legend(loc='upper left')
# #
# ax2 = fig.add_subplot(gs[0, 2:])
# ax2.set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
# ax2.set_ylabel('$y/R$')
# ax2.axis([0., 1.6, -1, 1])
# ax2.xaxis.set_major_locator(plt.MultipleLocator(0.2))
# ax2.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
# ax2.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax2.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
# var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case12_w_particle_average.curve',
#                     R,1)
# varMean = np.mean(var)
# var /= varMean
# ax2.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='-.',
#         label='1 way')
# var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case12_w_particle_average.curve',
#                     R,1)
# varMean = np.mean(var)
# var /= varMean
# ax2.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='--',
#         label='2 way')
# var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case12_w_particle_average.curve',
#                     R,1)
# varMean = np.mean(var)
# var /= varMean
# ax2.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='-',
#         label='4 way')
# var_exp, pos_exp = np.loadtxt('Tsuji1982_horizontalPipe/data/case12_w_particle_average.csv',
#                               dtype=float,
#                               delimiter=',',
#                               unpack=True)
# ax2.scatter(var_exp, pos_exp, s=20,
#             color='none',
#             marker='o',
#             edgecolor='black',
#             label='Tsuji and\nMorikawa (1982)')
# ax2.annotate(r'$\eta=0.9$',(0.615,-0.9),fontsize=10)
# #
# ax3 = fig.add_subplot(gs[1, 1:3])
# ax3.set_xlabel(r'$U_p/U_{g,\mathrm{in}}$')
# ax3.set_ylabel('$y/R$')
# ax3.axis([0.6, 1.4, -1, 1])
# ax3.xaxis.set_major_locator(plt.MultipleLocator(0.2))
# ax3.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
# ax3.yaxis.set_major_locator(plt.MultipleLocator(0.5))
# ax3.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
# var, pos = readData('Tsuji1982_horizontalPipe/data/1way_ke_tsuji_horizontal_case12_mean_diameter.curve',
#                     R,1)
# varMean = np.mean(var)
# var /= varMean
# ax3.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='-.',
#         label='1 way')
# var, pos = readData('Tsuji1982_horizontalPipe/data/2way_ke_tsuji_horizontal_case12_mean_diameter.curve',
#                     R,1)
# varMean = np.mean(var)
# var /= varMean
# ax3.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='--',
#         label='2 way')
# var, pos = readData('Tsuji1982_horizontalPipe/data/4way_ke_tsuji_horizontal_case12_mean_diameter.curve',
#                     R,1)
# varMean = np.mean(var)
# var /= varMean
# ax3.plot(var, pos,
#         color='black',
#         linewidth=1,
#         linestyle='-',
#         label='4 way')
# ax3.annotate(r'$\eta=2.2$',(0.615,-0.9),fontsize=10)
# #
# fig.tight_layout(pad=0.01)
# plt.savefig('Tsuji1982_horizontalPipe/Tsuji1982_horizontalPipe_case12_all.pdf',
#             format='pdf')