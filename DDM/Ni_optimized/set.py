import os


dir = '/mnt/scratch/songlin3/run/center_dis_glx/Ni_alloptimized//'

for i in [150,200,250,300,350,400,450,500,550,600]:
#for i in [100,150,200]:
  a = i
  adir = dir + "%s/"%(a)
  os.chdir(adir)
  for k in ['1','2']:
    workdir = adir + "step%s"%(k) + "/" 
    os.chdir(workdir)
    #os.system("sed -i 's/20:00:00/30:00:00/g' run.pbs")
    os.system("sbatch run.pbs")
    os.chdir(adir)
  os.chdir(dir)
