import argparse
import numpy as np
import os.path as osp
from glob import glob
from pathlib import Path
from easydict import EasyDict as edict

def main(dataset_dir, output_dir, target_framerate):

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
        if data.mocap_framerate < target_framerate:
            print(f'Cannot downsample [{data.mocap_framerate}]: {relative_path}')
            continue
        elif data.mocap_framerate == target_framerate:
            Path(save_dir).mkdir(parents=True, exist_ok=True)
            np.savez(osp.join(output_dir, relative_path),
                     trans=data.trans,
                     gender=data.gender,
                     mocap_framerate=data.mocap_framerate,
                     betas=data.betas,
                     dmpls=data.dmpls,
                     poses=data.poses)
            continue

        orig_num_frames = data.poses.shape[0]
        sampling_step = data.mocap_framerate / target_framerate
        downsampled_frame_idx = np.round(np.arange(0, orig_num_frames, sampling_step)).astype(int)
        if downsampled_frame_idx[-1] == orig_num_frames:
            downsampled_frame_idx[-1] -= 1

        downsampled_trans = np.take(data.trans, downsampled_frame_idx, axis=0)
        downsampled_dmpls = np.take(data.dmpls, downsampled_frame_idx, axis=0)
        downsampled_poses = np.take(data.poses, downsampled_frame_idx, axis=0)

        Path(save_dir).mkdir(parents=True, exist_ok=True)
        np.savez(save_path,
                 trans=downsampled_trans,
                 gender=data.gender,
                 mocap_framerate=float(target_framerate),
                 betas=data.betas,
                 dmpls=downsampled_dmpls,
                 poses=downsampled_poses)

        if (path_idx % 1000) == 0:
            print(f'Downsampled files {path_idx} / {len(npz_path_list)}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, help='Path to the AMASS dataset')
    parser.add_argument('--target_fr', type=int, help='Target frame rate to which we want to downsample the dataset')
    parser.add_argument('--output_dir', type=str, help='Path to the output directory where the dataset will be downsampled')
    args = parser.parse_args()

    main(args.dataset_dir, args.output_dir, args.target_fr)