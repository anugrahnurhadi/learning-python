dset ^sst_pacific.dat
title pacific sea surface temperature
undef -999000000
xdef 86 linear 120 2
ydef 41 linear -40 2
zdef 1 levels 1000
tdef 192 linear 00Z01JAN1975 1mo
vars 1
sst 0 99 99 monthly sea surface temperature
endvars
