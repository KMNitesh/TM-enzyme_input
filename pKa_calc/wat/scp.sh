for a in HIP-HID HIP-HIE
do
mkdir $a
cd $a/
mkdir freeMD  one-step
cd freeMD/
scp songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/freeMD/*in .
scp songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/freeMD/*pdb .
scp songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/freeMD/*prmtop .
scp songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/freeMD/*inpcrd .
scp songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/freeMD/*pbs .
cd ..
cd one-step/
scp songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/one-step/* .
scp -r songlin3@rsync.hpcc.msu.edu:/mnt/scratch/songlin3/run/glx-0904/pka_calc/wat/$a/one-step/temp .
cd ../..
done
