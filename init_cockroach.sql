-- init_cockroach.sql
CREATE DATABASE IF NOT EXISTS hashdb;

USE hashdb;

CREATE TABLE IF NOT EXISTS device_hashes (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    device_id VARCHAR(255) NOT NULL,
    hash_value TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- index
CREATE INDEX IF NOT EXISTS idx_user_device ON device_hashes (user_id, device_id);
