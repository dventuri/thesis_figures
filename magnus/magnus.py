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

# Oesterlé and Bui Dinh (1998)
def oesBui(Re_p,Re_R):
    Cl = 0.45*Re_p/Re_R + (rubKel() - 0.45**Re_p/Re_R)*np.exp(-0.056839*(Re_R**0.4)*(Re_p**0.3))
    return Cl

# Loth (2008)
def loth(Re_p,TwoOmega):
    Cl = rubKel() - (0.675 + 0.15*(1 + np.tanh(0.28*(Re_R/Re_p-2))))*np.tanh(0.18*np.sqrt(Re_p))
    return Cl


# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40),
             (148, 103, 189), (140, 86, 75), (227, 119, 194), (127, 127, 127),
             (188, 189, 34), (23, 190, 207)]


# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)


# Plot fixed Re_p, varying TwoOmega
fig, ax = plt.subplots()
ax.set_ylabel('$C_{LR}$')
ax.set_xlabel('$\mathrm{Re}_R/\mathrm{Re}_p$')
# ax.axis([1e0, 2e3, 4e-1, 3e1])

i = 0
Rep_list = [1,250]
ReR_over_Rep_list = np.linspace(0.1,12,1000)

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

    ax.loglog(ReR_over_Rep_list, Clr_LL,
            color=tableau20[i], linestyle='-')
    ax.loglog(ReR_over_Rep_list, Clr_OB,
            color=tableau20[i], linestyle='--')
    ax.loglog(ReR_over_Rep_list, Clr_LO,
            color=tableau20[i], linestyle=':')
    i += 1

#first legend
# line1 = mlines.Line2D([], [], color='black', linestyle='-',
#                            label='Rubinow and Keller (1961)')
line2 = mlines.Line2D([], [], color='black', linestyle='-',
                           label='Lun and Liu (1997)')
line3 = mlines.Line2D([], [], color='black', linestyle='--',
                           label='Oesterle and Bui Dinh (1998)')
line4 = mlines.Line2D([], [], color='black', linestyle=':',
                           label='Loth (2008)')
first_legend = plt.legend(handles=[line2, line3, line4],
                          loc='best')


# #second legend
blue_patch = mpatches.Patch(color=tableau20[0], label='$\mathrm{Re}_p = 1$')
orange_patch = mpatches.Patch(color=tableau20[1], label='$\mathrm{Re}_p = 250$')
ax.legend(handles=[blue_patch,orange_patch],
           loc=(0.75,0.45))

ax = plt.gca().add_artist(first_legend)

fig.tight_layout(pad=0.01)
plt.savefig('magnus/magnus.pdf',
            format='pdf')


# # Plot fixed TwoOmega, varying Re_p
# plt.figure()
# ax = plt.subplot(111)
# plt.ylabel('$C_{LR}$')
# plt.xlabel('$Re_p$')

# i = 0
# TwoOmegas = [1e-1,1e0,2e0]
# Re_ps = np.linspace(1e-3,5e2,625)

# for to in TwoOmegas:
#     j = 0
#     Clr_RK = np.zeros(len(Re_ps))
#     Clr_LL = np.zeros(len(Re_ps))
#     Clr_OB = np.zeros(len(Re_ps))
#     Clr_LO = np.zeros(len(Re_ps))

#     for Re_p in Re_ps:
#         Clr_RK[j] = rubKel(Re_p, to)
#         Clr_LL[j] = lunLiu(Re_p, to)
#         Clr_OB[j] = oesBui(Re_p, to)
#         Clr_LO[j] = loth(Re_p, to)
#         j += 1

#     plt.loglog(Re_ps, Clr_RK,
#             lw=2.5, color=tableau20[i], linestyle='-')
#     plt.loglog(Re_ps, Clr_LL,
#             lw=2.5, color=tableau20[i], linestyle='--')
#     plt.loglog(Re_ps, Clr_OB,
#             lw=2.5, color=tableau20[i], linestyle='-.')
#     plt.loglog(Re_ps, Clr_LO,
#             lw=2.5, color=tableau20[i], linestyle=':')
#     i += 1

# #first legend
# line1 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='-',
#                            label='Rubinow and Keller (1961)')
# line2 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='--',
#                            label='Lun and Liu (1997)')
# line3 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='-.',
#                            label='Oesterle and Bui Dinh (1998)')
# line4 = mlines.Line2D([], [], lw=2.5, color='black', linestyle=':',
#                            label='Loth (2008)')
# first_legend = plt.legend(handles=[line1, line2, line3, line4],
#                           loc=(0.01,0.6))
# ax = plt.gca().add_artist(first_legend)

# #second legend
# blue_patch = mpatches.Patch(color=tableau20[0], label='$Re_r/Re_p = 0.1$')
# orange_patch = mpatches.Patch(color=tableau20[1], label='$Re_r/Re_p = 1.0$')
# green_patch = mpatches.Patch(color=tableau20[2], label='$Re_r/Re_p = 2.0$')
# plt.legend(handles=[blue_patch,orange_patch,green_patch],
#            loc=(0.01,0.425))

# # plt.savefig("CL_vs_Rep.png", bbox_inches="tight")


# # Plot fixed Re_p, varying TwoOmega (another range!)
# plt.figure()
# ax = plt.subplot(111)
# plt.ylabel('$C_{LR}$')
# plt.xlabel('$Re_r/Re_p$')

# i = 0
# Re_ps = [1e1,1.4e2]
# TwoOmegas = np.linspace(2e0,1.2e1)

# for Re_p in Re_ps:
#     j = 0
#     Clr_RK = np.zeros(len(TwoOmegas))
#     Clr_LL = np.zeros(len(TwoOmegas))
#     Clr_OB = np.zeros(len(TwoOmegas))
#     Clr_LO = np.zeros(len(TwoOmegas))

#     for to in TwoOmegas:
#         Clr_RK[j] = rubKel(Re_p, to)
#         Clr_LL[j] = lunLiu(Re_p, to)
#         Clr_OB[j] = oesBui(Re_p, to)
#         Clr_LO[j] = loth(Re_p, to)
#         j += 1

#     plt.loglog(TwoOmegas, Clr_RK,
#             lw=2.5, color=tableau20[i], linestyle='-')
#     plt.loglog(TwoOmegas, Clr_LL,
#             lw=2.5, color=tableau20[i], linestyle='--')
#     plt.loglog(TwoOmegas, Clr_OB,
#             lw=2.5, color=tableau20[i], linestyle='-.')
#     plt.loglog(TwoOmegas, Clr_LO,
#             lw=2.5, color=tableau20[i], linestyle=':')
#     i += 1

# #first legend
# line1 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='-',
#                            label='Rubinow and Keller (1961)')
# line2 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='--',
#                            label='Lun and Liu (1997)')
# line3 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='-.',
#                            label='Oesterle and Bui Dinh (1998)')
# line4 = mlines.Line2D([], [], lw=2.5, color='black', linestyle=':',
#                            label='Loth (2008)')
# first_legend = plt.legend(handles=[line1, line2, line3, line4],
#                           loc=(0.01,0.8))
# ax = plt.gca().add_artist(first_legend)

# #second legend
# blue_patch = mpatches.Patch(color=tableau20[0], label='$Re_p = 10$')
# orange_patch = mpatches.Patch(color=tableau20[1], label='$Re_p = 140$')
# plt.legend(handles=[blue_patch,orange_patch],
#            loc=(0.01,0.65))

# # plt.savefig("CL_vs_ReroverRep_2.png", bbox_inches="tight")


# # Plot fixed TwoOmega, varying Re_p (another range!)
# plt.figure()
# ax = plt.subplot(111)
# plt.ylabel('$C_{LR}$')
# plt.xlabel('$Re_p$')

# i = 0
# TwoOmegas = [2e0,1.2e1]
# Re_ps = np.linspace(1e1,1.4e2,625)

# for to in TwoOmegas:
#     j = 0
#     Clr_RK = np.zeros(len(Re_ps))
#     Clr_LL = np.zeros(len(Re_ps))
#     Clr_OB = np.zeros(len(Re_ps))
#     Clr_LO = np.zeros(len(Re_ps))

#     for Re_p in Re_ps:
#         Clr_RK[j] = rubKel(Re_p, to)
#         Clr_LL[j] = lunLiu(Re_p, to)
#         Clr_OB[j] = oesBui(Re_p, to)
#         Clr_LO[j] = loth(Re_p, to)
#         j += 1

#     plt.loglog(Re_ps, Clr_RK,
#             lw=2.5, color=tableau20[i], linestyle='-')
#     plt.loglog(Re_ps, Clr_LL,
#             lw=2.5, color=tableau20[i], linestyle='--')
#     plt.loglog(Re_ps, Clr_OB,
#             lw=2.5, color=tableau20[i], linestyle='-.')
#     plt.loglog(Re_ps, Clr_LO,
#             lw=2.5, color=tableau20[i], linestyle=':')
#     i += 1

# #first legend
# line1 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='-',
#                            label='Rubinow and Keller (1961)')
# line2 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='--',
#                            label='Lun and Liu (1997)')
# line3 = mlines.Line2D([], [], lw=2.5, color='black', linestyle='-.',
#                            label='Oesterle and Bui Dinh (1998)')
# line4 = mlines.Line2D([], [], lw=2.5, color='black', linestyle=':',
#                            label='Loth (2008)')
# first_legend = plt.legend(handles=[line1, line2, line3, line4],
#                           loc=(0.54,0.675))
# ax = plt.gca().add_artist(first_legend)

# #second legend
# blue_patch = mpatches.Patch(color=tableau20[0], label='$Re_r/Re_p = 2$')
# orange_patch = mpatches.Patch(color=tableau20[1], label='$Re_r/Re_p = 12$')
# plt.legend(handles=[blue_patch,orange_patch],
#            loc=(0.01,0.02))

# # plt.savefig("CL_vs_Rep_2.png", bbox_inches="tight")
