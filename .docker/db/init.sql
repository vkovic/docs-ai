CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS embeddings
(
    id   SERIAL PRIMARY KEY,
    embedding vector,
    text TEXT,
    created_at timestamptz DEFAULT now()
);