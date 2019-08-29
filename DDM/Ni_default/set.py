import os

dir = '/mnt/home/songlin3/top_CdNi/Ni/keepCD2000/default_final/'
    
#for i in [20,50,100,150,200,250,300,350,400,450,500,550,600]:
#for i in [100,150,200]:
for i in [150,200,250,300,350,400,450,500,550,600]:
  a = i
  os.system("rm -r %s"%(a))
  os.system("cp -r temp %s"%(a))
  os.chdir("%d"%(a))
  adir = dir + "%d"%(a) + "/"
  for k in ['step1','step2']:
    os.chdir("%s"%(k))
    workdir = adir + "%s"%(k) + "/" 
    pbs = workdir + "run.pbs"
    os.system("sed -i 's/MMM/%d/g' %s" %(a, pbs))
    RST = workdir + "dis.RST"
    os.system("sed -i 's/XXX/%d/g' %s" %(a, RST))
    filesRST = workdir + "files" + "/" + "dis.RST"
    os.system("sed -i 's/XXX/%d/g' %s" %(a, filesRST))
    setpy = workdir + "set.py"
    os.system("sed -i 's/MMM/%d/g' %s" %(a, setpy))
    os.chdir(workdir)
    os.system("sbatch run.pbs")
    os.chdir(adir)
  os.chdir(dir)
