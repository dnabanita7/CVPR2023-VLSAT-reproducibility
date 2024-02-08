# 3RScan Library and Renderer

In the following we give detailed information on how to process files in 3RScan from the [paper](https://arxiv.org/abs/1908.06109) RIO: 3D Object Instance Re-Localization in Changing Indoor Environments. We provide a c++ library [rio_lib](https://github.com/WaldJohannaU/3RScan/tree/master/c++/rio_lib/src/rio_lib), an [example](https://github.com/WaldJohannaU/3RScan/tree/master/c++/rio_lib/src/example) project as well as a [rendering application](https://github.com/WaldJohannaU/3RScan/tree/master/c++/rio_renderer) to generate 2D renderings with semantics, depth or RGB.

## Getting Started

Before starting to use the code, some scenes of 3RScan needs to be downloaded, to do so please fill out [this form](https://forms.gle/NvL5dvB4tSFrHfQH6). To download example data to test the provided toolkit simply run [setup.sh](https://github.com/WaldJohannaU/3RScan/tree/master/setup.sh).

This downloads a rescan and it's corresponding reference and prepares the required directory structure as follows:

```
3RScan // this respository locally
├── setup.sh
├── README.md
├── FAQ.md
├── data
│	├── 3RScan
│	│	├── 4acaebcc-6c10-2a2a-858b-29c7e4fb410d
│	│	│	├── sequence
│	│	│	│	├── _info.txt
│	│	│	│	├── frame-000000.color.jpg
│	│	│	│	├── frame-000000.depth.pgm
│	│	│	│	├── frame-000000.pose.txt
│	│	│	│	└── ...
│	│	│	├── labels.instances.annotated.v2.ply
│	│	│	├── mesh.refined.v2.obj
│	│	│	├── mesh.refined_0.png
│	│	│	└── semseg.v2.json
│	│	└── 754e884c-ea24-2175-8b34-cead19d4198d
│	├── 3RScan.json
│	└── objects.json
└── ...
```

## 3RScan Library Dependencies

[OpenCV](https://github.com/opencv/opencv) and [Eigen](https://github.com/libigl/eigen) are required in order to be able to compile and run our example code. You can either build the dependencies from source or use the package manager of your choice e.g. ``brew`` on macOS to install the packages. Once you installed OpenCV and Eigen run:

```bash
  cd rio_lib
  mkdir build
  cd build
  cmake -DCMAKE_BUILD_TYPE=Release ..
  make
```

To run the sample application simply do:

```bash  
  ./bin/rio_example <3RScan_path> <scan_id>
  ./bin/rio_example ../../../data/3RScan 754e884c-ea24-2175-8b34-cead19d4198d
```

Our renderer application additionally requires OpenGL, GLFW3, GLEW, [Assimp](https://github.com/assimp/assimp) and glm (libglfw3-dev, libglew-dev, libassimp-dev and libglm-dev). Once installed, it also builds as follows:

```bash
  cd rio_renderer
  mkdir build
  cd build
  cmake -DCMAKE_BUILD_TYPE=Release ..
  make
```

```bash
  ./rio_renderer <3RScan_path> <scan_id> <output_folder>
  ./rio_renderer ../../../data/3RScan 754e884c-ea24-2175-8b34-cead19d4198d sequence
```

Our renderer application offers an additional binary that renders all artifacts (bounding-box file; rendered rgb, label, instance and depth image; occlusion scores for each object) for each frame in a scan:

```bash
  ./rio_renderer_render_all <3RScan_path> <scan_id> <output_folder> <render_mode>
  ./rio_renderer_render_all ../../../data/3RScan 754e884c-ea24-2175-8b34-cead19d4198d sequence 1
```

## Citation

If you find this useful, please consider citing the corresponding publication:

```
@inproceedings{Wald2019RIO,
	title={RIO: 3D Object Instance Re-Localization in Changing Indoor Environments},
	author={Johanna Wald, Armen Avetisyan, Nassir Navab, Federico Tombari, Matthias Niessner},
	journal={Proceedings IEEE International Conference on Computer Vision (ICCV)},
	year={2019}
}
```

## Contact

If you have questions checks out our [FAQ](https://github.com/WaldJohannaU/3RScan/tree/master/FAQ.md) or send me an [email](mailto:johanna.wald@tum.de) if things are still unclear. We are constantly working on improving our dataset and code, so stay tuned!

## Notes:
* Please see our [project page](https://waldjohannau.github.io/RIO) for more information.
* Our code uses [json11](https://github.com/dropbox/json11), [tinyobjloader](https://github.com/tinyobjloader/tinyobjloader) and [tinyply](https://github.com/ddiakopoulos/tinyply)
