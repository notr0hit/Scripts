# ffmpeg -i input.xyz -map 0 -c copy output.mp4

import os
directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(".ts") and ((filename[0:-3] + ".mkv") not in os.listdir(directory)):
        # ffmpeg -i input -map 0 -c copy output.mp4
        os.system(f'ffmpeg -i {filename} -map 0 -c copy {filename[0:-3] + ".avi"}')
    else:
        continue