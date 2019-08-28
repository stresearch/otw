# Extract frames from either the Homes or Lots directory.
# Python3.x required
#
# usage:
#   pip3 install imageio imageio-ffmpeg
#   python3 extract_frames.py

import os
import imageio
import sys
from multiprocessing import Pool

def _extract_frames(argtuple):
    # Arguments for multiprocessing map
    (videopath, tgtDir, compress_level) = argtuple

    # Create a target directory
    if not os.path.exists(tgtDir):
        print('Creating directory: "%s"' % tgtDir)
        os.mkdir(tgtDir)

    # Extract frames using imageio-ffmpeg plugin
    reader = imageio.get_reader(videopath)
    print('Extracting video: %s to %s' % (videopath, tgtDir))
    for idx,im in enumerate(reader):
        f = os.path.join(tgtDir, '%08d.png' % idx)
        imageio.imwrite(f, im, format='PNG-PIL', compress_level=compress_level)

def parallelize(dataset='homes', n_pool=10, compress_level=5):
    srcDir = os.path.join('.', dataset, 'video')
    tgtDir = os.path.join('.', dataset, 'frames')
    videopaths = [os.path.join(srcDir, v) for v in os.listdir(srcDir)]
    Pool(n_pool).map(_extract_frames, [(v, os.path.splitext(v)[0].replace('video','frames'), compress_level) for v in videopaths])
    
if __name__ == '__main__':
    dataset = sys.argv[1] if len(sys.argv) > 1 else 'homes'
    n_pool = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    compress_level = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    parallelize(dataset=dataset, n_pool=n_pool, compress_level=compress_level)

