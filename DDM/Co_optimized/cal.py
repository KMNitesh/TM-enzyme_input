import os

dir = '/mnt/gs18/scratch/users/songlin3/run/center_dis_glx/2.23_final/'

for i in [150,200,250,300,350,400,450,500,550,600]:
  a = i
  adir = dir + "%d"%(a) + "/calcu/"
  os.chdir(adir)
  #print os.getcwd()
  #os.system("sh c.sh")
  #os.system("tail *sum*")
  os.system("tail 1*VDW*")
  print
  os.chdir(dir)
