import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

#for a in range(0,15):          #remember to change this
for a  in range(0,29):
  a = round(float(3.94 - a*0.05),2)
  workdir=dir+'%s/'%(a)
  os.chdir(workdir)
  os.system("sed -i 's/rk2=100.0, rk3=100.0/rk2=500.0, rk3=500.0/g' dis.RST")
  os.system("rm *out *netcdf *mdinfo *log")
  #os.system("sbatch mh.pbs")
  os.chdir(dir)

for a  in range(0,5):
  a = round(float(2.49 - a*0.05),2)
  workdir=dir+'%s/'%(a)
  os.chdir(workdir)
  os.system("sed -i 's/rk2=100.0, rk3=100.0/rk2=1000.0, rk3=1000.0/g' dis.RST")
  os.system("rm *out *netcdf *mdinfo *log") 
  #os.system("sbatch mh.pbs")
  os.chdir(dir)
