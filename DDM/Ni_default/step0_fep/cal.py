import os

dir = '/mnt/scratch/songlin3/run/Ni_default_step0/'

for a in [150,200,250,300,350,400,450,500,550,600]:
  adir = dir + "%s_fep/"%(a)
  os.chdir(adir)
  print a
  os.system("cp ../c.py .")
  os.system("sed -i 's/AAA/%s/g' c.py"%(a))
  #print os.getcwd()
  os.system("python c.py")
  os.chdir(dir)