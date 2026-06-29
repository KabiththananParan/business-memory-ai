import asyncio
import cognee


async def main():
    print(f"Cognee version: {cognee.__version__}")
    print()

    print("Running improve()...")
    
    result = await cognee.improve()

    print("\nimprove() returned:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())