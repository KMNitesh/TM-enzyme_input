import os

dir = '/mnt/scratch/songlin3/run/try2_default_final/'
    
#for i in [20,50,100,150,200,250,300,350,400,450,500,550,600]:
#for i in [100,150,200]:
for i in [150,200,250,300,350,400,450,500,550,600]:
  a = i
  adir = dir + "%d"%(a) + "/"
  os.chdir(adir)
  for k in ['step1','step2']:
    workdir = adir + "%s"%(k) + "/"
    os.chdir(workdir)
    print os.getcwd()
    if 'Total wall time' in open('0.5_min.out').read() and os.path.isfile('0.5_min.rst'):
      print 'good to go'
      os.system("sed -i 's/MMM/%d/g' set.py"%(a))
      os.system("sed -i 's/iwrap=1/iwrap=0/g' files/temp*in")
      os.system("sed -i 's/MMM/%d/g' files/temp*pbs"%(a))
      os.system("python set.py")
    else:
      print 'not ready to go'
    os.chdir(adir)
  os.chdir(dir)
