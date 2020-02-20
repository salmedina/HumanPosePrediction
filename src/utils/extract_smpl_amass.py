import argparse
import numpy as np
import os.path as osp
from pathlib import Path
from easydict import EasyDict as edict

def main(dataset_dir, output_dir, subseq_len):

    npz_path_list = [str(fp) for fp in Path(dataset_dir).rglob('*.npz')]

    for path_idx, npz_path in enumerate(npz_path_list):
        try:
            data = edict(np.load(npz_path))
        except:
            print(f'Could not open {npz_path}')
            continue

        relative_path = osp.relpath(npz_path, dataset_dir)
        save_path = osp.join(output_dir, relative_path)
        save_dir = osp.dirname(save_path)

        Path(save_dir).mkdir(parents=True, exist_ok=True)
        np.savez(save_path,
                 trans=data.trans[:, :subseq_len],
                 poses=data.poses[:, :subseq_len])

        if (path_idx % 1000) == 0:
            print(f'Extracted files {path_idx} / {len(npz_path_list)}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='Path to the AMASS dataset')
    parser.add_argument('--output_dir', type=str, help='Path to the output directory where the SMPL sequence and translation will be stored')
    parser.add_argument('--subseq_len', type=int, default=66, help='Subsequence length to be extracted')
    args = parser.parse_args()

    main(args.dataset_dir, args.output_dir, args.subseq_len)
