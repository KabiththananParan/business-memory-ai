from pydantic import BaseModel


class ApplicationConfig(BaseModel):
    app_name: str
    app_version: str
    debug: bool
    environment: str
    port: int
    
    
class LLMConfig(BaseModel):
    provider: str
    model: str
    api_key: str
    temperature: float
    max_tokens: int
    top_p: float
    timeout: int
    
    
class EmbeddingConfig(BaseModel):
    provider: str
    model: str
    dimension: int


class CogneeConfig(BaseModel):
    environment: str
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
    database: str


class QdrantConfig(BaseModel):
    url: str
    api_key: str
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
    