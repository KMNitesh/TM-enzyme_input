import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

#for a in range(0,56):          #remember to change this
for a in range(0,23):
  #a = round(float(2.29 + a*0.05),2)
  a = round(float(3.94 + a*0.05),2)
  workdir=dir+'%s/'%(a)
  os.chdir(workdir)
  os.system("sbatch mh.pbs")
  os.chdir(dir)

for a in range(0,60):          #remember to change this
  a = round(float(5.14 + a*0.1),2)
  workdir=dir+'%s/'%(a)
  os.chdir(workdir)
  os.system("sbatch mh.pbs")
  os.chdir(dir)
