import os
import re
from typing import Pattern
dir = os.getcwd()


def find_info(file_name):
	file_name = file_name.replace(" ", "").replace(".", "").replace("_", "")
	season = 0
	episode = 0

	pattern1 = re.compile(r'[s|S][0-9]{1,2}[e|E][0-9]{1,2}')
	pattern2 = re.compile(r'[0-9]{1,2}[x|X][0-9]{1,2}')

	patterns = [pattern1, pattern2 ]

	for idx, p in enumerate(patterns):
		m = re.search(p, file_name)
		if m:
			if idx == 0:
				season = int(re.split(r'[e|E]', m.group())[0][1:])
				episode = int(re.split(r'[e|E]', m.group())[1])
			elif idx == 1:
				season = int(re.split(r'[x|X]', m.group())[0])
				episode = int(re.split(r'[x|X]', m.group())[1])
			else:
				print("NO MATCH!")
			break

	return [season, episode]

def change_sub_name(sub, file):
	os.rename(sub, file) 

for file in os.listdir(dir):
	if(file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".avi") and ((file[0:-4] + ".srt") not in os.listdir(dir))):
		file_name = file[0:-4]
		file_info = find_info(file_name)
		for sub in os.listdir(dir):
			if(sub.endswith(".srt")):
				sub_name = sub[0:-4]
				sub_info = find_info(sub_name)
				if(sub_info == file_info):
					change_sub_name(sub, file_name+'.srt')
					break
					