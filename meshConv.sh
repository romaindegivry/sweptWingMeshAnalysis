#clean
cd Panel_code
rm -r results/*
clear
#compile
echo "Compilation started"
gfortran geowing.f -o geowing &
gfortran combo.f -o combo &
wait
echo "Compilation Done"
#compute
for angle in 0
do
  for i in 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40
  do
    echo "32.5" > stream.dat
    echo $angle >> stream.dat
    echo "0.0"  >> stream.dat
    echo "1.211558" >> stream.dat

    for j in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    do
    echo "stream parametres"
    cat stream.dat
    echo 'Analysis started'
    #Generate the mesh file
    echo $i >  meshParameters.dat
    echo $j >> meshParameters.dat
    echo $angle
    cat meshParameters.dat
    #Create Output directory
    dirName=$(echo "results/"$angle"deg_"$i"x"$j)
    mkdir $dirName
    #run mesh generation
    ./geowing
    #run solution
    ./combo mesh.dat auxiliary.dat stream.dat sect inp
    wait
    #move the files away from the directory
    mv sect_0* $dirName
    mv span_load $dirName
    #clean the files
    echo "Iteration completed"
    wait
    clear
    done
  done
done
#clean the empty directories
rmdir results/*
echo "Compute done"
cd ../
python3 processor.py
