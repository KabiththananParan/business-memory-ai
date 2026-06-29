import asyncio
import cognee


async def main():
    # Print Cognee version
    print(f"Cognee version: {cognee.__version__}")

    # Store a small business fact
    result = await cognee.remember(
        "Supplier A caused delivery delays in January."
    )

    # Print what remember() returns
    print("\nremember() returned:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())