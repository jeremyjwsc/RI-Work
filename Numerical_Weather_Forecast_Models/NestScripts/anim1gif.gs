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
  'printim gifs/pressure/NestPressure't'.gif gif'
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
  'printim gifs/sea/NestSeaLevel't'.gif gif'
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
  'printim gifs/cloud/NestHighCloud't'.gif gif'
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
  'printim gifs/wind/NestWindSpeed't'.gif gif'
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
  'printim gifs/hum/NestHumidity't'.gif gif'
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
  'printim gifs/temp/NestTemperature't'.gif gif'
  'clear'
  t = t + 1
endwhile

