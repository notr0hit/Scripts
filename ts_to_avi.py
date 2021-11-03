# ffmpeg -i input -map 0 -c copy output.mp4

import os
directory = 'E:\\IDM\\Movies'
for filename in os.listdir(directory):
    if filename.endswith(".ts") and ((filename[0:-3] + ".mkv") not in os.listdir(directory)):
        # ffmpeg -i input -map 0 -c copy output.mp4
        os.system(f'ffmpeg -i {directory}\\{filename} -map 0 -c copy {directory}\\{filename[0:-3] + ".mkv"}')
    else:
        continue