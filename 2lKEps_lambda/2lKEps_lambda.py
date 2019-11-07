import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')

A_2layer = 0.05*200*2/np.log((1.+0.98)/(1.-0.98))
Rey = np.linspace(150,250,1000)
lambdaa = 0.5*(1+np.tanh((Rey-200)/A_2layer))

plt.style.use('oneHalfColumn.mplstyle')
fig, ax = plt.subplots()
ax.set_ylabel(r'$\lambda$')
ax.set_xlabel(r'$\mathrm{Re}_y$')
ax.axis([185, 215.0, 0, 1])
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_minor_locator(plt.MultipleLocator(5))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25/2))
ax.plot(Rey, lambdaa,
        color='black',
        linewidth=1,
        linestyle='-')
ax.grid(True)
fig.tight_layout(pad=0.01)
plt.savefig('2lKEps_lambda/2lKEps_lambda.pdf',
            format='pdf')
