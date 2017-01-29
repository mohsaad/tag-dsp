from __future__ import print_function
from __future__ import division

import platform
import numpy as np
import config


_gamma = np.load(config.GAMMA_TABLE_PATH)
"""Gamma lookup table used for nonlinear brightness correction"""

_prev_pixels = np.tile(253, (3, config.N_PIXELS))
"""Pixel values that were most recently displayed on the LED strip"""

pixels = np.tile(1, (3, config.N_PIXELS))
"""Pixel values for the LED strip"""


def _update_none():
    ''' Writes values for the visualizer without any output'''
    global pixels, prev_pixels
    # Truncate values and cast to integer
    pixels = np.clip(pixels, 0, 255).astype(int)
    # Optionally apply gamma correctio
    p = _gamma[pixels] if config.SOFTWARE_GAMMA_CORRECTION else np.copy(pixels)
    _prev_pixels = np.copy(p)


def update():
    """Updates the LED visualization values values"""
    _update_none()


# Execute this file to run a LED strand test
# TODO: Extend this to the Adafruit LED strips connected via arduino!
if __name__ == '__main__':
    import time
    # Turn all pixels off
    pixels *= 0
    pixels[0, 0] = 255  # Set 1st pixel red
    pixels[1, 1] = 255  # Set 2nd pixel green
    pixels[2, 2] = 255  # Set 3rd pixel blue
    print('Starting LED strand test')
    while True:
        pixels = np.roll(pixels, 1, axis=1)
        update()
        time.sleep(1)
