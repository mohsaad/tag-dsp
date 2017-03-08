# TAG-DSP Audio LED Strips

To get this software working, follow these steps:


# Anaconda
Install Miniconda/Anaconda for your platform. Choose Python3 when chosing your platform. https://conda.io/miniconda.html

Open up a command line or terminal, and run the following command to create a new environment: 

`conda create --name led-env python=3.5`

Activate the environment by running 

`activate led-env`

# Libraries needed

Install the following libraries:

* Qt (https://www.qt.io/)
* Python libraries

Run the following command in your command line
`conda install numpy scipy pyqtgraph pyserial`

* PyAudio
Install this by running in your command line:
`pip install PyAudio`

You may need PortAudio, which you can download from http://www.portaudio.com/download.html

# Running
To run the software, just run python python/visualization.py from the root of the directory.

Credit goes to Scott Lawson for making the visualizer and most of the code.