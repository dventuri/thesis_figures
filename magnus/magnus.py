import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
plt.style.use('default')
plt.style.use('oneHalfColumn.mplstyle')


# Rubinow and Keller (1961)
def rubKel():
    return 1

# Lun and Liu (1997)
def lunLiu(Re_p,Re_R):
    if (Re_p < 1):
        Cl = rubKel()
    else:
        Cl = rubKel()*(0.178 + 0.822*Re_p**(-0.522))
    return Cl

# Oesterlé and Dinh (1998)
def oesBui(Re_p,Re_R):
    Cl = 0.45*Re_p/Re_R + (rubKel() - 0.45**Re_p/Re_R)*np.exp(-0.05684*((Re_R/Re_p)**0.4)*(Re_p**0.7))
    return Cl

# Loth (2008)
def loth(Re_p,Re_R):
    Cl = rubKel() - (0.675 + 0.15*(1 + np.tanh(0.28*(Re_R/Re_p-2))))*np.tanh(0.18*np.sqrt(Re_p))
    return Cl


# Linecolors
colors = ['black','#5c6068','#a3acb9']

# Plot fixed Re_p, varying Re_R/Re_p
fig, ax = plt.subplots()
ax.set_ylabel('$C_{LR}$')
ax.set_xlabel('$\mathrm{Re}_R/\mathrm{Re}_p$')
ax.axis([0.1, 20, 0, 1.2])

i = 0
Rep_list = [5,20,100]
ReR_over_Rep_list = np.linspace(0.1,20,1000)

for Re_p in Rep_list:
    j = 0
    Clr_LL = np.zeros(len(ReR_over_Rep_list))
    Clr_OB = np.zeros(len(ReR_over_Rep_list))
    Clr_LO = np.zeros(len(ReR_over_Rep_list))

    for ReR_over_Rep in ReR_over_Rep_list:
        Re_R = ReR_over_Rep*Re_p
        Clr_LL[j] = lunLiu(Re_p, Re_R)
        Clr_OB[j] = oesBui(Re_p, Re_R)
        Clr_LO[j] = loth(Re_p, Re_R)
        j += 1

    ax.semilogx(ReR_over_Rep_list, Clr_LL,
                color=colors[i], linestyle='-')
    ax.semilogx(ReR_over_Rep_list, Clr_OB,
                color=colors[i], linestyle='--')
    ax.semilogx(ReR_over_Rep_list, Clr_LO,
                color=colors[i], linestyle=':')
    i += 1

ax.annotate(r'$\mathrm{Re}_p = 5$',(11,0.7),
            fontsize=10,
            color=colors[0])
ax.annotate(r'$\mathrm{Re}_p = 20$',(10,0.38),
            fontsize=10,
            color=colors[1])
ax.annotate(r'$\mathrm{Re}_p = 100$',(9,0.105),
            fontsize=10,
            color=colors[2])

#first legend
line2 = mlines.Line2D([], [], color='black', linestyle='-',
                      label='Lun and Liu (1997)')
line3 = mlines.Line2D([], [], color='black', linestyle='--',
                      label='Oesterlé and Dinh (1998)')
line4 = mlines.Line2D([], [], color='black', linestyle=':',
                      label='Loth (2008)')
first_legend = plt.legend(handles=[line2, line3, line4],
                          loc='upper left',
                          frameon=True,
                          framealpha=1)

ax = plt.gca().add_artist(first_legend)

fig.tight_layout(pad=0.01)
plt.savefig('magnus/magnus.pdf',
            format='pdf')
