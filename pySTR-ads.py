#!/usr/bin/python
# -*- coding: utf-8 -*-
''' A simple Python script to add an intermediate (or initial) time slot in .srt subtitles files (useful when video has an ad but not the SRT file) '''

__author__ = "Francisco Garate - @garpa"
__copyright__ = "Copyleft 2014"
__license__ = "GPL v3"
__version__ = "1.0"
__date__ = "2014-01-06"

#example (add 23 seconds after minute 12):
'''
Before:
-------
181
00:12:02,801 --> 00:12:04,909
<i>The IT Crowd continues next!</i>

After:
------
181
00:12:25,801 --> 00:12:27,909 
<i>The IT Crowd continues next!</i>
'''

import datetime

#Settings:
pause_minute = 12
pause_duration = 23 #in seconds
file_input = open('x_example.srt','r')
file_ouput = open('z_example.srt','w')


lines = file_input.readlines()
count_lines = len(lines)

pause_duration = datetime.timedelta(seconds=pause_duration)
second_part = True

for i in range(0,count_lines):
	if '-->' in lines[i]:
		original_ini = lines[i].split(' --> ')[0].strip()
		original_end = lines[i].split(' --> ')[1].strip()
		pause = datetime.datetime.strptime(original_ini,'%H:%M:%S,%f')
		if pause.minute >= pause_minute:
			new_ini = datetime.datetime.strptime(original_ini,'%H:%M:%S,%f') + pause_duration
			new_end = datetime.datetime.strptime(original_end,'%H:%M:%S,%f') + pause_duration
			new_ini_str = new_ini.strftime('%H:%M:%S,%f')[:-3]
			new_end_str = new_end.strftime('%H:%M:%S,%f')[:-3]
			file_ouput.writelines('%s --> %s \n' % (new_ini_str,new_end_str))
		else:
			file_ouput.writelines(lines[i])
	else:
		file_ouput.writelines(lines[i])

file_input.close()
file_ouput.close()
print "Done!"