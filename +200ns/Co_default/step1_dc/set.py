import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'
for a in [150,200,250,300,350,400,450,500,550,600]:
#for a in [150]:
#for a in [200,250,300,350,400,450,500,550,600]:
  os.system("rm -r %s_dc"%(a))
  os.system("cp -r temp/ %s_dc"%(a))
  adir=dir+ "%s_dc/"%(a)
  os.chdir(adir)
  os.system("sed -i 's/MMM/%s/g' */*pbs"%(a))
  array= [0,0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078,1.0]
  for n in range(1,len(array)-1):
    i=array[n]
    os.system("rm -r %s"%(i))
    os.system("cp -r files %s"%(i))
    wdir=adir+"%s/"%(i)
    os.chdir(wdir)
    os.system("mv eq.in %s_eq.in"%(i))
    os.system("mv us.in %s_us.in"%(i))
    os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
    os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
    os.system("sed -i 's/MMM/%s/g' dis.RST"%(a))
    os.system("mv eq.pbs %s_eq.pbs"%(i))
    os.system("mv us.pbs %s_us.pbs"%(i))
    os.system("sed -i 's/XXX/%s/g' *.pbs"%(i))
    os.system("sed -i 's/NNN/%s/g' *.pbs"%(array[n+1]))
    os.system("sed -i 's/PPP/%s/g' *.pbs"%(array[n-1]))
    os.chdir(adir)
  sdir=adir+"0/"
  os.chdir(sdir)
  i=0
  os.system("cp /mnt/gs18/scratch/users/songlin3/run/glx-0904/+200ns/Co_default/step0_fep/%s_fep/1.0/%s_1.0_eq_center.rst ."%(a,a))
  os.system("mv eq.in %s_eq.in"%(i))
  os.system("mv us.in %s_us.in"%(i))
  os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
  os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
  os.system("mv eq.pbs %s_eq.pbs"%(i))
  os.system("mv us.pbs %s_us.pbs"%(i))
  os.system("sed -i 's/XXX/%s/g' *.pbs"%(i))
  os.system("sed -i 's/MMM/%s/g' dis.RST"%(a))
  os.system("sbatch 0_eq.pbs")
  sdir=adir+"1.0/"
  os.chdir(sdir)
  i=1.0
  os.system("mv eq.in %s_eq.in"%(i))
  os.system("mv us.in %s_us.in"%(i))
  os.system("sed -i 's/XXX/%s/g' %s_eq.in"%(i,i))
  os.system("sed -i 's/XXX/%s/g' %s_us.in"%(i,i))
  os.system("mv eq.pbs %s_eq.pbs"%(i))
  os.system("mv us.pbs %s_us.pbs"%(i))
  os.system("sed -i 's/XXX/%s/g' *.pbs"%(i))
  os.system("sed -i 's/MMM/%s/g' dis.RST"%(a))
  os.system("sed -i 's/MMM/%s/g' center.in"%(a))
  os.chdir(dir)
