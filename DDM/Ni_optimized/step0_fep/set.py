import os

dir = '/mnt/scratch/songlin3/run/center_dis_glx/Ni_alloptimized/step0_fep/'

for a in [150,200,250,300,350,400,450,500,550,600]:
  os.system("rm -r %s_fep"%(a))
  os.system("cp -r files/ %s_fep"%(a))
  adir=dir+ "%s_fep/"%(a)
  os.chdir(adir)
  os.system("sed -i 's/MMM/%s/g' *pbs"%(a))
  array= [0,0.0025,0.005,0.0075,0.01,0.02,0.04,0.06,0.08,0.1,0.2,0.4,0.6,0.8,1.0]
  for n in range(0,len(array)):
    i=array[n]
    f=a*i
    os.system("rm -r %s"%(i))
    os.system("mkdir %s"%(i))
    wdir=adir+"%s/"%(i)
    os.chdir(wdir)
    os.system("cp ../min.in %s_min.in"%(i))
    os.system("sed -i 's/XXX/%s/g' %s_min.in"%(i,i))
    os.system("cp ../heat.in %s_heat.in"%(i))
    os.system("sed -i 's/XXX/%s/g' %s_heat.in"%(i,i))
    os.system("cp ../eq.in %s_eq.in"%(i))
    os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
    os.system("cp ../us.in %s_us.in"%(i))
    os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
    os.system("cp ../dis.RST %s.RST"%(i))
    os.system("sed -i 's/XXX/%s/g' %s.RST"%(f,i))
    os.system("cp ../temp.pbs %s.pbs"%(i))
    os.system("sed -i 's/XXX/%s/g' %s.pbs"%(i,i))
    os.system("cp ../*prmtop .")
    os.system("cp ../*inpcrd .")
    os.system("sbatch %s.pbs"%(i))
    os.chdir(adir)
  os.chdir(dir)
