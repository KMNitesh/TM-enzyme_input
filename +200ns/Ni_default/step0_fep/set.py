import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'
us_center_rst='/mnt/scratch/songlin3/run/glx-0904/+200ns/Ni_default/freeMD/us_center.rst'  ## change this ! ##

for a in [150,200,250,300,350,400,450,500,550,600]:
#for a in [200,250,300,350,400,450,500,550,600]:
  os.system("rm -r %s_fep"%(a))
  os.system("cp -r temp/ %s_fep"%(a))
  adir=dir+ "%s_fep/"%(a)
  os.chdir(adir)
  os.system("sed -i 's/MMM/%s/g' */*pbs"%(a))
  array= [0,0.0025,0.005,0.0075,0.01,0.02,0.04,0.06,0.08,0.1,0.2,0.4,0.6,0.8,1.0]
  for n in range(1,len(array)-1):
    i=array[n]
    f=a*i
    os.system("rm -r %s"%(i))
    os.system("cp -r files %s"%(i))
    wdir=adir+"%s/"%(i)
    os.chdir(wdir)
    os.system("mv eq.in %s_eq.in"%(i))
    os.system("mv us.in %s_us.in"%(i))
    os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
    os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
    os.system("mv dis.RST %s.RST"%(i))
    os.system("sed -i 's/XXX/%s/g' %s.RST"%(f,i))
    os.system("mv eq.pbs %s_eq.pbs"%(i))
    os.system("mv us.pbs %s_us.pbs"%(i))
    os.system("sed -i 's/XXX/%s/g' *.pbs"%(i))
    os.system("sed -i 's/NNN/%s/g' *.pbs"%(array[n+1]))
    os.system("sed -i 's/PPP/%s/g' *.pbs"%(array[n-1]))
    os.chdir(adir)
  sdir=adir+"0/"
  os.chdir(sdir)
  i=0
  os.system("mv eq.in %s_eq.in"%(i))
  os.system("mv us.in %s_us.in"%(i))
  os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
  os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
  os.system("mv eq.pbs %s_eq.pbs"%(i))
  os.system("mv us.pbs %s_us.pbs"%(i))
  os.system("sed -i 's/XXX/%s/g' *.pbs"%(i))
  os.system("cp %s ."%(us_center_rst))
  os.system("sbatch 0_eq.pbs")
  sdir=adir+"1.0/"
  os.chdir(sdir)
  i=1.0
  os.system("mv eq.in %s_eq.in"%(i))
  os.system("mv us.in %s_us.in"%(i))
  os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
  os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
  os.system("sed -i 's/MMM/%s/g' center.in"%(a))
  os.system("mv eq.pbs %s_eq.pbs"%(i))
  os.system("mv us.pbs %s_us.pbs"%(i))
  os.system("sed -i 's/XXX/%s/g' *.pbs"%(i))
  os.chdir(dir)
