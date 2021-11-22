# ffmpeg -i input.xyz -map 0 -c copy output.mp4

import os
import sys
directory = os.getcwd()

input_extension = '.'+sys.argv[1];
output_extension = '.'+sys.argv[2];

for filename in os.listdir(directory):
    if filename.endswith(input_extension):
        # ffmpeg -i input -map 0 -c copy output.mp4
        os.system(f'ffmpeg -i {filename} -map 0 -c copy {filename[0:-3] + output_extension}')
    else:
        continue