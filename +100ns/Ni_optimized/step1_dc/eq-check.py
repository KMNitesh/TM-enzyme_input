import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

for a in [150,200,250,300,350,400,450,500,550,600]:
#for a in [200,250,300,350,400,450,500,550,600]:
  adir=dir+ "%s_dc/"%(a)
  array= [0,0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078,1.0]
  for n in range(0,len(array)):
    i=array[n]
    f=a*i
    wdir=adir+"%s/"%(i)
    os.chdir(wdir)
    if os.path.isfile('%s_eq.out'%(i)):
      if 'Total wall time' not in open("%s_eq.out"%(i)).read():
        #os.system("sbatch mh.pbs")
        print os.getcwd(),'not done'
    else:
      #os.system("sbatch mh.pbs")
      print os.getcwd(), 'no no no no  file'
  os.chdir(dir)
