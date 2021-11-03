import os
dir = os.getcwd()

def valid(file_name, indices):
	res = True
	for index in indices:	
		res = res and file_name[index].isdigit()

	return res

def find_info(file_name):
	file_name = file_name.lower().replace(" ", "").replace(".", "").replace("_", "").lower()
	season = 0
	episode = 0
	for i in range(len(file_name)):
		# s01e01
		if(file_name[i] == 's'):
			if(i+3 < len(file_name) and file_name[i+3] == 'e'):
				if (i+5 < len(file_name) and valid(file_name, [i+1, i+2, i+4, i+5])):
					season = int(file_name[i+1:i+3])
					episode = int(file_name[i+4:i+6])
					break
		
		# 01x01
		if (file_name[i] == 'x'):
			if ((i+2)<len(file_name) and (i-2)>=0 and valid(file_name, [i+1,i+2, i-1, i-2])):
				season = int(file_name[i-2:i])
				episode = int(file_name[i+1:i+3])
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
					