import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

R = 0.063/2.0
Uin = 20.

plt.style.use('oneHalfColumn.mplstyle')

# Fluid velocity
this = 'Lain2012_pipe/data/2way_ke_lain2012pipe_012000_w_average.curve'
pos_this, var_this = np.loadtxt(this,
                                skiprows=2,
                                delimiter=' ',
                                unpack=True)
lain = 'Lain2012_pipe/data/2way_ke_lain2012pipe_w_average.csv'
var_lain, pos_lain = np.loadtxt(lain,
                                skiprows=0,
                                delimiter=',',
                                unpack=True)
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_g/U_{g,in}$')
ax.axis([0, 1.2, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(var_this/Uin, (pos_this-R)/R,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work')
ax.plot(var_lain, pos_lain,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Laín and Sommerfeld (2012)')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Lain2012_pipe/Lain2012_2way_gasVel.pdf',
            format='pdf')

this = 'Lain2012_pipe/data/4way_ke_lain2012pipe_012000_w_average.curve'
pos_this, var_this = np.loadtxt(this,
                                skiprows=2,
                                delimiter=' ',
                                unpack=True)
lain = 'Lain2012_pipe/data/4way_ke_lain2012pipe_w_average.csv'
var_lain, pos_lain = np.loadtxt(lain,
                                skiprows=0,
                                delimiter=',',
                                unpack=True)
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_g/U_{g,in}$')
ax.axis([0, 1.2, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(var_this/Uin, (pos_this-R)/R,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work')
ax.plot(var_lain, pos_lain,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Laín and Sommerfeld (2012)')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Lain2012_pipe/Lain2012_4way_gasVel.pdf',
            format='pdf')


# Particle velocity
this = 'Lain2012_pipe/data/2way_ke_lain2012pipe_012000_w_particle_average.curve'
pos_this, var_this = np.loadtxt(this,
                                skiprows=2,
                                delimiter=' ',
                                unpack=True)
lain = 'Lain2012_pipe/data/2way_ke_lain2012pipe_w_particle_average.csv'
var_lain, pos_lain = np.loadtxt(lain,
                                skiprows=0,
                                delimiter=',',
                                unpack=True)
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_p/U_{g,in}$')
ax.axis([0, 1.2, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(var_this/Uin, (pos_this-R)/R,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work')
ax.plot(var_lain, pos_lain,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Laín and Sommerfeld (2012)')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Lain2012_pipe/Lain2012_2way_partVel.pdf',
            format='pdf')

this = 'Lain2012_pipe/data/4way_ke_lain2012pipe_012000_w_particle_average.curve'
pos_this, var_this = np.loadtxt(this,
                                skiprows=2,
                                delimiter=' ',
                                unpack=True)
lain = 'Lain2012_pipe/data/4way_ke_lain2012pipe_w_particle_average.csv'
var_lain, pos_lain = np.loadtxt(lain,
                                skiprows=0,
                                delimiter=',',
                                unpack=True)
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_p/U_{g,in}$')
ax.axis([0, 1.2, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(var_this/Uin, (pos_this-R)/R,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work')
ax.plot(var_lain, pos_lain,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Laín and Sommerfeld (2012)')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Lain2012_pipe/Lain2012_4way_partVel.pdf',
            format='pdf')


# Gas phase turbulence energy
this = 'Lain2012_pipe/data/2way_ke_lain2012pipe_TKE.curve'
pos_this, var_this = np.loadtxt(this,
                                skiprows=2,
                                delimiter=' ',
                                unpack=True)
lain = 'Lain2012_pipe/data/2way_ke_lain2012pipe_TKE.csv'
var_lain, pos_lain = np.loadtxt(lain,
                                skiprows=0,
                                delimiter=',',
                                unpack=True)
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$k/U_{g,in}^2$')
ax.axis([0, 0.01, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.002))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.0005))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(var_this/(Uin**2), (pos_this-R)/R,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work')
ax.plot(var_lain, pos_lain,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Laín and Sommerfeld (2012)')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Lain2012_pipe/Lain2012_2way_TKE.pdf',
            format='pdf')

this = 'Lain2012_pipe/data/4way_ke_lain2012pipe_TKE.curve'
pos_this, var_this = np.loadtxt(this,
                                skiprows=2,
                                delimiter=' ',
                                unpack=True)
lain = 'Lain2012_pipe/data/4way_ke_lain2012pipe_TKE.csv'
var_lain, pos_lain = np.loadtxt(lain,
                                skiprows=0,
                                delimiter=',',
                                unpack=True)
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$k/U_{g,in}^2$')
ax.axis([0, 0.01, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.002))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.0005))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(var_this/Uin**2, (pos_this-R)/R,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Present work')
ax.plot(var_lain, pos_lain,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Laín and Sommerfeld (2012)')
ax.legend(loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Lain2012_pipe/Lain2012_4way_TKE.pdf',
            format='pdf')

