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
r1_ke, up1_ke = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/1wayKE_avg.curve', **opts2)
up2_ke, r2_ke = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/2wayKE_avg_24000.csv', **opts)
r2_ke_rk2, up2_ke_rk2 = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/2way_v2.2.5_vel.curve', **opts2)
up4_ke, r4_ke = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/4wayKE_avg_24000.csv', **opts)
r4_ke_rk2, up4_ke_rk2 = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/4way_v2.2.5_vel.curve', **opts2)
# simulation: rms
rf1_ke, uf1_ke = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/1wayKE_rms.curve', **opts2)
rf2_ke, uf2_ke = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/2wayKE_rms_24000.curve', **opts2)
rf4_ke, uf4_ke = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/4wayKE_rms_24000.curve', **opts2)
# experimental data
up, r = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/exp_avg.csv', **opts)
uf, rf = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/exp_rms.csv', **opts)
# simulation: average
r1_rsm, up1_rsm = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/1wayRSM_avg.curve', **opts2)
up2_rsm, r2_rsm = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/2wayRSM_avg_18000.csv', **opts)
up4_rsm, r4_rsm = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/4wayRSM_avg_18000.csv', **opts)
# simulation: rms
rf1_rsm, uf1_rsm = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/1wayRSM_rms.curve', **opts2)
rf2_rsm, uf2_rsm = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/2wayRSM_rms_18000.curve', **opts2)
rf4_rsm, uf4_rsm = np.loadtxt('Huber1998_pipe_case3/partVelocity/data/4wayRSM_rms_18000.curve', **opts2)
# normalization of data
up1_ke = up1_ke/27
r1_ke = (r1_ke-0.075)/(0.075)
up2_ke_rk2 = up2_ke_rk2/27
r2_ke_rk2 = (r2_ke_rk2-0.075)/0.075
up4_ke_rk2 = up4_ke_rk2/27
r4_ke_rk2 = (r4_ke_rk2-0.075)/0.075
uf1_ke = uf1_ke/27
rf1_ke = (rf1_ke-0.075)/(0.075)
uf2_ke = uf2_ke/27
rf2_ke = (rf2_ke-0.075)/(0.075)
uf4_ke = uf4_ke/27
rf4_ke = (rf4_ke-0.075)/(0.075)
up1_rsm = up1_rsm/27
r1_rsm = (r1_rsm-0.075)/(0.075)
uf1_rsm = uf1_rsm/27
rf1_rsm = (rf1_rsm-0.075)/(0.075)
uf2_rsm = uf2_rsm/27
rf2_rsm = (rf2_rsm-0.075)/(0.075)
uf4_rsm = uf4_rsm/27
rf4_rsm = (rf4_rsm-0.075)/(0.075)


plt.style.use('oneHalfColumn.mplstyle')

# Particle velocity - ke
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_p/U_{p,avg}$')
ax.axis([0, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
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
ax.plot(uf1_ke, rf1_ke,
        color='black',
        linewidth=1,
        linestyle='-.')
ax.plot(uf2_ke, rf2_ke,
        color='black',
        linewidth=1,
        linestyle='--')
ax.plot(uf4_ke, rf4_ke,
        color='black',
        linewidth=1,
        linestyle='-')
ax.scatter(up, r, s=20,
           color='black',
           marker='o',
           edgecolor='black',
           label='Exp. average')
ax.scatter(uf, rf, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Exp. RMS')
ax.legend(title=r'$k$-$\varepsilon$',loc='best')
ax.arrow(1.3, -0.5, 1.3, -0.9, head_width=0.05, head_length=0.1, fc='k', ec='k')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/partVelocity/Huber1998_pipe_case3_KE_partVel.pdf',
            format='pdf')

# Particle velocity - RSM
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_p/U_{p,avg}$')
ax.axis([0, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
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
ax.plot(uf1_rsm, rf1_rsm,
        color='black',
        linewidth=1,
        linestyle='-.')
ax.plot(uf2_rsm, rf2_rsm,
        color='black',
        linewidth=1,
        linestyle='--')
ax.plot(uf4_rsm, rf4_rsm,
        color='black',
        linewidth=1,
        linestyle='-')
ax.scatter(up, r, s=20,
           color='black',
           marker='o',
           edgecolor='black',
           label='Exp. average')
ax.scatter(uf, rf, s=20,
           color='none',
           marker='o',
           edgecolor='black',
           label='Exp. RMS')
ax.legend(title='RSM',loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/partVelocity/Huber1998_pipe_case3_RSM_partVel.pdf',
            format='pdf')


# Particle velocity - ke - Particle integration
fig, ax = plt.subplots()
ax.set_ylabel(r'$y/R$')
ax.set_xlabel(r'$U_p/U_{p,avg}$')
ax.axis([0, 1.4, -1, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.plot(up2_ke, r2_ke,
        color='black',
        linewidth=1,
        linestyle='--',
        label='Sim. 2 way - Analytic')
ax.plot(up2_ke_rk2, r2_ke_rk2,
        color='black',
        linewidth=1,
        linestyle=':',
        label='Sim. 2 way - RK2')
ax.plot(up4_ke, r4_ke,
        color='black',
        linewidth=1,
        linestyle='-',
        label='Sim. 4 way - Analytic')
ax.plot(up4_ke_rk2, r4_ke_rk2,
        color='black',
        linewidth=1,
        linestyle='-.',
        label='Sim. 4 way - RK2')
ax.scatter(up, r, s=20,
           color='black',
           marker='o',
           edgecolor='black',
           label='Exp. average')
ax.legend(title=r'$k$-$\varepsilon$',loc='best')
fig.tight_layout(pad=0.01)
plt.savefig('Huber1998_pipe_case3/partVelocity/Huber1998_pipe_case3_KE_analiticVsRK2_partVel.pdf',
            format='pdf')
