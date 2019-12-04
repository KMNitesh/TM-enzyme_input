import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

smd_filesdir = dir + 'smd_files/'
disfile = smd_filesdir + 'Ni-AceC_dis.txt' # remember to rename for diff metal lig 
prm = 'nicoo1264_0.145.prmtop'

for a in range(0,60):          #remember to change this
  a = round(float(5.14 + a*0.1),2)
  os.system("rm -r %s"%(a))              #removing the folder if present previously
  os.system("cp -r files %s"%(a))          #making the folder
  os.chdir(smd_filesdir) 
  fil=open(disfile,'r')                    # remember to check with Lin 
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
  os.system("cp prod_center_%s.rst ../%s/"%(num,a))
  workdir=dir+'%s/'%(a)
  os.chdir(workdir)
  os.system("sed -i 's/XXX/%s/g' dis.RST" %(a))
  os.system("sed -i 's/XXX/%s/g' *.pbs" %(a))
  os.system("sed -i 's/NNN/%s/g' *.pbs" %(num))
  os.chdir(dir)
