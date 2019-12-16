import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')


opts = {'dtype': float,
        'delimiter': ',',
        'unpack': True,
        'usecols': (0, 1)}
opts2 = {'dtype': float,
         'delimiter': ' ',
         'unpack': True,
         'usecols': (0, 1),
         'skiprows': 2}


# simulation: average
r1_ke, up1_ke = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/ke_1way_analit_19630_avg.curve', **opts2)
r2_ke, up2_ke = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/ke_2way_analit_19630_avg.curve', **opts2)
r4_ke, up4_ke = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/ke_4way_analit_19630_avg.curve', **opts2)
r1_ke_rk2, up1_ke_rk2 = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/ke_1way_rk2_19630_avg.curve', **opts2)
r1_ke_coarse, up1_ke_coarse = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/ke_1way_analit_coarse_19630_avg.curve', **opts2)
# experimental data
up, r = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/exp_avg.csv', **opts)
# simulation: average
r1_rsm, up1_rsm = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/1wayRSM_avg.curve', **opts2)
up2_rsm, r2_rsm = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/2wayRSM_avg_18000.csv', **opts)
up4_rsm, r4_rsm = np.loadtxt('Huber1998_pipe_case3/p_diameter/data/4wayRSM_avg_18000.csv', **opts)
# normalization of data
up1_ke = up1_ke/40e-6
r1_ke = (r1_ke-0.075)/(0.075)
up2_ke = up2_ke/40e-6
r2_ke = (r2_ke-0.075)/0.075
up4_ke = up4_ke/40e-6
r4_ke = (r4_ke-0.075)/0.075
up1_ke_rk2 = up1_ke_rk2/40e-6
r1_ke_rk2 = (r1_ke_rk2-0.075)/(0.075)
up1_ke_coarse = up1_ke_coarse/40e-6
r1_ke_coarse = (r1_ke_coarse-0.075)/(0.075)
up1_rsm = up1_rsm/40e-6
r1_rsm = (r1_rsm-0.075)/(0.075)


plt.style.use('oneHalfColumn.mplstyle')

# Particle diameter - ke
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax.axis([0.4, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(up1_ke, r1_ke,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Sim. 1 way')
ax.plot(up2_ke, r2_ke,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Sim. 2 way')
ax.plot(up4_ke, r4_ke,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Sim. 4 way')
ax.scatter(up, r, s=20,
           color='black',
           marker='o',
           edgecolor='black',
           label='Exp. average')
ax.legend(title=r'$k$-$\varepsilon$',loc='upper left')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/p_diameter/Huber1998_pipe_case3_KE_partDiam.pdf',
            format='pdf')

# Particle diameter - RSM
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax.axis([0.4, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(up1_rsm, r1_rsm,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Sim. 1 way')
ax.plot(up2_rsm, r2_rsm,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Sim. 2 way')
ax.plot(up4_rsm, r4_rsm,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Sim. 4 way')
ax.scatter(up, r, s=20,
           color='black',
           marker='o',
           edgecolor='black',
           label='Exp. average')
ax.legend(title='RSM',loc='upper left')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/p_diameter/Huber1998_pipe_case3_RSM_partDiam.pdf',
            format='pdf')

# Particle diameter - KE vs RSM
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax.axis([0.4, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(up4_ke, r4_ke,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Sim. $k$-$\\varepsilon$')
ax.plot(up4_rsm, r4_rsm,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Sim. RSM')
ax.scatter(up, r, s=20,
           color='black',
           marker='o',
           edgecolor='black',
           label='Exp. average')
ax.legend(title='4 way',loc='upper left')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/p_diameter/Huber1998_pipe_case3_KEvsRSM_partDiam.pdf',
            format='pdf')

# Particle diameter - ke - particle integration - mesh size
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax.axis([0.4, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(up1_ke, r1_ke,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Analytic')
ax.plot(up1_ke_rk2, r1_ke_rk2,
        color='black',
        linewidth=1,
        linestyle=':',
        label='RK2')
ax.plot(up1_ke_coarse, r1_ke_coarse,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Coarse grid')
ax.legend(title=r'1 way $k$-$\varepsilon$',loc='upper left')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/p_diameter/Huber1998_pipe_case3_KE_analiticVsRK2_meshSize_partDiam.pdf',
            format='pdf')

# Particle velocity - ke - mesh size
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$d_p/d_{p,\mathrm{mean}}$')
ax.axis([0.8, 1.3, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(up1_ke, r1_ke,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Fine grid')
ax.plot(up1_ke_coarse, r1_ke_coarse,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Coarse grid')
ax.legend(title=r'1 way $k$-$\varepsilon$',loc='upper left')
ax.arrow(1.25, -0.6, 0, -0.25, head_width=0.02, head_length=0.08, fc='k', ec='k')
ax.annotate(r'$g$',(1.26,-0.75),fontsize=12)
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/p_diameter/Huber1998_pipe_case3_KE_meshSize_partDiam.pdf',
            format='pdf')
