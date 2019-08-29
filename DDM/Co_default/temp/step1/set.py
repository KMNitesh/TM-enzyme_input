import os

dir = '/mnt/scratch/songlin3/run/try2_default_final/MMM/step1/'
filesdir = dir + 'files/'
temp_heatin = filesdir + 'temp_heat.in'
temp_equiin = filesdir + 'temp_equi.in'
temp_prodin = filesdir + 'temp_prod.in'
temp_heat_pbs = filesdir + 'temp_heat.pbs'
temp_equi_pbs = filesdir + 'temp_equi.pbs'
temp_prod_pbs = filesdir + 'temp_prod.pbs'

lambd = [ 0.00922, 0.04794, 0.11505, 0.20634, 0.31608, 0.43738, 0.56262, 0.68392, 0.79366, 0.88495, 0.95206, 0.99078]
for j in lambd:
  os.system("rm -r %6.5f" %(j)) 
  os.system("mkdir %6.5f" %(j)) 
  os.chdir("%6.5f" %(j))
  #os.system("rm *")
  workdir = dir + "%6.5f" %(j) + '/'
  #heatin
  heatin = workdir + "%6.5f_heat.in" %(j)
  os.system("cp %s %s" %(temp_heatin, heatin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, heatin))
  #equiin
  equiin = workdir + "%6.5f_equi.in" %(j)
  os.system("cp %s %s" %(temp_equiin, equiin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, equiin))
  #prodin
  prodin = workdir + "%6.5f_prod.in" %(j)
  os.system("cp %s %s" %(temp_prodin, prodin))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, prodin))
  #RST
  os.system("cp ../files/dis.RST .")
  #PBS
  heat_pbs = workdir + "%6.5f_heat.pbs" %(j)
  os.system("cp %s %s" %(temp_heat_pbs, heat_pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, heat_pbs))
  equi_pbs = workdir + "%6.5f_equi.pbs" %(j)
  os.system("cp %s %s" %(temp_equi_pbs, equi_pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, equi_pbs))
  prod_pbs = workdir + "%6.5f_prod.pbs" %(j)
  os.system("cp %s %s" %(temp_prod_pbs, prod_pbs))
  os.system("sed -i 's/XXX/%6.5f/g' %s" %(j, prod_pbs))
  #top
  os.system("cp ../glx-co_step1.prmtop .")
  os.system("cp ../0.5_min.rst .")
  #submit pbs 
  os.system("sbatch %s" %(heat_pbs)) 
  os.chdir(dir)
  
