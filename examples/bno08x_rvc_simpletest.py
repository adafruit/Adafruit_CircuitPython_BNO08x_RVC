# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
from adafruit_bno08x_rvc import BNO08x_RVC

uart = busio.UART(board.TX, board.RX, baudrate=115200, receiver_buffer_size=2048)
rvc = BNO08x_RVC(uart)
while True:
    print("Roll: %2.2f Pitch: %2.2f Yaw: %2.2f Degrees Accel-X: %2.2f Accel-Y: %2.2f Accel-Z: %2.2f m/s^2"%rvc.heading)
    time.sleep(0.1)

