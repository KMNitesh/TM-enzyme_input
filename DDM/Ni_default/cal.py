import os

dir = '/mnt/home/songlin3/top_CdNi/Ni/keepCD2000/default_final/'

for i in [150,200,250,300,350,400,450,500,550,600]:
#for i in [20,50,400,450,600]:
  a = i
  adir = dir + "%d"%(a) + "/calcu/"
  os.chdir(adir)
  #os.system("cp ../../temp/calcu/c.sh .")
  #print os.getcwd()
  #os.system("sh c.sh")
  #os.system("tail *sum*")
  os.system("tail 1*VDW*")
  print
 #bdir = dir + "%d"%(a) + "/calcu_step0/"
 #os.chdir(bdir)
 #print os.getcwd()
 #os.system("sh c.sh")
 #os.system("tail *sum*")
 #os.system("tail step0_dvdl.txt")
 #print
  os.chdir(dir)
