# BUSINESS MEMORY AI — PROJECT WORKFLOW

## Project Overview

Business Memory AI is an AI-powered organizational memory system built using Cognee's hybrid graph-vector memory architecture. The system enables businesses to permanently store, retrieve, improve, and selectively forget organizational knowledge across infinite sessions.

The goal is to eliminate knowledge loss within organizations by creating a persistent memory layer for business operations, decisions, incidents, suppliers, and customer interactions.

---

# Core Technologies

| Component         | Technology   | Purpose                            |
| ----------------- | ------------ | ---------------------------------- |
| Memory Layer      | Cognee       | Orchestrates memory lifecycle      |
| LLM               | Groq         | Reasoning and knowledge extraction |
| Graph Database    | Neo4j        | Relationship storage               |
| Vector Database   | Qdrant Cloud | Semantic memory retrieval          |
| Metadata Database | PostgreSQL   | Dataset and system metadata        |
| Embeddings        | FastEmbed    | Text embedding generation          |
| Backend           | FastAPI      | API services                       |
| Frontend          | Next.js      | User interface                     |

---

# Business Memory Types

The system supports four primary business memory categories.

## 1. Supplier Memory

Stores supplier-related operational knowledge.

### Examples

* Supplier delivery delays
* Quality issues
* Contract changes
* Supplier performance history
* Vendor relationships

### Example

Input:

> Supplier A delayed shipment by 14 days due to factory shutdown.

Stored knowledge:

* Supplier: Supplier A
* Event: Delivery Delay
* Cause: Factory Shutdown
* Duration: 14 Days

---

## 2. Customer Memory

Stores customer-related interactions and issues.

### Examples

* Customer complaints
* Refund requests
* Customer preferences
* Purchase history
* Support interactions

### Example

Input:

> Customer XYZ requested a refund because of damaged products.

Stored knowledge:

* Customer: Customer XYZ
* Action: Refund Request
* Cause: Damaged Product

---

## 3. Meeting Decision Memory

Stores organizational decisions.

### Examples

* Executive decisions
* Strategic planning
* Policy updates
* Supplier changes
* Budget approvals

### Example

Input:

> Management decided to switch to Supplier B starting July.

Stored knowledge:

* Decision Maker: Management
* Decision: Switch Supplier
* Target: Supplier B
* Effective Date: July

---

## 4. Business Incident Memory

Stores operational incidents.

### Examples

* Shipping disruptions
* Factory shutdowns
* Warehouse accidents
* System failures
* Security incidents

### Example

Input:

> Warehouse fire caused a three-day shipping interruption.

Stored knowledge:

* Incident: Warehouse Fire
* Impact: Shipping Delay
* Duration: Three Days

---

# Memory Lifecycle Workflow

Business Memory AI fully implements the Cognee memory lifecycle.

---

## 1. remember()

Purpose:

Store business knowledge permanently.

### Workflow

User Input

↓

Cognee receives memory

↓

Groq extracts entities and relationships

↓

FastEmbed generates embeddings

↓

Neo4j stores graph relationships

↓

Qdrant stores semantic vectors

↓

PostgreSQL stores metadata

### Example

Input:

> Supplier A caused delivery delays in January.

Output:

Persistent business memory.

---

## 2. recall()

Purpose:

Retrieve business knowledge.

### Workflow

User Question

↓

Generate question embedding

↓

Search Qdrant for semantic similarity

↓

Search Neo4j for relationships

↓

Combine retrieved context

↓

Groq generates response

### Example

Question:

> Which supplier caused delivery delays?

Response:

> Supplier A caused delivery delays in January.

---

## 3. improve()

Purpose:

Optimize and enrich business memory.

### Workflow

Load graph memory

↓

Load vector memory

↓

Analyze relationships

↓

Re-index memory vectors

↓

Strengthen memory associations

↓

Optimize retrieval quality

---

## 4. forget()

Purpose:

Remove outdated or unnecessary business knowledge.

### Workflow

Locate target memory

↓

Delete graph relationships

↓

Delete semantic vectors

↓

Delete metadata

↓

Clean orphan relationships

↓

Finalize deletion

---

# System Architecture

```
                User
                  |
                  v
           Business Memory AI
                  |
                  v
               Cognee
                  |
    ----------------------------------
    |               |               |
    v               v               v
  Groq           Neo4j          Qdrant
    |               |               |
Reasoning      Relationships     Semantics
                  |
                  v
             PostgreSQL
```

---

# Backend API Design

## Memory Operations

### Store Memory

POST /api/memory/remember

---

### Retrieve Memory

POST /api/memory/recall

---

### Improve Memory

POST /api/memory/improve

---

### Delete Memory

DELETE /api/memory/forget

---

## Dashboard APIs

### Statistics

GET /api/memory/stats

---

### History

GET /api/memory/history

---

### Graph Visualization

GET /api/memory/graph

---

# Frontend Pages

## Dashboard

Displays:

* Total memories
* Suppliers
* Customers
* Incidents
* Decisions
* Recent activity

---

## Add Memory

Allows users to:

* Select memory type
* Enter business knowledge
* Store memory

---

## Ask Memory

Allows users to:

* Ask business questions
* Retrieve contextual answers
* Explore related memories

---

## Memory Explorer

Allows users to:

* Browse memories
* Filter memories
* Search memories
* Delete memories

---

## Analytics Dashboard

Displays:

* Supplier performance
* Customer issues
* Incident trends
* Organizational decisions

---

# Demo Workflow

## Step 1

Add supplier memory:

> Supplier A delayed shipment by 14 days.

---

## Step 2

Add management decision:

> Management decided to replace Supplier A.

---

## Step 3

Ask:

> Which supplier caused delivery problems?

---

## Step 4

Business Memory AI recalls:

> Supplier A caused delivery delays and management decided to replace them.

---

## Step 5

Run improve() to optimize memory.

---

## Step 6

Run forget() to remove outdated supplier knowledge.

---

# Hackathon Objectives

Demonstrate complete use of Cognee's memory lifecycle:

* ✅ remember()
* ✅ recall()
* ✅ improve()
* ✅ forget()

Demonstrate hybrid memory architecture:

* Graph Memory (Neo4j)
* Vector Memory (Qdrant)
* Metadata Storage (PostgreSQL)
* LLM Reasoning (Groq)
* Local Embeddings (FastEmbed)

---

# Project Vision

Business Memory AI transforms organizational knowledge into a persistent, searchable, self-improving memory system that never forgets critical business information.
