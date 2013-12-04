#coding:UTF-8
#!/usr/bin/python

import os
import numpy as np
import matplotlib.pyplot as plt

#先处理文件
proA=[]
proT=[]
proG=[]
proC=[]
nonA=[]
nonT=[]
nonG=[]
nonC=[]

f=open('data/profreq','r')
for line in f.read().splitlines():
  cons=line.split('\t')
  s=sum([int(x) for x in cons])
  proA.append(float(cons[0])/s)
  proT.append(float(cons[1])/s)
  proG.append(float(cons[2])/s)
  proC.append(float(cons[3])/s)
f=open('data/noprofreq','r')
for line in f.read().splitlines():
  cons=line.split('\t')
  s=sum([int(x) for x in cons])
  nonA.append(float(cons[0])/s)
  nonT.append(float(cons[1])/s)
  nonG.append(float(cons[2])/s)
  nonC.append(float(cons[3])/s)
datalist={'A':[proA,nonA],
          'T':[proT,nonT],
          'G':[proG,nonG],
          'C':[proC,nonC]}
f.close()

x=np.array(range(1,301))
xtick=np.array(range(0,300,40))

bases=['A','T','G','C']
for i in range(4):
  plt.subplot(2,2,i)
  [proy,nony]=datalist[bases[i]]
  plt.plot(x,np.array(proy),label=bases[i]+"% promoter")
  plt.plot(x,np.array(nony),label=bases[i]+"% non-promoter")
  plt.xticks(xtick)
  plt.legend(loc='upper left',fontsize='x-small')
  plt.title(bases[i],fontsize='x-small')
  plt.xlabel("base loci",fontsize='x-small')
  plt.ylabel("frequency%",fontsize='x-small')

plt.savefig("refreq.png")

plt.show()  
