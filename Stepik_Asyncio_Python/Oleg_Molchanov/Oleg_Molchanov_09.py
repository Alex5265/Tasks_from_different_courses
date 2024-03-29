import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)



async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task_1 = asyncio.ensure_future(print_nums())
    task_2 = asyncio.ensure_future(print_time())

    await asyncio.gather(task_1, task_2)




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
