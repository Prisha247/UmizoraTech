#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():

    print("-- Starting gyro calibration")
    async for progress_data in drone.calibration.calibrate_gyro():
        print(progress_data)

    print("-- Starting magneto calibration")
    async for progress_data in drone.calibration.calibrate_magnetometer():
        print(progress_data)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
