# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
`adafruit_bno08x_rvc`
================================================================================

A simple helper library for using the UART-RVC mode of the BNO08x IMUs

* Author(s): Bryan Siepert

Implementation Notes
--------------------

**Hardware:**

* `Adafruit 9-DOF Orientation IMU Fusion Breakout - BNO085 (BNO080)
  <https://www.adafruit.com/product/4754>`_ (Product ID: 4754)


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""
import time
from struct import unpack_from

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BNO08x_RVC.git"


class RVCReadTimeoutError(Exception):
    """Raised if a UART-RVC message cannot be read before the given timeout"""


class BNO08x_RVC:
    """A simple class for reading heading from the BNO08x IMUs using the UART-RVC mode

    :param uart: The UART device the BNO08x_RVC is connected to.
    :param float timeout: time to wait for readings. Defaults to :const:`1.0`


    **Quickstart: Importing and using the device**

        Here is an example of using the :class:`BNO08X_UART` class.
        First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            import busio
            from adafruit_bno08x_rvc import BNO08x_RVC

        Once this is done you can define your `busio.UART` object and define your sensor object

        .. code-block:: python

            uart = busio.UART(board.TX, board.RX, baudrate=3000000, receiver_buffer_size=2048)
            rvc = BNO08X_UART(uart)


        Now you have access to the :attr:`heading` attribute

        .. code-block:: python

            yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading

    """

    def __init__(self, uart, timeout=1.0):
        self._uart = uart
        self._debug = True
        self._read_timeout = timeout

    @staticmethod
    def _parse_frame(frame):
        heading_frame = unpack_from("<BhhhhhhBBBB", frame)
        (
            _index,
            yaw,
            pitch,
            roll,
            x_accel,
            y_accel,
            z_accel,
            _res1,
            _res2,
            _res3,
            _checksum,
        ) = heading_frame
        checksum_calc = sum(frame[0:16]) % 256
        if checksum_calc != _checksum:
            return None
        yaw *= 0.01
        pitch *= 0.01
        roll *= 0.01
        x_accel *= 0.0098067
        y_accel *= 0.0098067
        z_accel *= 0.0098067
        return (yaw, pitch, roll, x_accel, y_accel, z_accel)

    @property
    def heading(self):
        """The current heading made up of

        * Yaw
        * Pitch
        * Roll
        * X-Axis Acceleration
        * Y-Axis Acceleration
        * Z-Axis Acceleration

        """
        # try to read initial packet start byte
        data = None
        start_time = time.monotonic()
        while time.monotonic() - start_time < self._read_timeout:
            data = self._uart.read(2)
            # print("data", data)
            if data[0] == 0xAA and data[1] == 0xAA:
                msg = self._uart.read(17)
                heading = self._parse_frame(msg)
                if heading is None:
                    continue
                return heading
        raise RVCReadTimeoutError("Unable to read RVC heading message")
