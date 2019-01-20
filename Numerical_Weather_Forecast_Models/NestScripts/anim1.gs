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
  'printim png/pressure/NestPressure't'.png png'
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
  'printim png/sea/NestSeaLevel't'.png png'
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
  'printim png/cloud/NestHighCloud't'.png png'
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
  'printim png/wind/NestWindSpeed't'.png png'
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
  'printim png/hum/NestHumidity't'.png png'
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
  'printim png/temp/NestTemperature't'.png png'
  'clear'
  t = t + 1
endwhile

