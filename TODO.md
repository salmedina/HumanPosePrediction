### Dataset Tasks

-[X] Downsample data
-[X] Filter out by duration of minimum 3.5 secs or 175 frames @ 50 FPS
-[X] Calculate statistics of filtered data
-[X] Create csv of samples (no overlap):
    - path
    - x_start
    - x_end
    - y_start
    - y_end
-[X] Sample 100k samples
-[X] Get statistics of 100k samples
-[ ] Build dataloader
-[ ] Train model
-[ ] Fine-tune hyperparams


### Devel Notes

Could not open these files while downsampling

```
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/29/29_01_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/29/29_04_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/29/29_08_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/29/29_10_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/29/29_17_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_11_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_18_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_25_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_48_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_51_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_56_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_58_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_59_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_74_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_83_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_84_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_89_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/79/79_95_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_01_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_02_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_04_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_06_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_07_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_08_poses.npz
Could not open /mnt/Alfheim/Data/AMASS/NPZ/CMU/CMU/140/140_09_poses.npz
No mocap framerate: DFaust_67 2/50002/shape.npz
No mocap framerate: DFaust_67 2/50004/shape.npz
No mocap framerate: DFaust_67 2/50007/shape.npz
No mocap framerate: DFaust_67 2/50009/shape.npz
No mocap framerate: DFaust_67 2/50020/shape.npz
No mocap framerate: DFaust_67 2/50021/shape.npz
No mocap framerate: DFaust_67 2/50022/shape.npz
No mocap framerate: DFaust_67 2/50025/shape.npz
No mocap framerate: DFaust_67 2/50026/shape.npz
No mocap framerate: DFaust_67 2/50027/shape.npz
```


