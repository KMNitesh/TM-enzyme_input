import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

smd_filesdir = dir + 'smd_files_1/'
disfile = smd_filesdir + 'Ni-Nimz_dis_1.txt'
prm = 'imz_def.prmtop'
#os.system("sed -i 's/cd316cm5/imz2.50'/g files/*.pbs")

for a in range(1,9):

  a = round(float(2.16 - a*0.05),2)
  os.system("rm -r %s"%(a))
  os.system("cp -r files %s"%(a))
  os.chdir(smd_filesdir)
  fil=open(disfile,'r')
  lines=fil.readlines()[1:]
  for line in lines:
    num,dis=line.split()
    dis=round(float(dis),2)
    if dis == a:
       break
       print(dis)
       print(num)
  os.system("cp ptraj.in %s_p.in"%(a))
  os.system("sed -i 's/NNN/%s/g' %s_p.in"%(num,a))
  os.system("cpptraj %s < %s_p.in > out"%(prm,a))
  os.system("cp prod_center_1_%s.rst ../%s/"%(num,a))
  workdir=dir+'%s/'%(a)
  os.chdir(workdir)
  os.system("sed -i 's/XXX/%s/g' dis.RST" %(a))
  os.system("sed -i 's/XXX/%s/g' *.pbs" %(a))
  os.system("sed -i 's/ter_NNN/ter_1_%s/g' *.pbs" %(num))
  os.system("sbatch mh.pbs")
  os.chdir(dir)

