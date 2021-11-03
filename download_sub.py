import os
directory = os.getcwd()
for filename in os.listdir(directory):
    # subtitler Cars.avi --lang en_us LANG=en_us subtitler Cars.avi
    if (filename.endswith(".avi") or filename.endswith(".mp4") or filename.endswith(".mkv")) and ((filename[0:-4] + ".srt") not in os.listdir(directory)):
        os.system(f'subtitler {filename[0:-4]} --lang eng {filename} -n 1 --download')
    else:
        continue