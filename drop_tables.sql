BEGIN;

DROP TABLE IF EXISTS restaurant CASCADE;
DROP TABLE IF EXISTS subsidiary_restaurant CASCADE;
DROP TABLE IF EXISTS addresses CASCADE;
DROP TABLE IF EXISTS restaurant_info CASCADE;
DROP TABLE IF EXISTS menu_item CASCADE;

COMMIT;