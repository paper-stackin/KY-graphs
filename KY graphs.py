#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

clas = pd.read_csv('Tables/CS/cs_clas_2.csv')
phi_clas = clas['phi'].tolist()

inf = pd.read_csv('Tables/CS/Information.csv')

for index, row in inf.iterrows():
    cs_clas = clas[row['cs_clas_name']].tolist()
    dcs_clas = clas[row['dcs_clas_name']].tolist()
    
    prog = pd.read_csv(row['prog_names'])
    cs_prog = prog['cs'].tolist()
    dcs_prog = prog['dcs'].tolist()
    phi_prog = prog['phi'].tolist()
    
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)
    fig.patch.set_facecolor('w')
    
    ax.errorbar(phi_clas, cs_clas, yerr = dcs_clas, c = 'b', label = 'Данные CLAS')
    ax.errorbar(phi_prog, cs_prog, yerr = dcs_prog, c = 'r', label = 'Расчет дифференциального сечения')
    
    ax.legend(title_fontsize = 9, title = row['title'], loc = row['loc'])
    ax.set_xlabel('\u03C6, \N{DEGREE SIGN}')
    ax.set_ylabel(r'$dσ_{γ}/dΩ, нб/ср$')
    ax.set_xlim(0, 360)
    ax.set_xticks(np.arange(0, 420, 60))
    ax.set_ylim(row['y_min'], row['y_max'])
    ax.set_yticks(np.arange(row['y_min'], row['y_max']+row['yticks'], row['yticks']))
    
    fig.savefig(row['folder'])


# In[3]:


inf = pd.read_csv('Tables/ST_Q2_extr/Information.csv')


KL_cos = np.array([])
KL_St = np.array([])
KL_dSt = np.array([])
KS_cos = np.array([])
KS_St = np.array([])
KS_dSt = np.array([])
KL = pd.read_csv('Tables/ST_Q2_extr/KLP3.csv')
KL['St'] = KL['Su']/(1 + KL['eps']/5)
KL['dSt'] = KL['dSu']/(1 + KL['eps']/5)
for index, row in KL.iterrows():
    if (row['W'] == 1.875) and (row['Q2'] == 3.45):
        KL_cos = np.append(KL_cos, row['cos_th'])
        KL_St = np.append(KL_St, row['St'])
        KL_dSt = np.append(KL_dSt, row['dSt'])
KS = pd.read_csv('Tables/ST_Q2_extr/KSP3.csv')
KS['St'] = KS['Su']/(1 + KS['eps']/5)
KS['dSt'] = KS['dSu']/(1 + KS['eps']/5)
for index, row in KS.iterrows():
    if (row['W'] == 1.825) and (row['Q2'] == 3.45):
        KS_cos = np.append(KS_cos, row['cos_th'])
        KS_St = np.append(KS_St, row['St'])
        KS_dSt = np.append(KS_dSt, row['dSt'])

for index, row in inf.iterrows():
    prog = pd.read_csv(row['name'])
    cos = prog['cos_th'].tolist()
    St = prog['S_t[nb/sr]'].tolist()
    dSt = prog['dS_t[nb/sr]'].tolist()
    
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)
    fig.patch.set_facecolor('w')
    
    ax.errorbar(cos, St, yerr = dSt, c = 'grey', ls = 'none', elinewidth = 2.1)
    ax.errorbar(cos, St, c = 'black', label = 'Результаты экстраполяции')
    if index == 0:
        ax.errorbar(KL_cos, KL_St, yerr = KL_dSt, c = 'b', label = 'Данные CLAS', fmt='o')
    if index == 3:
        ax.errorbar(KS_cos, KS_St, yerr = KS_dSt, c = 'b', label = 'Данные CLAS', fmt='o')

    ax.set_xlim(-1, 1)
    if index <3:
        ax.set_ylim(0, 120)
    else:
        ax.set_ylim(-5, 20)
    ax.grid(True, c ='black', zorder = 0)
    ax.set_xlabel('cos'r'$θ$')
    ax.set_ylabel(r'$dσ_{T}/dΩ, нб/ср$')
    ax.legend(title_fontsize = 9, title = row['title'], framealpha = 1, loc = 'upper left')
    
    fig.savefig(row['folder'])


# In[ ]:




