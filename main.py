import asyncio


async def good():
    print("Начата")
    return 1


async def bad():
    print("Начата")
    raise ValueError("Error")
    # return 1


async def main():
    try:
        result = await asyncio.gather(bad(), good(), return_exceptions=True)
        print(result)
    except ValueError as e:
        print(e)


asyncio.run(main())
