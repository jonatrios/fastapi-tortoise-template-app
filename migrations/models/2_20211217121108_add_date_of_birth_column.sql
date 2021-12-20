-- upgrade --
ALTER TABLE "user" ADD "date_of_birth" DATE;
-- downgrade --
ALTER TABLE "user" DROP COLUMN "date_of_birth";
