import asyncio
import time 

async def create_clock():
    while True:
        print(time.strftime("%H:%M:%S", time.localtime()))   

        """
        pauses the execution of the current task for 1 sec, allowing other tasks to run concurrently, this is used in an asynchronous env to prevent blocking the event loop and to allow other tasks to execute while waiting for the next clock update
        """
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(create_clock())
