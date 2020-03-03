import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
plt.style.use('default')

def stokes(Rep):
    Cd = 24/Rep
    return Cd

def schillerNaumann(Rep):
    st = stokes(Rep)
    if (Rep < 1000):
        Cd = st*(1 + 0.15*Rep**0.687)
    else:
        Cd = 0.44
    return Cd

def morsiAlexander(Rep):
    if (Rep < 0.1):
        a = [0,24,0]
    elif (Rep < 1):
        a = [3.69,22.73,0.0903]
    elif (Rep < 10):
        a = [1.222,29.1667,-3.8889]
    elif (Rep < 100):
        a = [0.6167,46.5,-116.67]
    elif (Rep < 1000):
        a = [0.3644,98.33,-2778]
    elif (Rep < 5000):
        a = [0.357,148.62,-47500]
    elif (Rep < 10000):
        a = [0.46,-490.546,578700]
    else:
        a = [0.5191,-1662.5,5416700]
    Cd = a[0] + a[1]/Rep + a[2]/Rep**2
    return Cd

def haiderLevenspiel(Rep):
    st = stokes(Rep)
    Cd = st*(1.0 + 0.1806*Rep**0.687 + (0.0175*Rep)/(1.0 + 4.25e4/(Rep**1.16)))
    return Cd

def coelhoMassarani(Rep):
    st = stokes(Rep)
    Cd = (st**0.63 + 0.43**0.63)**(1./0.63)
    return Cd

def tennetiDesjardins(Rep,alpha):
    st = stokes(Rep*alpha)
    Cd0 = schillerNaumann(Rep*alpha)/alpha**2
    Cd1 = 5.81*(1-alpha)/alpha**2 + 0.48*(1-alpha)**(1/3)/alpha**3
    Cd2 = alpha*(1-alpha)**3*(alpha*Rep)*(0.95 + 0.61*(1-alpha)**3/alpha**2)
    Cd = Cd0 + st*Cd1 + st*Cd2
    return Cd


#Regular drag

Rep = np.linspace(1e-1,2e3,20000)

vectfunc = np.vectorize(stokes, otypes=[np.float])
Cd_ST = vectfunc(Rep)

vectfunc = np.vectorize(schillerNaumann, otypes=[np.float])
Cd_SN = vectfunc(Rep)

vectfunc = np.vectorize(morsiAlexander, otypes=[np.float])
Cd_MA = vectfunc(Rep)

vectfunc = np.vectorize(haiderLevenspiel, otypes=[np.float])
Cd_HL = vectfunc(Rep)

vectfunc = np.vectorize(coelhoMassarani, otypes=[np.float])
Cd_CM = vectfunc(Rep)


plt.style.use('../oneHalfColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_ylabel(r'$C_D$')
ax.set_xlabel(r'$\mathrm{Re}_p$')
ax.axis([1e0, 2e3, 4e-1, 3e1])
ax.loglog(Rep, Cd_ST,
          color='gray',
          linewidth=1,
          linestyle='--')
ax.loglog(Rep, Cd_SN,
          color='black',
          linewidth=1,
          linestyle='-',
          label='Schiller and Naumann (1935)')
ax.loglog(Rep, Cd_MA,
          color='black',
          linewidth=1,
          linestyle='--',
          label='Morsi and Alexander (1972)')
ax.loglog(Rep, Cd_HL,
          color='black',
          linewidth=1,
          linestyle=':',
          label='Haider and Levenspiel (1989)')
ax.loglog(Rep, Cd_CM,
          color='black',
          linewidth=1,
          linestyle='-.',
          label='Coelho and Massarani (1996)')
ax.annotate("Stokes drag",(5,1),
            fontsize=10,
            color='gray')
plt.legend(frameon=True,framealpha=1)
fig.tight_layout(pad=0.01)
plt.savefig('./drag_dilute.pdf',
            format='pdf')


#Modified drag

alpha = 0.90
Rep = np.linspace(1e-5,800,100000)

Cd_ST = []; Cd_SN = []; Cd_TD = [];

vectfunc = np.vectorize(stokes, otypes=[np.float])
Cd_ST = vectfunc(Rep)

vectfunc = np.vectorize(schillerNaumann, otypes=[np.float])
Cd_SN = vectfunc(Rep)

vectfunc = np.vectorize(tennetiDesjardins, otypes=[np.float])
Cd_TD = vectfunc(Rep,alpha)

plt.style.use('../oneHalfColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_ylabel(r'$F_D/F_{D,\mathrm{Stokes}}$')
ax.set_xlabel(r'$\mathrm{Re}_{p,\alpha}$')
ax.axis([0, 300, 0, 40])
ax.yaxis.set_minor_locator(MultipleLocator(2.5))
ax.plot(Rep, Cd_SN/Cd_ST,
          color='black',
          linewidth=1,
          linestyle='-',
          label='Schiller and Naumann (1935)')
ax.plot(Rep*alpha, Cd_TD*alpha**2/Cd_ST,
          color='black',
          linewidth=1,
          linestyle='--',
          label='Tenneti et al. (2011)')

alpha = 0.70

Cd_TD = []

vectfunc = np.vectorize(tennetiDesjardins, otypes=[np.float])
Cd_TD = vectfunc(Rep,alpha)

ax.plot(Rep*alpha, Cd_TD*alpha**2/Cd_ST,
          color='black',
          linewidth=1,
          linestyle='--')

alpha = 0.50

Cd_TD = []

vectfunc = np.vectorize(tennetiDesjardins, otypes=[np.float])
Cd_TD = vectfunc(Rep,alpha)

ax.plot(Rep*alpha, Cd_TD*alpha**2/Cd_ST,
          color='black',
          linewidth=1,
          linestyle='--')

ax.annotate(r'$\alpha_g = 0.9$',(265,11.5),
            fontsize=10,
            color='black')
ax.annotate(r'$\alpha_g = 0.7$',(265,20),
            fontsize=10,
            color='black')
ax.annotate(r'$\alpha_g = 0.5$',(265,37),
            fontsize=10,
            color='black')

plt.legend(frameon=True,framealpha=1,loc='upper left')
fig.tight_layout(pad=0.01)
plt.savefig('./drag_dense.pdf',
            format='pdf')
