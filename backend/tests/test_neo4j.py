from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "neo4j://127.0.0.1:7687",
    auth=("neo4j", "businessmemory123")
)

with driver.session(database="business-memory") as session:
    result = session.run("RETURN 'Connected'")
    print(result.single()[0])

driver.close()