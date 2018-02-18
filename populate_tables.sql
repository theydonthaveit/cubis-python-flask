BEGIN;

CREATE TABLE IF NOT EXISTS restaurant (
	id INT,
	name VARCHAR(80)
);
insert into restaurant (id, name) values (1, 'The Ledbury');
insert into restaurant (id, name) values (2, 'The Five Fields');
insert into restaurant (id, name) values (3, 'Scott''s Restaurant');
insert into restaurant (id, name) values (4, 'Restaurant Story London');
insert into restaurant (id, name) values (5, 'Restaurant Gordon Ramsay');
insert into restaurant (id, name) values (6, 'Anglo restaurant');
insert into restaurant (id, name) values (7, 'Mere');
insert into restaurant (id, name) values (8, 'Typing Room');
insert into restaurant (id, name) values (9, 'Portland Restaurant');
insert into restaurant (id, name) values (10, 'Chez Bruce');

COMMIT;