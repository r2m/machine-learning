# machine-learning
Machine Learning Meetup

In this tutorial we will use the following development tools:

 * Python 2.7.x
 * Numpy 1.x
 * OpenCV 2.x

## installation

### Windows

 1. Download the latest Python 2.7 Windows installer from https://www.python.org/downloads/release/python-2711/
 2. Install Anaconda (contains numpy, scipy and scikit): https://www.continuum.io/downloads/
 3. From now on, you  need to use the python.exe provided by anaconda. You can choose between calling anacondas python.exe directly with parameters from its folder, 
    or set the global PYTHON_HOME the directory <PathToAnacondaRoot> where anacondas python.exe resides, as well as adding <PathToAnacondaRoot> and <PathToAnacondaRoot>/Scripts 
    to the Windows PATH variable.
 3. Download and install the latest OpenCV distribution from here: http://opencv.org/downloads.html
 4. Manually copy the file opencv\build\python\2.7\xNN\cv2.pyd to the Lib\site-packages\ directory of your Python installation (where xXX is x86 or x64)
 5. Verify the installation (instructions below)
 
### Mac

We recommend installing Python and OpenCV using homebrew.

 1. Install homebrew from: http://brew.sh/
 2. Install python: 'brew install python'
 3. Open a new shell (to upgrade the path and environment)
 4. Type: 'which python'
 5. Make sure that the response is: 'usr/local/bin/python', otherwise retry...
 6. Upgrade pip 'pip install --upgrade pip'
 7. Install science tap in homebrew: 'brew tap homebrew/science/'
 8. Install OpenCV: 'brew install opencv'
 9. Install OpenCV python extensions: 'echo /usr/local/opt/opencv/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/opencv.pth'
10. pip install scipy
11. pip install scikit-learn 
12. Verify the installation (instructions below)

## Verify installation

 * Run: 'python'
 * Type: 'import cv2'
 * Type: 'cv2.__version__'
 * The result should be the version of OpenCV currently installed (2.x)
 * Verify scipy installation by typing: 'import scipy'
 * Verify scikit-learn installation by typing: 'import sklearn'
If it doesn't work, try opening a new shell to make sure that the right defaults have been loaded!

If it still doesn't work, please contact us so we can help!
