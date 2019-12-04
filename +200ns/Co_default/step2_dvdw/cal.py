import os

dir = os.path.dirname(os.path.realpath(__file__)) + '/'

for a in [150,200,250,300,350,400,450,500,550,600]:
  adir = dir + "%s_dvdw/"%(a)
  os.chdir(adir)
  #os.system("cp  -r ../temp/calcu .")
  sdir=adir+"calcu/"
  os.chdir(sdir)
  #print os.getcwd()
  #os.system("sh c.sh")
  #os.system("tail *sum*")
  os.system("tail 1*")
  print
  os.chdir(dir)
