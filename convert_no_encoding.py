# ffmpeg -i input.xyz -map 0 -c copy output.mp4

import os
import sys
directory = os.getcwd()

input_extension = '.'+sys.argv[1];
output_extension = '.'+sys.argv[2];

for filename in os.listdir(directory):
    if filename.endswith(input_extension):
        file_name = os.path.splitext(filename)[0]
        # ffmpeg -i input -map 0 -c copy output.mp4
        os.system(f'ffmpeg -i {filename} -map 0 -c copy {file_name + output_extension}')
    else:
        continue