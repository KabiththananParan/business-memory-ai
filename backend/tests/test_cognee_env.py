import os
from dotenv import load_dotenv

load_dotenv()

print("Neo4j:", os.getenv("NEO4J_URI"))
print("Qdrant:", os.getenv("QDRANT_URL"))
print("Postgres:", os.getenv("POSTGRES_DB"))

import cognee

print("Cognee Version:", cognee.__version__)
print("Cognee loaded successfully")