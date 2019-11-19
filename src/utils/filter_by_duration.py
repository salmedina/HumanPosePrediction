import argparse
import numpy as np
import os.path as osp
from glob import glob
from pathlib import Path
from easydict import EasyDict as edict

def main(dataset_dir, min_duration, output_path):
    npz_path_list = [str(fp) for fp in Path(dataset_dir).rglob('*.npz')]

    duration_list = list()
    for path_idx, npz_path in enumerate(npz_path_list):
        try:
            data = edict(np.load(npz_path))
        except:
            print(f'Could not open {npz_path}')
            continue

        relative_path = osp.relpath(npz_path, dataset_dir)
        num_frames = len(data.poses)
        duration = num_frames / data.mocap_framerate
        if duration >= min_duration:
            duration_list.append((relative_path, num_frames, duration))

        if (path_idx % 1000) == 0:
            print(f'Number of file read {path_idx} / {len(npz_path_list)}')

    with open(output_path, 'w') as output_file:
        output_file.write('\n'.join([f'{rel_path},{num_frames},{duration:.2f}' for rel_path, num_frames, duration in duration_list]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='Path to the data directory to be filtered')
    parser.add_argument('--min_duration', type=float, help='Minimum duration of the sample in seconds')
    parser.add_argument('--output_csv', type=str, help='Path to the csv file that lists the filtered data along with their duration in frames')
    args = parser.parse_args()

    main(args.dataset_dir, args.min_duration, args.output_csv)