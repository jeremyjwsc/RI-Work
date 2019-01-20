'open gradsplots.ctl'
'set dbuff on'
t = 1
'set gxout shaded'
'clear'
while (t <= 9)
  'set t 't
  'draw title Model Pressure (hPa)'
  'd pressure'  
  'cbar'
  'swap'
  'printim pressure/NestPressure't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 9)
  'set t 't
  'draw title Sea Levelp Pressure (hPa)'
  'd slp'  
  'cbar'
  'swap'
  'printim sea/NestSeaLevel't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 9)
  'set t 't
  'draw title High Cloud Fraction (%)'
  'd clfhi'  
  'cbar'
  'swap'
  'printim cloud/NestHighCloud't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 9)
  'set t 't
  'draw title Wind Speed (m s-1)'
  'd wspd'  
  'cbar'
  'swap'
  'printim wind/NestWindSpeed't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 9)
  'set t 't
  'draw title Relative Humidity (%)'
  'd rh'  
  'cbar'
  'swap'
  'printim hum/NestHumidity't'.png png'
  'clear'
  t = t + 1
endwhile

t = 1
'set gxout shaded'
'clear'
while (t <= 9)
  'set t 't
  'draw title Temperature (C)'
  'd tc'  
  'cbar'
  'swap'
  'printim temp/NestTemperature't'.png png'
  'clear'
  t = t + 1
endwhile

