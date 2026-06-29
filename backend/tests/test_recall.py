import asyncio
import os

from dotenv import load_dotenv
import cognee

load_dotenv()


async def main():
    print(f"Cognee version: {cognee.__version__}")
    print()

    query = "Which supplier caused delivery delays?"

    print(f"Query: {query}")
    print()

    result = await cognee.recall(query)

    print("Recall result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())