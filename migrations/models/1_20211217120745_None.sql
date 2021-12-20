-- upgrade --
CREATE TABLE IF NOT EXISTS "location" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "location_name" VARCHAR(200) NOT NULL,
    "code" VARCHAR(2) NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "created_at" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "categorymodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "category_name" VARCHAR(50) NOT NULL UNIQUE,
    "description" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "mesureunitmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "mesure_name" VARCHAR(50) NOT NULL UNIQUE,
    "description" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "products" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "product_name" VARCHAR(50) NOT NULL UNIQUE,
    "description" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL,
    "category_id" INT NOT NULL REFERENCES "categorymodel" ("id") ON DELETE CASCADE,
    "mesure_unit_id" INT NOT NULL REFERENCES "mesureunitmodel" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
