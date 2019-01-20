'open gradsplots.ctl'
'set dbuff on'
t = 1
'set gxout vector'
'clear'
while (t <= 5)
  'set t 't
  'draw title Pressure, Sea, Cloud, Wind, Humidity and Temperature Vector'
  'd pressure;slp;clfhi;wspd;rh;tc'  
  'cbar'
  'swap'
  'printim vectorgrid/NestAllVectors't'.gif gif'
  'clear'
  t = t + 1
endwhile

