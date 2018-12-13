import os

# A
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:0:0" 07_shark_000.avi

# B
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:960:0" 07_shark_001.avi

# C
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:1920:0" 07_shark_002.avi


# D
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:2880:0" 07_shark_003.avi

# E
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:0:512" 07_shark_004.avi

# F
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:960:512" 07_shark_005.avi

# G
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:1920:512" 07_shark_006.avi

# H
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:2880:512" 07_shark_007.avi

# A
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:0:1024" 07_shark_008.avi

# B
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:960:1024" 07_shark_009.avi

# C
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:1920:1024" 07_shark_010.avi

# D
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:2880:1024" 07_shark_011.avi

# E
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:0:1536" 07_shark_012.avi

# F
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:960:1536" 07_shark_013.avi

# G
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:1920:1536" 07_shark_014.avi

# H
ffmpeg -i 07_shark.avi -vcodec rawvideo -filter:v "crop=960:512:2880:1536" 07_shark_015.avi
