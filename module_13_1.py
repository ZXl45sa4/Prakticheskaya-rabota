import asyncio


async def start_strongman(name, power):
    n = 1
    print(f"'Силач {name} начал соревнования.'")
    while n < 6:
        await asyncio.sleep(1 / power)
        print(f"'Силач {name} поднял {n}'")
        n += 1
    print(f"'Силач {name} закончил соревнования.'")


async def main():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


asyncio.run(main())
