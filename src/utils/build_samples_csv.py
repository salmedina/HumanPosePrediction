import argparse
import pandas as pd
import os.path as osp

def main(input_path, x_frames, y_frames, output_path):
    data = pd.read_csv(input_path, names=['rel_path', 'frames', 'seconds'])

    output_list = list()
    for idx, row in data.iterrows():
        num_motion_frames = row['frames']
        for x_start in range(0, num_motion_frames, 25):
            x_end = x_start + x_frames - 1
            y_start = x_start + x_frames
            y_end = y_start + y_frames
            if y_end < num_motion_frames:
                sample = (row['rel_path'], x_start, x_end, y_start, y_end)
                output_list.append(sample)

        if (idx % 1000) == 0:
            print(f'Number of file read {idx} / {len(data)}')

    with open(output_path, 'w') as output_file:
        output_file.write('\n'.join([f'{rel_path},{xs},{xe},{ys},{ye}' for rel_path, xs, xe, ys, ye in output_list]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filtered_csv', type=str, help='Path csv with filtered data')
    parser.add_argument('--input_len', type=int, help='Number of frames for input')
    parser.add_argument('--output_len', type=int, help='Number of frames for output')
    parser.add_argument('--output_csv', type=str, help='Path to the output csv path with the samples')
    args = parser.parse_args()

    main(args.filtered_csv, args.input_len, args.output_len, args.output_csv)