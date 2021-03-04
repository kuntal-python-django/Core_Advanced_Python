import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


