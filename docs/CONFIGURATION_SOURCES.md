# BUSINESS MEMORY AI — CONFIGURATION SOURCES

# Purpose

This document defines where every configuration value in the Business Memory AI system originates.

The goal is to centralize configuration management, support multiple environments, and follow modern backend engineering practices.

---

# Configuration Architecture

```
Environment Variables (.env)
                |
                v
        Configuration Loader
                |
                v
            Settings
                |
    +-----------+-----------+
    |           |           |
    v           v           v
 Application   Services   Memory
```

---

# Primary Configuration Source

The primary configuration source for the application is:

```
.env
```

Reasons:

- Environment separation
- Secret management
- Deployment flexibility
- Security
- 12-Factor App compliance

---

# ApplicationConfig

Purpose:

Store application-level settings.

Configuration Source:

```
.env
```

Variables:

```
APP_NAME
APP_VERSION
APP_ENVIRONMENT
APP_DEBUG
```

Example:

```env
APP_NAME=Business Memory AI
APP_VERSION=1.0.0
APP_ENVIRONMENT=development
APP_DEBUG=true
```

---

# LLMConfig

Purpose:

Configure the language model provider.

Configuration Source:

```
.env
```

Variables:

```
LLM_PROVIDER
LLM_MODEL
LLM_API_KEY
LLM_TEMPERATURE
LLM_MAX_TOKENS
LLM_TOP_P
LLM_TIMEOUT
```

Example:

```env
LLM_PROVIDER=custom
LLM_MODEL=groq/llama-3.3-70b-versatile
LLM_API_KEY=gsk_xxxxxxxxx
LLM_TEMPERATURE=0.2
LLM_MAX_TOKENS=4096
LLM_TOP_P=1.0
LLM_TIMEOUT=60
```

---

# EmbeddingConfig

Purpose:

Configure embedding generation.

Configuration Source:

```
.env
```

Variables:

```
EMBEDDING_PROVIDER
EMBEDDING_MODEL
EMBEDDING_DIMENSION
```

Example:

```env
EMBEDDING_PROVIDER=fastembed
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
EMBEDDING_DIMENSION=384
```

---

# CogneeConfig

Purpose:

Configure Cognee memory engine.

Configuration Source:

```
.env
```

Variables:

```
COGNEE_ENVIRONMENT
COGNEE_API_KEY
COGNEE_DATASET_NAME
```

Example:

```env
COGNEE_ENVIRONMENT=cloud
COGNEE_API_KEY=xxxxxxxx
COGNEE_DATASET_NAME=business_memory_ai
```

---

# PostgresConfig

Purpose:

Configure PostgreSQL metadata storage.

Configuration Source:

```
.env
```

Variables:

```
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DATABASE
POSTGRES_USERNAME
POSTGRES_PASSWORD
```

Example:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=business_memory_ai
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=password
```

---

# Neo4jConfig

Purpose:

Configure graph database.

Configuration Source:

```
.env
```

Variables:

```
NEO4J_URI
NEO4J_USERNAME
NEO4J_PASSWORD
NEO4J_DATABASE
```

Example:

```env
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password
NEO4J_DATABASE=neo4j
```

---

# QdrantConfig

Purpose:

Configure vector database.

Configuration Source:

```
.env
```

Variables:

```
QDRANT_URL
QDRANT_API_KEY
QDRANT_COLLECTION_NAME
```

Example:

```env
QDRANT_URL=https://xxxxx.cloud.qdrant.io
QDRANT_API_KEY=xxxxxxxx
QDRANT_COLLECTION_NAME=business_memory_vectors
```

---

# LoggingConfig

Purpose:

Configure application logging.

Configuration Source:

```
.env
```

Variables:

```
LOG_LEVEL
LOG_FORMAT
LOG_FILE_PATH
```

Example:

```env
LOG_LEVEL=INFO
LOG_FORMAT=json
LOG_FILE_PATH=logs/application.log
```

---

# Configuration Priority Order

If multiple configuration sources exist, the application follows this priority:

```
1. Environment Variables
        ↓
2. .env File
        ↓
3. Application Defaults
```

---

# Environment Types

The application supports:

```
development
testing
production
```

---

# Secret Management

The following values are considered secrets:

```
LLM_API_KEY
COGNEE_API_KEY
POSTGRES_PASSWORD
NEO4J_PASSWORD
QDRANT_API_KEY
```

These values:

- Must never be committed to Git
- Must remain inside .env
- Must be ignored by version control

---

# Benefits of this Architecture

This configuration architecture provides:

✓ Centralized configuration

✓ Environment separation

✓ Secure secret management

✓ Deployment flexibility

✓ Easier maintenance

✓ Better scalability

✓ 12-Factor App compliance

---

# Topics Learned

This configuration architecture teaches:

- Environment Variables
- Secret Management
- Configuration Management
- 12-Factor Applications
- Backend Architecture
- Deployment Architecture
- Application Bootstrapping
- Environment Separation
- Production Software Engineering
