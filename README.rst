Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-bno08x_rvc/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/bno08x_rvc/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_BNO08x_RVC/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_BNO08x_RVC/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A simple helper library for using the UART-RVC mode of the BNO08x IMUs


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-bno08x_rvc/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-bno08x-rvc

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-bno08x-rvc

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-bno08x-rvc

Usage Example
=============

.. code-block:: python3

    import time
    import board
    import busio
    from adafruit_bno08x_rvc import BNO08x_RVC

    uart = busio.UART(board.TX, board.RX, baudrate=115200, receiver_buffer_size=2048)
    rvc = BNO08x_RVC(uart)
    while True:
        roll, pitch, yaw, x_accel, y_accel, z_accel = rvc.heading
        print("Roll: %2.2f Pitch: %2.2f Yaw: %2.2f Degrees" % (roll, pitch, yaw))
        print("Acceleration X: %2.2f Y: %2.2f Z: %2.2f m/s^2" % (x_accel, y_accel, z_accel))
        print("")
        time.sleep(0.1)

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/bno08x_rvc/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_BNO08x_RVC/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
