# BUSINESS MEMORY AI — APPLICATION STARTUP FLOW

# Purpose

This document describes how the Business Memory AI application initializes its components during startup.

The startup sequence ensures that all required services are loaded and validated before the application begins accepting requests.

---

# Application Startup Sequence

When the application starts, it follows this initialization order:

```
Application Start
        |
        v
Load Environment Variables
        |
        v
Load Application Settings
        |
        v
Initialize Logging
        |
        v
Initialize PostgreSQL
        |
        v
Initialize Neo4j
        |
        v
Initialize Qdrant
        |
        v
Initialize Cognee
        |
        v
Initialize Memory Manager
        |
        v
Register API Routes
        |
        v
Application Ready
```

---

# Step 1 — Application Start

Entry Point:

```
backend/main.py
```

Responsibilities:

- Start the FastAPI application
- Trigger the startup lifecycle
- Initialize all application resources

---

# Step 2 — Load Environment Variables

Source:

```
.env
```

Purpose:

Load all application secrets and configuration values.

Examples:

- LLM API Key
- Neo4j credentials
- PostgreSQL credentials
- Qdrant credentials
- Cognee settings

---

# Step 3 — Load Application Settings

File:

```
backend/app/core/config.py
```

Purpose:

Convert environment variables into structured configuration objects.

Configuration Domains:

- ApplicationConfig
- LLMConfig
- CogneeConfig
- EmbeddingConfig
- PostgresConfig
- Neo4jConfig
- QdrantConfig
- LoggingConfig

---

# Step 4 — Initialize Logging

File:

```
backend/app/core/logger.py
```

Purpose:

Create centralized logging.

Responsibilities:

- Configure log levels
- Configure log formatting
- Configure file logging
- Configure console logging

Log Levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

# Step 5 — Initialize PostgreSQL

File:

```
backend/app/core/database.py
```

Purpose:

Initialize metadata storage.

Stores:

- User information
- Dataset metadata
- Application metadata
- Memory metadata

---

# Step 6 — Initialize Neo4j

Purpose:

Initialize graph memory storage.

Stores:

- Entities
- Relationships
- Knowledge graphs
- Business connections

Example:

```
Supplier A
       |
 caused
       |
Delivery Delay
```

---

# Step 7 — Initialize Qdrant

Purpose:

Initialize vector memory storage.

Stores:

- Semantic embeddings
- Similarity search indexes
- Vector collections

Example:

```
"Supplier delay"

↓

[0.342, 0.112, 0.884, ...]
```

---

# Step 8 — Initialize Cognee

Purpose:

Initialize the hybrid graph-vector memory engine.

Cognee Responsibilities:

- remember()
- recall()
- improve()
- forget()

Connected Systems:

- Neo4j
- Qdrant
- PostgreSQL
- Groq
- FastEmbed

---

# Step 9 — Initialize Memory Manager

File:

```
backend/app/memory/memory_manager.py
```

Purpose:

Provide a single interface for all memory operations.

Responsibilities:

- Store memories
- Retrieve memories
- Improve memories
- Forget memories

---

# Step 10 — Register API Routes

File:

```
backend/app/api/
```

Register:

```
POST   /api/memory/remember

POST   /api/memory/recall

POST   /api/memory/improve

DELETE /api/memory/forget

GET    /api/memory/stats

GET    /api/memory/history

GET    /api/analytics
```

---

# Step 11 — Application Ready

The application is now ready to accept requests.

Available Components:

✓ Configuration

✓ Logging

✓ PostgreSQL

✓ Neo4j

✓ Qdrant

✓ Cognee

✓ Memory Manager

✓ API Layer

---

# Dependency Graph

```
Application
      |
      v
Configuration
      |
      +------------+
      |            |
      v            v
Logger      Database Connections
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
    Postgres     Neo4j      Qdrant
                    |
                    v
                 Cognee
                    |
                    v
             Memory Manager
                    |
                    v
               API Layer
                    |
                    v
                Frontend
```

---

# Topics Learned

This startup architecture teaches:

- Environment Variables
- Configuration Management
- Application Bootstrapping
- Dependency Management
- Resource Management
- Logging Systems
- Database Initialization
- Backend Architecture
- Service Lifecycle Management
- Dependency Injection
