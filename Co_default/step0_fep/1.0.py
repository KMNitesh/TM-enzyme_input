import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

for a in [150,200,250,300,350,400,450,500,550,600]:
  adir=dir+ "%s_fep/"%(a)
  sdir=adir+"1.0/"
  os.chdir(sdir)
  i=1.0
  f=a*i
  os.system("sed -i 's/XXX/%s/g' %s.RST"%(f,i))
  os.system("sbatch 1.0_eq.pbs")
  os.chdir(dir)
