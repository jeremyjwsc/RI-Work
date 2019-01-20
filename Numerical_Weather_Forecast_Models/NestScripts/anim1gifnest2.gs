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
  'printim gifs2/pressure2/Nest2Pressure't'.gif gif'
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
  'printim gifs2/sea2/Nest2SeaLevel't'.gif gif'
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
  'printim gifs2/cloud2/Nest2HighCloud't'.gif gif'
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
  'printim gifs2/wind2/Nest2WindSpeed't'.gif gif'
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
  'printim gifs2/hum2/Nest2Humidity't'.gif gif'
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
  'printim gifs2/temp2/Nest2Temperature't'.gif gif'
  'clear'
  t = t + 1
endwhile

