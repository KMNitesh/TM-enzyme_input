import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

for a in [150,200,250,300,350,400,450,500,550,600]:
#for a in [200,250,300,350,400,450,500,550,600]:
  adir=dir+ "%s_fep/"%(a)
  array= [0,0.0025,0.005,0.0075,0.01,0.02,0.04,0.06,0.08,0.1,0.2,0.4,0.6,0.8,1.0]
  for n in range(0,len(array)):
    i=array[n]
    f=a*i
    wdir=adir+"%s/"%(i)
    os.chdir(wdir)
    if os.path.isfile('%s_us.out'%(i)):
      if 'Total wall time' not in open("%s_us.out"%(i)).read():
        #os.system("sbatch %s_us.pbs"%(i))
        print os.getcwd(),'not done'
    else:
      #os.system("sbatch mh.pbs")
      print os.getcwd(), 'no no no no  file'
  os.chdir(dir)
