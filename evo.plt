
set title "Hinton Paper: How Learning Can Guide Evolution"
set xlabel  "Generation"
set ylabel "Relative Frequency"

plot "evo.dat" u 1:2 w l  title "Correct Alleles", "evo.dat" u 1:3 w l  title "Incorrect Alleles", "evo.dat" u 1:4 w l title "Undecided"
pause -1
