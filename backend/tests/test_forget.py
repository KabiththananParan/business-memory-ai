import asyncio
import cognee


async def main():
    print(f"Cognee version: {cognee.__version__}")
    print()

    print("Deleting all memory...")

    result = await cognee.forget(
        everything=True
    )

    print("\nforget() returned:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())