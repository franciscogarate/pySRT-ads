pySRT-ads
=========

A simple Python script to add an intermediate (or initial) time slot in .srt subtitles files.

Useful when video has an ad but not the SRT file.

Example (add 23 seconds after minute 12):

<i>Before:</i>
181<br />
00:12:02,801 --> 00:12:04,909<br />
The IT Crowd continues next!<br />

<i>After:</i>
181<br />
00:12:25,801 --> 00:12:27,909 <br />
The IT Crowd continues next!<br />
