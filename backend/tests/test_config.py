from app.core.config import load_settings

def main():
    print("\n=== Testing Configuration Loading ===\n")
    
    print("Loading settings...")
    settings = load_settings()
    
    print("✓ load_settings() executed")
    
    print("\nVerifying configuration groups...")
    
    assert settings.app is not None
    assert settings.llm is not None
    assert settings.embeddings is not None
    assert settings.cognee is not None
    assert settings.postgres is not None
    assert settings.neo4j is not None
    assert settings.qdrant is not None
    assert settings.logging is not None

    print("✓ settings.app")
    print("✓ settings.llm")
    print("✓ settings.embeddings")
    print("✓ settings.cognee")
    print("✓ settings.postgres")
    print("✓ settings.neo4j")
    print("✓ settings.qdrant")
    print("✓ settings.logging")
    
    
    print("\n=== Sample Values ===")

    print(f"Application Name : {settings.app.app_name}")
    print(f"LLM Model       : {settings.llm.model}")
    print(f"Neo4j URI       : {settings.neo4j.uri}")
    print(f"Qdrant URL      : {settings.qdrant.url}")
    print(f"Cognee Env      : {settings.cognee.environment}")

    print("\n✓ Configuration loaded successfully")


if __name__ == "__main__":
    main()