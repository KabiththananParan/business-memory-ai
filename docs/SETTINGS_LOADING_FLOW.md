# BUSINESS MEMORY AI — SETTINGS LOADING FLOW

# Purpose

This document describes how Business Memory AI loads application configuration from environment variables and transforms them into structured configuration objects.

The goal is to create a single source of truth for application configuration.

---

# Problem

The application depends on multiple external systems:

- Groq
- Cognee
- Neo4j
- Qdrant
- PostgreSQL
- Logging

Without centralized configuration, every component would need to read environment variables independently.

Example:

```python
os.getenv("NEO4J_URI")
os.getenv("QDRANT_URL")
os.getenv("LLM_API_KEY")
```

This creates:

- duplicated code
- poor maintainability
- difficult testing
- inconsistent configuration

---

# Solution

Create a centralized Settings object that loads all application configuration during application startup.

---

# Configuration Loading Workflow

```
                .env
                  |
                  v
        Environment Variables
                  |
                  v
            load_settings()
                  |
                  v
        ------------------------
        |          |           |
        v          v           v
      APP        LLM      EMBEDDINGS
        |          |           |
        v          v           v
     COGNEE    DATABASES    LOGGING
                  |
                  v
               Settings
                  |
                  v
          Global Application
              Configuration
```

---

# Detailed Startup Flow

```
Application Start
        |
        v
Read .env File
        |
        v
Load Environment Variables
        |
        v
Create ApplicationConfig
        |
        v
Create LLMConfig
        |
        v
Create EmbeddingConfig
        |
        v
Create CogneeConfig
        |
        v
Create PostgresConfig
        |
        v
Create Neo4jConfig
        |
        v
Create QdrantConfig
        |
        v
Create LoggingConfig
        |
        v
Assemble Settings Object
        |
        v
Store Global Settings
        |
        v
Application Ready
```

---

# Configuration Object Hierarchy

```
Settings
   |
   +---- ApplicationConfig
   |
   +---- LLMConfig
   |
   +---- EmbeddingConfig
   |
   +---- CogneeConfig
   |
   +---- PostgresConfig
   |
   +---- Neo4jConfig
   |
   +---- QdrantConfig
   |
   +---- LoggingConfig
```

---

# Question 1

## How many Settings objects should exist?

Answer:

```
Exactly one.
```

Reason:

The entire application should use a single configuration source.

This follows the:

- Singleton Pattern
- Single Source of Truth principle

---

# Question 2

## Who creates the Settings object?

Answer:

```
The application startup process.
```

Example:

```
main.py
        |
        v
load_settings()
        |
        v
Settings
```

No other component should create Settings.

---

# Question 3

## Who uses the Settings object?

Answer:

Every major component.

Examples:

```
Memory Layer
Services Layer
API Layer
Database Layer
Logging Layer
```

---

# Question 4

## When should Settings be created?

Answer:

```
During application startup.
```

Example:

```
python main.py
        |
        v
Create Settings
        |
        v
Initialize Services
        |
        v
Start API Server
```

Settings should never be created after the application starts serving requests.

---

# Singleton Configuration Pattern

The application follows the Singleton Pattern:

```
                    Settings
                        |
        ----------------------------------
        |          |          |          |
        v          v          v          v
      API      Services    Memory    Database
```

Benefits:

- Single source of truth
- Better performance
- Easier testing
- Easier maintenance
- Consistent configuration

---

# Example Usage

Instead of:

```
Read .env everywhere
```

The application should use:

```
settings.app.app_name

settings.llm.model

settings.neo4j.uri

settings.qdrant.url

settings.cognee.dataset_name
```

---

# Configuration Source Priority

If multiple configuration sources exist:

```
1. Environment Variables
        ↓
2. .env File
        ↓
3. Default Values
```

---

# Application Lifecycle

```
Application Start
        |
        v
Load Configuration
        |
        v
Initialize Logger
        |
        v
Initialize Databases
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

# Benefits

This architecture provides:

✓ Centralized configuration

✓ Environment separation

✓ Secure secret management

✓ Single source of truth

✓ Better maintainability

✓ Easier testing

✓ Production readiness

✓ Cleaner architecture

---

# Topics Learned

This design teaches:

- Environment Variables
- Configuration Management
- Singleton Pattern
- Application Bootstrapping
- Dependency Injection
- Backend Architecture
- System Design
- Resource Management
- 12-Factor Applications
- Production Software Engineering
