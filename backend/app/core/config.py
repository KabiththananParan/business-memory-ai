from pydantic import BaseModel


class ApplicationConfig(BaseModel):
    app_name: str
    app_version: str
    debug: bool
    
class LLMConfig(BaseModel):
    provider: str
    model: str
    api_key: str
    
    
class EmbeddingConfig(BaseModel):
    provider: str
    model: str
    dimension: int


class CogneeConfig(BaseModel):
    environment: bool
    dataset_name: str
    api_key: str
    
class PostgresConfig(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str


class Neo4jConfig(BaseModel):
    uri: str
    username: str
    password: str


class QdrantConfig(BaseModel):
    url: str
    api_key: int
    collection_name: str


class LoggingConfig(BaseModel):
    level: str
    format: str
    file_path: str
    

    
    
    
class Settings(BaseModel):
    app: ApplicationConfig

    llm: LLMConfig
    
    embeddings: EmbeddingConfig

    cognee: CogneeConfig

    postgres: PostgresConfig

    neo4j: Neo4jConfig

    qdrant: QdrantConfig

    logging: LoggingConfig
    