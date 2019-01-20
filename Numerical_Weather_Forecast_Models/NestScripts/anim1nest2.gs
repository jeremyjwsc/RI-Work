'reinit'
'clear'
'open gradsplots.ctl'
'set dbuff on'
t = 1
'set gxout shaded'
'clear'
while (t <= 5)
  'set t 't
  'draw title Model Pressure (hPa)'
  'd pressure'  
  'cbar'
  'swap'
  'printim png2/pressure2/Nest2Pressure't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 5)
  'set t 't
  'draw title Sea Levelp Pressure (hPa)'
  'd slp'  
  'cbar'
  'swap'
  'printim png2/sea2/Nest2SeaLevel't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 5)
  'set t 't
  'draw title High Cloud Fraction (%)'
  'd clfhi'  
  'cbar'
  'swap'
  'printim png2/cloud2/Nest2HighCloud't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 5)
  'set t 't
  'draw title Wind Speed (m s-1)'
  'd wspd'  
  'cbar'
  'swap'
  'printim png2/wind2/Nest2WindSpeed't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 5)
  'set t 't
  'draw title Relative Humidity (%)'
  'd rh'  
  'cbar'
  'swap'
  'printim png2/hum2/Nest2Humidity't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 5)
  'set t 't
  'draw title Temperature (C)'
  'd tc'  
  'cbar'
  'swap'
  'printim png2/temp2/Nest2Temperature't'.png png'
  'clear'
  t = t + 1
endwhile
