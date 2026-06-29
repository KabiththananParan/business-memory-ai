import cognee
import asyncio


async def main():
    result = await cognee.remember(
        "Supplier A caused delivery delays in January."
    )
    
    print(result)
    
    
if __name__ == "__main__":
    asyncio.run(main())
