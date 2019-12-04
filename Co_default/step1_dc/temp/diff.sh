#for i in Co_default Co_optimized Ni_default Ni_optimized
for i in Co_optimized Ni_default Ni_optimized
do
for a in eq us
do
diff 0/$a'.in' ../../../$i/step1_dc/temp/0/$a'.in'
diff files/$a'.in' ../../../$i/step1_dc/temp/files/$a'.in'
diff 1.0/$a'.in' ../../../$i/step1_dc/temp/1.0/$a'.in'
#diff 0/$a'.in' ../../../+100ns/$i/step1_dc/temp/0/$a'.in'
#diff files/$a'.in' ../../../+100ns/$i/step1_dc/temp/files/$a'.in'
#diff 1.0/$a'.in' ../../../+100ns/$i/step1_dc/temp/1.0/$a'.in'
#diff 0/$a'.in' ../../../+200ns/$i/step1_dc/temp/0/$a'.in'
#diff files/$a'.in' ../../../+200ns/$i/step1_dc/temp/files/$a'.in'
#diff 1.0/$a'.in' ../../../+200ns/$i/step1_dc/temp/1.0/$a'.in'
done
done

