import os


dir = os.getcwd()

for i in [150,200,250,300,350,400,450,500,550,600]:
#for i in [20,50,200,250,300,350,400,450,500,550,600]:
  a = i
  dir1 = dir + "/%d_dvdw"%(a) + "/"
  os.chdir(dir1)
  workdir = dir1
  for a in [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]:
    adir = workdir + '%s/'%(a)
    os.chdir(adir)
    print os.getcwd()
    os.system("cp ../../p.in .")
    os.system("sed -i 's/XXX/%s/g' p.in"%(a))
    os.system("cpptraj *prmtop < p.in > out")
    os.system("mv *center.netcdf ..")
    os.chdir(workdir)
  os.system("cp ../all.in .")
  os.system("cp 0.11505/*prmtop .")
  os.system("sed -i 's/MMM/%s/g' all.in"%(i))
  os.system("cpptraj -p glx-ni_1264_final_vdw.prmtop < all.in > out")
  os.system("cp %s_all_us_center.netcdf ../../netcdf/%s/step2/"%(i,i))
  os.system("cp glx-ni_1264_final_vdw.prmtop ../../netcdf/%s/step2/"%(i))
  os.system("rm *center*netcdf")
  os.chdir(dir1)
  os.chdir(dir)