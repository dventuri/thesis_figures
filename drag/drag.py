import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

# DISCLAIMER
#  Here, we are considering the context of the UNSCYFL3D code, where the drag
#  force (F_D) is given by F_D = rho/2*A_p*C_D*|Ur|*Ur. So, the new C_D
#  (modified by population effects) must carry all effects of \alpha.
#  Note that some correlations define the drag force differently, such as
#  F_D = rho/2*A_p*C_D*|Ur|*Ur*\alpha**2, so that must also be taken into
#  account.


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


plt.style.use('oneHalfColumn.mplstyle')
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
plt.savefig('drag/drag_dilute.pdf',
            format='pdf')




# import os
# import numpy as np
# import matplotlib.pyplot as plt
# from cycler import cycler

# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#               cycler('linestyle', ['-', '--', ':', '-.']))
# plt.rc('axes', prop_cycle=monochrome)

# plt.style.use(os.path.join(os.environ['HOME'],
#               'Templates',
#               'matplotlib',
#               'doubleColumn.mplstyle'))

# def dallavalle(Rep):
#     Cd = (0.63 + 4.8/Rep**0.5)**2
#     return Cd

# def diFelice(Rep,alpha):
#     x = np.log10(alpha*Rep)
#     beta = 3.7 - 0.65*np.exp(-0.5*(1.5-x)**2)
#     g = alpha**(-beta)
#     Cd = dallavalle(alpha*Rep)*g
#     return alpha**2*Cd

# #def diFelice(Rep,alpha):
# #    x = np.log10(Rep)
# #    beta = 3.7 - 0.65*np.exp(-0.5*(1.5-x)**2)
# #    g = alpha**(-beta)
# #    Cd = dallavalle(Rep)*g
# #    return Cd

# def tenneti(Rep,alpha):
#     st = stokes(Rep*alpha)
#     Cd0 = schillerNaumann(Rep*alpha)/alpha**3
#     Cd1 = 5.81*(1-alpha)/alpha**3 + 0.48*(1-alpha)**(1/3)/alpha**4
#     Cd2 = (1-alpha)**3*(alpha*Rep)*(0.95 + 0.61*(1-alpha)**3/alpha**2)
#     Cd = Cd0 + st*Cd1 + st*Cd2
#     return alpha**2*Cd

# def tennetiDesjardins(Rep,alpha):
#     st = stokes(Rep*alpha)
#     Cd0 = schillerNaumann(Rep*alpha)/alpha**3
#     Cd1 = 5.81*(1-alpha)/alpha**3 + 0.48*(1-alpha)**(1/3)/alpha**4
#     Cd2 = (1-alpha)**3*(alpha*Rep)*(0.95 + 0.61*(1-alpha)**3/alpha**2)
#     Cd = Cd0 + st*Cd1 + st*Cd2
#     return alpha**3*Cd

# def wenYu(Rep,alpha):
#     Cd0 = schillerNaumann(alpha*Rep)
#     Cd = Cd0*alpha**(-3.65)
#     return alpha**2*Cd

# def ergunWenYu(Rep,alpha): #from Beetstra
#     if (alpha<0.8):
#         F = 200*(1-alpha)/(Rep*alpha) + 7/3*1/alpha
#     else:
#         F = schillerNaumann(Rep)*alpha**(-2.65)
#     return F

# def ergunWenYu2(Rep,alpha): #from Yang
#     if (alpha<0.8):
#         F = 200*(1-alpha)/(Rep*alpha) + 7/3*1/alpha
#     else:
#         F = schillerNaumann(Rep)*alpha**(-2.65)*(1-alpha)
#     return F

# def beetstra(Rep,alpha):
#     al2 = alpha**2
#     am1 = 1-alpha
#     alInv = 1/alpha
#     F = 10*am1/al2 + al2*(1 + 1.5*np.sqrt(am1)) + 0.413*Rep/(24*al2)* \
#     (alInv + 3*alpha*am1 + 8.4*Rep**(-0.343))/ \
#     (1 + 10**(3*am1)*Rep**(-0.5 - 2*am1))
#     return alpha*F*stokes(Rep)

# #needs checking
# #def emms(Rep,alpha):
# #    if (alpha>0.9997):
# #        a = 1
# #        b = 0
# #        c = 0
# #    elif (alpha>0.99):
# #        a = 0.4243 + 0.88/(1+np.exp(-(alpha-0.9942)/0.00218))*(1-1/(1+np.exp(-(alpha-0.9989)/0.00003)))
# #        b = 0.01661 + 0.2436*np.exp(-0.5*((alpha-0.9985)/0.00191)**2)
# #        c = 0.0825 - 0.0574*np.exp(-0.5*((alpha-0.9979)/0.00703)**2)
# #    elif (alpha>0.545):
# #        a = (2124.956 - 2142.3*alpha)**(-0.4896)
# #        b = (0.8223 - 0.1293*alpha)**(13.0310)
# #        c = (alpha-1.0013)/(-0.06633+9.1391*(alpha-1.0013)+6.9231*(alpha-1.0013)**2)
# #    elif (alpha>0.46):
# #        a = 0.0320 + 0.7399/(1+(alpha/0.4912)**(54.4265))
# #        b = 0.00225 + 772.0074/(1+10**(66.3224*(alpha-0.3987))) + 0.02404/(1+10**(53.8948*(0.5257-alpha)))
# #        c = 0.1705 - 0.1731/(1+(alpha/0.5020)**37.7091)
# #    elif (alpha>0.4):
# #        a = 0.8526 - 0.5846/(1+(alpha/0.4325)**22.6279)
# #        b = 0
# #        c = 0
# #    else:
# #        print('error')
# #
# #    Hd = a*(Rep*alpha + b)**c
# #    Cd = schillerNaumann(Rep*alpha)*alpha**(-1.7)*Hd
# #    return Cd

# def emms(Rep,alpha):
#     if (alpha>(1-0.006304)):
#         Hd = 1
#     elif (alpha>(1-0.472331)):
#         Hd = 0.00818*(1-alpha)**(-0.94858)
#     elif (alpha>(1-0.562782)):
#         Hd = np.exp(51.82637-255.75154*(1-alpha)+290.80887*(1-alpha)**2)
#     else:
#         Hd = 1

#     Cd = schillerNaumann(Rep)*alpha**(-2.7)*Hd
#     return Cd

# #def emms(Rep,alpha):
# #    if (alpha>0.97):
# #        Hd = -31.8295 + 32.8295*alpha
# #    elif (alpha>0.82):
# #        Hd = -0.0101 + 0.0038/(4*(alpha - 0.7789)**2 + 0.0040)
# #    elif (alpha>0.74):
# #        Hd = -0.5760 + 0.0214/(4*(alpha - 0.7463)**2 + 0.0044)
# #    else:
# #        Hd = 7/3 + 200/(Rep*alpha)*(1-alpha)
# #        Hd = Hd/schillerNaumann(Rep*alpha)
# #        Hd = Hd/alpha
# #
# #    Cd = schillerNaumann(Rep*alpha)*Hd*alpha
# #    return Cd

# def gidaspow(Rep,alpha):
#     Cd = schillerNaumann(Rep*alpha)*alpha**(-1.65)
#     return Cd


# #alpha = 1-0.022
# alpha = 0.83
# Rep = np.linspace(1e-1,2e3,20000)

# Cd_ST = []; Cd_SN = []; Cd_CM = [];
# Cd_HL = []; Cd_MA = []; Cd_DA = [];
# Cd_DF = []; Cd_TE = []; Cd_TD = [];
# Cd_WY = []; Cd_EW = []; Cd_BE = [];
# Cd_EM = []; Cd_GD = [];

# vectfunc = np.vectorize(stokes, otypes=[np.float])
# Cd_ST = vectfunc(Rep)

# vectfunc = np.vectorize(schillerNaumann, otypes=[np.float])
# Cd_SN = vectfunc(Rep)

# vectfunc = np.vectorize(tennetiDesjardins, otypes=[np.float])
# Cd_TD = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(ergunWenYu, otypes=[np.float])
# Cd_EW = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(beetstra, otypes=[np.float])
# Cd_BE = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(emms, otypes=[np.float])
# Cd_EM = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(gidaspow, otypes=[np.float])
# Cd_GD = vectfunc(Rep,alpha)


# # plot Cd standard
# plt.figure()
# #plt.loglog(Rep,Cd_ST,label='Stokes')
# plt.loglog(Rep,Cd_SN,label='Schiller and Naumann')
# plt.loglog(Rep,Cd_TD,label='Tenneti (Desjardis)')
# plt.loglog(Rep,Cd_EW,label='Ergun/Wen and Yu')
# #plt.loglog(Rep,Cd_BE,label='Beetstra')
# plt.loglog(Rep,Cd_EM,label='EMMS')
# #plt.loglog(Rep,Cd_GD,label='Gidaspow')
# plt.xlim([0.1,2000])
# plt.grid(linestyle='--')
# plt.legend(frameon=True,framealpha=1)
# plt.xlabel(r'$Re_p$')
# plt.ylabel(r'$C_D$')
# #plt.savefig('cd_re.png', dpi=1200, format='png')


### CONFERIR
# Plot F/Fstokes, or Cd/Cd_stokes
#plt.figure()
#plt.plot(Rep*alpha,Cd_SN/Cd_ST,label='Schiller and Naumann')
#plt.plot(Rep*alpha,Cd_TD/Cd_ST,label='Tenneti (Desjardins)')
#plt.plot(Rep*alpha,Cd_WY/alpha**2/Cd_ST_ALPHA,label='Wen and Yu')
#plt.plot(Rep*alpha,Cd_EM/alpha**2/Cd_ST_ALPHA,label='EMMS')
#plt.plot(Rep*alpha,Cd_BE/Cd_ST_ALPHA,label='Beetstra')
#plt.xlim([0,1000])
#plt.ylim([1,60])
#plt.yticks([5,10,15,20,25,30,35])
#plt.grid(linestyle='--')
#plt.legend(frameon=True,framealpha=1)
#plt.xlabel(r'$Re_{p,\alpha}$')
#plt.ylabel(r'$F$')
#plt.savefig('f_re.png', dpi=1200, format='png')


#Funtion of \alpha
# Rep = 100
# alpha = np.linspace(0.6,1,1000)

# Cd_ST = []; Cd_SN = []; Cd_CM = [];
# Cd_HL = []; Cd_MA = []; Cd_DA = [];
# Cd_DF = []; Cd_TE = []; Cd_TD = [];
# Cd_WY = []; Cd_EW = []; Cd_BE = [];
# Cd_EM = []; Cd_GD = [];

# Cd_ST = stokes(Rep)

# Cd_SN = schillerNaumann(Rep)

# vectfunc = np.vectorize(tennetiDesjardins, otypes=[np.float])
# Cd_TD = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(ergunWenYu, otypes=[np.float])
# Cd_EW = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(beetstra, otypes=[np.float])
# Cd_BE = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(emms, otypes=[np.float])
# Cd_EM = vectfunc(Rep,alpha)

# vectfunc = np.vectorize(gidaspow, otypes=[np.float])
# Cd_GD = vectfunc(Rep,alpha)


# # plot Cd standard
# plt.figure()
# #plt.plot(alpha,Cd_ST,label='Stokes')
# #plt.plot(alpha,Cd_SN,label='Schiller and Naumann')
# plt.semilogy(alpha,Cd_TD/Cd_SN,label='Tenneti (Desjardis)')
# plt.semilogy(alpha,Cd_EW/Cd_SN,label='Ergun/Wen and Yu')
# plt.semilogy(alpha,Cd_BE/Cd_SN,label='Beetstra')
# plt.semilogy(alpha,Cd_EM/Cd_SN,label='EMMS')
# #plt.semilogy(alpha,Cd_GD,label='Gidaspow')
# plt.xlim([0.6,1])
# #plt.ylim([0.5,20])
# plt.grid(linestyle='--')
# plt.legend(frameon=True,framealpha=1)
# plt.xlabel(r'$Re_p$')
# plt.ylabel(r'$C_D$')
# #plt.savefig('cd_re.png', dpi=1200, format='png')
