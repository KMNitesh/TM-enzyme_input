import os

dir = '/mnt/scratch/songlin3/run/center_dis_glx/Ni_alloptimized/'

for i in [150,200,250,300,350,400,450,500,550,600]:
#for i in [150,200,250,300,350,400]:
#for i in [250,450,500,550,600]:
  a = i
  adir = dir + "%d"%(a) + "/calcu/"
  os.chdir(adir)
  #print os.getcwd()
  #os.system("sh c.sh")
  #os.system("tail *sum*")
  os.system("tail 1*CHARGE*")
  print
  os.chdir(dir)
