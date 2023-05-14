set size square
set key out font ',20'
set xran [0:32.316520]
set yran [0:32.316520]
plot "lj00000000.dat" using 1:2 t "00000" w po pt 6
pause -1
plot "lj00000100.dat" using 1:2 t "00100" w po pt 6
pause 0.01
plot "lj00000200.dat" using 1:2 t "00200" w po pt 6
pause 0.01
plot "lj00000300.dat" using 1:2 t "00300" w po pt 6
pause 0.01
plot "lj00000400.dat" using 1:2 t "00400" w po pt 6
pause 0.01
plot "lj00000500.dat" using 1:2 t "00500" w po pt 6
pause 0.01
plot "lj00000600.dat" using 1:2 t "00600" w po pt 6
pause 0.01
plot "lj00000700.dat" using 1:2 t "00700" w po pt 6
pause 0.01
plot "lj00000800.dat" using 1:2 t "00800" w po pt 6
pause 0.01
plot "lj00000900.dat" using 1:2 t "00900" w po pt 6
pause 0.01
plot "lj00001000.dat" using 1:2 t "01000" w po pt 6
pause 0.01
