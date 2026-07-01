from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


# ==========================================================
# Environment Variables
# ==========================================================

class EnvironmentSettings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool = False
    APP_ENVIRONMENT: str
    APP_PORT: int = 8000

    # LLM
    LLM_PROVIDER: str
    LLM_MODEL: str
    LLM_API_KEY: str
    LLM_TEMPERATURE: float = 0.0
    LLM_MAX_TOKENS: int = 4096
    LLM_TOP_P: float = 0.1
    LLM_TIMEOUT: int = 30

    # Embeddings
    EMBEDDING_PROVIDER: str
    EMBEDDING_MODEL: str
    EMBEDDING_DIMENSION: int

    # Cognee
    COGNEE_ENVIRONMENT: str
    COGNEE_DATASET_NAME: str
    COGNEE_API_KEY: str

    # PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE: str
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str

    # Neo4j
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str
    NEO4J_DATABASE: str

    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION_NAME: str

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    LOG_FILE_PATH: str = "logs/app.log"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# ==========================================================
# Configuration Domain Objects
# ==========================================================
 
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
    
    
    
    
def load_settings() -> Settings:
    env = EnvironmentSettings()

    app_config = ApplicationConfig(
        app_name=env.APP_NAME,
        app_version=env.APP_VERSION,
        debug=env.DEBUG,
        environment=env.ENVIRONMENT,
        port=env.APP_PORT,
    )

    llm_config = LLMConfig(
        provider=env.LLM_PROVIDER,
        model=env.LLM_MODEL,
        api_key=env.LLM_API_KEY,
        temperature=env.LLM_TEMPERATURE,
        max_tokens=env.LLM_MAX_TOKENS,
        top_p=env.LLM_TOP_P,
        timeout=env.LLM_TIMEOUT,
    )

    embedding_config = EmbeddingConfig(
        provider=env.EMBEDDING_PROVIDER,
        model=env.EMBEDDING_MODEL,
        dimension=env.EMBEDDING_DIMENSION,
    )

    cognee_config = CogneeConfig(
        environment=env.COGNEE_ENVIRONMENT,
        dataset_name=env.COGNEE_DATASET_NAME,
        api_key=env.COGNEE_API_KEY,
    )

    postgres_config = PostgresConfig(
        host=env.POSTGRES_HOST,
        port=env.POSTGRES_PORT,
        database=env.POSTGRES_DATABASE,
        username=env.POSTGRES_USERNAME,
        password=env.POSTGRES_PASSWORD,
    )

    neo4j_config = Neo4jConfig(
        uri=env.NEO4J_URI,
        username=env.NEO4J_USERNAME,
        password=env.NEO4J_PASSWORD,
        database=env.NEO4J_DATABASE,
    )

    qdrant_config = QdrantConfig(
        url=env.QDRANT_URL,
        api_key=env.QDRANT_API_KEY,
        collection_name=env.QDRANT_COLLECTION_NAME,
    )

    logging_config = LoggingConfig(
        level=env.LOG_LEVEL,
        format=env.LOG_FORMAT,
        file_path=env.LOG_FILE_PATH,
    )

    return Settings(
        app=app_config,
        llm=llm_config,
        embeddings=embedding_config,
        cognee=cognee_config,
        postgres=postgres_config,
        neo4j=neo4j_config,
        qdrant=qdrant_config,
        logging=logging_config,
    )
    