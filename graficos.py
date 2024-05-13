#!/usr/bin/env python
# -*- coding: utf-8 -*-



#tramanho das bandas
BANDWIDTH = [100, 150, 200, 250, 300, 350, 400]


######################## Graficos #######################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # Importe o módulo necessário
import matplotlib.cm as cm
import matplotlib.colors as mcolors



local_path_fifo = 'EON_SIM_ONDM\\out\\usa\\'
local_path_alg = 'EON_SIM_V2\\out\\usa\\'
local_path = 'plot\\'
labelss=['ONDM', 'EON_SIM_V2']


###################################################################

fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "availability.dat")
data_alg = np.loadtxt(local_path_alg + "availability.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_fifo['Medio'] *= 100
data_pd_alg['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y-0.19, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('Average Availability [%]')
ax.set_title('Availability all')
ax.legend(labels=labelss)

plt.savefig(local_path + 'availability.png', bbox_inches='tight')



###################################################################



fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "restorability.dat")
data_alg = np.loadtxt(local_path_alg + "restorability.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_fifo['Medio'] *= 100
data_pd_alg['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y-0.05, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y-0.05, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('Average restorability [%]')
ax.set_title('restorability all')
ax.legend(labels=labelss)

plt.savefig(local_path + 'restorability.png', bbox_inches='tight')


###################################################################



fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "bloqueio.dat")
data_alg = np.loadtxt(local_path_alg + "bloqueio.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_fifo['Medio'] *= 100
data_pd_alg['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y+0.2, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y+0.2, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs']) 
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('% Nao Restauradas')
ax.set_title('Req. Nao Restauradas')
ax.legend(labels=labelss)

plt.savefig(local_path + 'bloqueio.png', bbox_inches='tight')


###################################################################


fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "afetadas.dat")
data_alg = np.loadtxt(local_path_alg + "afetadas.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
#data_pd_fifo['Medio'] *= 100
#data_pd_alg['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y+5, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y+5, f'{y:.0f}', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('QTD. Afetadas')
ax.set_title('Afetadas (QTD. Media de Req. Afetadas bloqueio ou quedas)')
ax.legend(labels=labelss)

plt.savefig(local_path + 'afetadas.png', bbox_inches='tight')


###################################################################


fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "saltos.dat")
data_alg = np.loadtxt(local_path_alg + "saltos.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
# Arredondar os valores da coluna 'Medio'
data_pd_fifo['Medio'] = data_pd_fifo['Medio'].round()
data_pd_alg['Medio'] = data_pd_alg['Medio'].round()


ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y+0.02, f'{y:.0f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y+0.02, f'{y:.0f}', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('QTD. Saltos')
ax.set_title('QTD. Saltos')
ax.legend(labels=labelss)

plt.savefig(local_path + 'saltos.png', bbox_inches='tight')



######################################################################


fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "re_afetadas.dat")
data_alg = np.loadtxt(local_path_alg + "re_afetadas.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_fifo['Medio'] = data_pd_fifo['Medio'].round()
data_pd_alg['Medio'] = data_pd_alg['Medio'].round()

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y+0.1, f'{y:.2f}', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y+0.1, f'{y:.2f}', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('QTD. Re-Afetadas')
ax.set_title('QTD. Re-Afetadas')
ax.legend(labels=labelss)

plt.savefig(local_path + 're_afetadas.png', bbox_inches='tight')


###################################################################


fig = plt.figure()
fig.add_subplot(121)
data_fifo1 = np.loadtxt(local_path_fifo + "bloqueio_classe1.dat")
data_alg1 = np.loadtxt(local_path_alg + "bloqueio_classe1.dat")

data_fifo2 = np.loadtxt(local_path_fifo + "bloqueio_classe2.dat")
data_alg2 = np.loadtxt(local_path_alg + "bloqueio_classe2.dat")

data_fifo3 = np.loadtxt(local_path_fifo + "bloqueio_classe3.dat")
data_alg3 = np.loadtxt(local_path_alg + "bloqueio_classe3.dat")


data_pd_fifo1 = pd.DataFrame(data_fifo1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg1 = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

data_pd_fifo2 = pd.DataFrame(data_fifo2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

data_pd_fifo3 = pd.DataFrame(data_fifo3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

data_pd_fifo1['Medio'] *= 100
data_pd_alg1['Medio'] *= 100

data_pd_fifo2['Medio'] *= 100
data_pd_alg2['Medio'] *= 100

data_pd_fifo3['Medio'] *= 100
data_pd_alg3['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo1['Erlangs'], data_pd_fifo1['Medio'], marker='o', color=(255/255, 182/255, 193/255), label='FIFO_COS1')
ax.plot(data_pd_fifo2['Erlangs'], data_pd_fifo2['Medio'], marker='o', color=(255/255, 0/255, 0/255), label='FIFO_COS2')
ax.plot(data_pd_fifo3['Erlangs'], data_pd_fifo3['Medio'], marker='o', color=(139/255, 0/255, 0/255), label='FIFO_COS3')

ax.plot(data_pd_alg1['Erlangs'], data_pd_alg1['Medio'], marker='o', color=(173/255, 216/255, 230/255), label='ALG_COS1')
ax.plot(data_pd_alg2['Erlangs'], data_pd_alg2['Medio'], marker='o', color=(0/255, 0/255, 255/255), label='ALG_COS2')
ax.plot(data_pd_alg3['Erlangs'], data_pd_alg3['Medio'], marker='o', color=(0/255, 0/255, 139/255), label='ALG_COS3')

for x, y in zip(data_pd_fifo1['Erlangs'], data_pd_fifo1['Medio']):
    ax.text(x, y-0.09, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_fifo2['Erlangs'], data_pd_fifo2['Medio']):
    ax.text(x, y-0.09, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_fifo3['Erlangs'], data_pd_fifo3['Medio']):
    ax.text(x, y-0.09, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

for x, y in zip(data_pd_alg1['Erlangs'], data_pd_alg1['Medio']):
    ax.text(x, y-0.09, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg2['Erlangs'], data_pd_alg2['Medio']):
    ax.text(x, y-0.09, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg3['Erlangs'], data_pd_alg3['Medio']):
    ax.text(x, y-0.09, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)


ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('% Nao Restauradas')
ax.set_title('Nao Restauradas COS 1 2 3')
ax.legend(labels=['ONDM COS1', 'ONDM COS2', 'ONDM COS3', 'EON_SIM_V2 COS1', 'EON_SIM_V2 COS2', 'EON_SIM_V2 COS3'])

plt.savefig(local_path + 'bloqueio_classe123.png', bbox_inches='tight')



###################################################################



fig = plt.figure()
fig.add_subplot(121)
data_fifo = np.loadtxt(local_path_fifo + "bloqueio_banda.dat")
data_alg = np.loadtxt(local_path_alg + "bloqueio_banda.dat")
data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_fifo['Medio'] *= 100
data_pd_alg['Medio'] *= 100

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color='r', label='FIFO')
ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color='b', label='ALG')

for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
    ax.text(x, y-0.05, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)
for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
    ax.text(x, y-0.05, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('% Nao Restauradas')
ax.set_title('Banda Nao Restauradas')
ax.legend(labels=labelss)

plt.savefig(local_path + 'bloqueio_banda.png', bbox_inches='tight')


###################################################################

fig = plt.figure()
fig.add_subplot(121)
ax = fig.add_axes([0, 0, 1, 1])
labds=[]
reds = mcolors.LinearSegmentedColormap.from_list('reds', ["red", "darkred"], N=7)
reds = reds(range(7))
blues = mcolors.LinearSegmentedColormap.from_list('blues', ["blue", "darkblue"], N=7)
blues = blues(range(7))

for i, bandwidth in enumerate(BANDWIDTH):
    filename = f"bloqueio_{bandwidth}.dat"
    data_fifo = np.loadtxt(local_path_fifo + filename)
    data_pd_fifo = pd.DataFrame(data_fifo, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
    data_pd_fifo['Medio'] *= 100
    ax.plot(data_pd_fifo['Erlangs'], data_pd_fifo['Medio'], marker='o', color=blues[i], label=f"bloqueio_{bandwidth}")
    labds.append("bloqueio ONDM " + str(bandwidth))
    for x, y in zip(data_pd_fifo['Erlangs'], data_pd_fifo['Medio']):
        ax.text(x, y-0.05, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)


for i, bandwidth in enumerate(BANDWIDTH):
    filename = f"bloqueio_{bandwidth}.dat"
    data_alg = np.loadtxt(local_path_alg + filename)
    data_pd_alg = pd.DataFrame(data_alg, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
    data_pd_alg['Medio'] *= 100
    ax.plot(data_pd_alg['Erlangs'], data_pd_alg['Medio'], marker='o', color=reds[i], label=f"bloqueio_{bandwidth}")
    labds.append("bloqueio EO_SIM_V2 " + str(bandwidth))
    for x, y in zip(data_pd_alg['Erlangs'], data_pd_alg['Medio']):
        ax.text(x, y-0.05, f'{y:.2f}%', ha='center', va='bottom', fontsize=8)

ax.set_xticks(data_pd_fifo['Erlangs'])
ax.set_xlabel('Load [Erlangs]')
ax.set_ylabel('% Nao Restauradas')
ax.set_title('Nao Restauradas Bandas')
#ax.legend(labels=labds)
# Configure a legenda
ax.legend(labels=labds, loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 10})




plt.savefig(local_path + 'bloqueio_bandas.png', bbox_inches='tight')





###################################################################
