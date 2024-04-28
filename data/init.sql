CREATE TABLE point (
    id SERIAL PRIMARY KEY,
    coords POINT,
    address varchar(128)
);

CREATE EXTENSION pg_trgm;
CREATE INDEX trgm_idx ON point USING GIN (address gin_trgm_ops);

SET pg_trgm.similarity_threshold = 0.7;
