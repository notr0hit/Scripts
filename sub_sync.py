import os

directory = os.getcwd()

#filter-subtitles
for filename in os.listdir(directory):
    if(filename.endswith(".srt")):
        os.system(f'python C:/Users/rohit/AppData/Local/Programs/Python/Python310/Scripts/filter-subtitles.py -s {filename}')
    else:
        continue

# script to rename and fix subtitles
os.system('python D:/Scripts/rename_subs.py')

#sync subtitles with audio track
for filename in os.listdir(directory):
    if (filename.endswith(".avi") or filename.endswith(".mp4") or filename.endswith(".mkv")) and ((filename[0:-4] + ".srt") in os.listdir(directory)):
        os.system(f'ffs {filename} -i {filename[0:-4]+".srt"} -o {filename[0:-4]+".srt"}')
    else:
        continue


# opensubtitle
# username: mind_f    
# password: 7MDdzvMj9n2!J@B