# Instalação OpenCV na Raspberry Pi

<img src="imagens\opencv.png" alt="logo">

> Créditos e Conteúdo do site: https://qengineering.eu/install-opencv-4.1-on-raspberry-pi-4.html

Apenas notas de estudo.

## Operating Systen

        $ sudo apt-get update
        $ sudo apt-get upgrade

As explained here, the physical RAM chip is used both by the CPU and the GPU. On a Raspberry Pi 2 or 3 default is 64 Mbyte allocated for the GPU. This can be somewhat small for vision projects. To increase the amount of memory for the GPU, use the following command. On a Raspberry Pi 4, there is 128 Mbyte given to the GPU. It is not necessary to change this at first.

        $ sudo raspi-config

After altering the amount to at least 128 the system asks you to reboot, so let's do that.

## Cleaning

The full OpenCV package takes about 5.5 Gbyte on your SD card. Raspbian itself is about 5.4 Gbyte. Time to make some space on your card by simply removing programs you likely not want to use. The most simple and safe way to do this is by the main menu. <br>
We have removed the following software packages: BlueJ, Claws Mail, Greenfoot, LibreOffice, Mathematica, Minecraft, Node-RED, Scratch, Strach2, Sense HAT, SmartSim, and Sonic Pi. This action frees about 2.5 Gbytes. However, leave at any time Mu and Python Games together with Thonny on your system! In the beginning, we deleted them also in the urge for more memory. But somehow too many Python packages are then removed and OpenCV could no longer generate a proper Python library.
Once all the unnecessary packages are removed, two last instructions finish this action.

        $ sudo apt-get clean
        $ sudo apt-get autoremove

        $ sudo apt-get install build-essential cmake git unzip pkg-config
        $ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
        $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
        $ sudo apt-get install libgtk2.0-dev libcanberra-gtk*
        $ sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev
        $ sudo apt-get install python3-dev python3-numpy
        $ sudo apt-get install python-dev python3-pip python-numpy
        $ sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev
        $ sudo apt-get install libv4l-dev v4l-utils
        $ sudo apt-get install libjasper-dev libopenblas-dev libatlas-base-dev libblas-dev
        $ sudo apt-get install liblapack-dev gfortran
        $ sudo apt-get install gcc-arm*
        $ sudo apt-get install protobuf-compiler

## Download OpenCV

When all third-party software is installed, OpenCV itself can be downloaded. There are two packages needed; the basic version and the additional contributions. Check before downloading the latest version at https://opencv.org/releases/. If necessary, change the names of the zip files according to the latest version. After downloading, you can unzip the files.

        $ cd ~
        $ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.2.zip
        $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.2.zip
        $ unzip opencv.zip
        $ unzip opencv_contrib.

The next step is some administration. First, rename your directories with more convenient names like opencv and opencv_contrib. This makes live later on easier. Next, make a directory where all the build files are located.

        $ mv opencv-4.1.2 opencv
        $ mv opencv_contrib-4.1.2 opencv_contrib

        $ cd ~/opencv/
        $ mkdir build
        $ cd build

## Build Make

        $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
                -D CMAKE_INSTALL_PREFIX=/usr/local \
                -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
                -D ENABLE_NEON=ON \
                -D ENABLE_VFPV3=ON \
                -D WITH_OPENMP=ON \
                -D BUILD_TIFF=ON \
                -D WITH_FFMPEG=ON \
                -D WITH_GSTREAMER=ON \
                -D WITH_TBB=ON \
                -D BUILD_TBB=ON \
                -D BUILD_TESTS=OFF \
                -D WITH_EIGEN=OFF \
                -D WITH_V4L=ON \
                -D WITH_LIBV4L=ON \
                -D WITH_VTK=OFF \
                -D OPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic \
                -D OPENCV_ENABLE_NONFREE=ON \
                -D INSTALL_C_EXAMPLES=OFF \
                -D INSTALL_PYTHON_EXAMPLES=OFF \
                -D BUILD_NEW_PYTHON_SUPPORT=ON \
                -D BUILD_opencv_python3=TRUE \
                -D OPENCV_GENERATE_PKGCONFIG=ON \
                -D BUILD_EXAMPLES=OFF ..

If everything went well, CMake generates a report that looks something like this (for readability purposes we omitted most lines). Very crucial are the Python sections. If these are missing, OpenCV will not install proper Python libraries. Most of the time CMake could not find the Python directories in that case. We are experiencing these issues when removing too many packages from the operating system, as mentioned earlier. Also, NEON and VFPV3 support must be enabled if you are planning to build our deep learning applications. Check if v4l/v4l2 is available if your planning to use the Raspicam.


    -- General configuration for OpenCV 4.1.2 =====================================
    --   Version control:               unknown
    --
    --   Extra modules:
    --     Location (extra):            /home/pi/opencv_contrib/modules
    --     Version control (extra):     unknown
    --
    --   Platform:
    --     Timestamp:                   2019-10-18T12:15:44Z
    --     Host:                        Linux 4.19.66-v7+ armv7l
    --     CMake:                       3.13.4
    --     CMake generator:             Unix Makefiles
    --     CMake build tool:            /usr/bin/make
    --     Configuration:               RELEASE
    --
    --   CPU/HW features:
    --     Baseline:                    VFPV3 NEON
    --       requested:                 DETECT
    --       required:                  VFPV3 NEON
    --
    --   C/C++:
    --     Built as dynamic libs?:      YES
    --     C++ Compiler:                /usr/bin/c++  (ver 8.3.0)
    ***********************
    --     C Compiler:                  /usr/bin/cc
    ***********************
    --     Documentation:               NO
    --     Non-free algorithms:         YES
    ***********************
    --   Video I/O:
    --   DC1394:                      YES (2.2.5)
    --   FFMPEG:                      YES
    --     avcodec:                   YES (58.35.100)
    --     avformat:                  YES (58.20.100)
    --     avutil:                    YES (56.22.100)
    --     swscale:                   YES (5.3.100)
    --     avresample:                NO
    --   GStreamer:                   NO
    --   v4l/v4l2:                    YES (linux/videodev2.h)
    ***********************
    --   Python 2:
    --     Interpreter:                 /usr/bin/python2.7 (ver 2.7.16)
    --     Libraries:                   /usr/lib/arm-linux-gnueabihf/libpython2.7.so (ver 2.7.16)
    --     numpy:                       /usr/lib/python2.7/dist-packages/numpy/core/include (ver 1.16.2)
    --     install path:                lib/python2.7/dist-packages/cv2/python-2.7
    --
    --   Python 3:
    --     Interpreter:                 /usr/bin/python3 (ver 3.7.3)
    --     Libraries:                   /usr/lib/arm-linux-gnueabihf/libpython3.7m.so (ver 3.7.3)
    --     numpy:                       /usr/lib/python3/dist-packages/numpy/core/include (ver 1.16.2)
    --     install path:                lib/python3.7/dist-packages/cv2/python-3.7
    --
    --   Python (for build):            /usr/bin/python2.7
    ***********************
    --   Install to:                    /usr/local
    -- -----------------------------------------------------------------

Another issue we came across was the missing of the c++ compiler. CMake generated the screen dump below. By simply giving the Cmake command a second time, the problem was solved. In rare occasions, we had to sudo apt-get update and upgrade the system before CMake could find the c++ compiler.


    -- The CXX compiler identification is GNU 8.3.0
    -- The C compiler identification is GNU 8.3.0
    -- Check for working CXX compiler: /usr/bin/c++
    -- Check for working CXX compiler: /usr/bin/c++ -- broken
    CMake Error at /usr/share/cmake-3.13/Modules/CMakeTestCXXCompiler.cmake:45 (message):
    The C++ compiler

    "/usr/bin/c++"

    is not able to compile a simple test program.
    ***********************
    -- Configuring incomplete, errors occurred!
    See also "/home/pi/opencv/build/CMakeFiles/CMakeOutput.log".
    See also "/home/pi/opencv/build/CMakeFiles/CMakeError.log".

Before we can start the actual build, the memory swap space needs to be enlarged. For daily use a swap memory of 100 Mbyte is sufficient. However, with the massive build ahead of use, extra memory space is crucial. Enlarge the swap space with the following command.

        $ sudo nano /etc/dphys-swapfile

This command opens Nano, a very lightweight text editor, with the system file dphys-swapfile. With the arrow keys, you can move the cursor to the CONF_SWAPSIZE line where the new value 4096 can be entered. Next, close the session with the <Ctrl+X> key combination. With <Y> and <Enter> changes are being saved in the same file.


        $ sudo /etc/init.d/dphys-swapfile stop
        $ sudo /etc/init.d/dphys-swapfile start

## Make

Now everything is ready for the great build. This takes a lot of time. Be very patient is the only advice here. Don't be surprised if at 100% your build seems to be crashed. That is 'normal' behaviour. Even when your CPU Usage Monitor gives very low ratings like 7%. In reality, your CPU is working so hard it has not enough time to update these usage numbers correctly.
You can speed things up with four cores working simultaneously (make -j4). On a Raspberry Pi 4, it takes just over an hour to build the whole library. Sometimes the system crashes for no apparent reason at all at 99% or even 100%. In that case, restart all over again, as explained at the end of this page, and rebuild with make -j1.
Probably you get a whole bunch of warnings during the make. Don't pay to much attention to it. They are generated by subtle differences in template overload functions due to little version differences. So take coffee and a good book for reading, and start building with the next command.


        $ make -j4
        $ sudo make install
        $ sudo ldconfig
        $ sudo apt-get update   


        $ sudo nano /etc/dphys-swapfile

set CONF_SWAPSIZE=100 with the Nano text editor

        $ sudo reboot