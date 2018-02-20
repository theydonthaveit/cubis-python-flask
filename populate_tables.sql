BEGIN;

CREATE TABLE IF NOT EXISTS restaurant (
	id INT,
	name VARCHAR(80)
);
insert into restaurant (id, name) values (1, 'The Ledbury Group');
insert into restaurant (id, name) values (2, 'The Five Fields Group');
insert into restaurant (id, name) values (3, 'Scotts Restaurant Group');
insert into restaurant (id, name) values (4, 'Restaurant Story London Group');
insert into restaurant (id, name) values (5, 'Restaurant Gordon Ramsay Group');
insert into restaurant (id, name) values (6, 'Anglo restaurant Group');
insert into restaurant (id, name) values (7, 'Mere Group');
insert into restaurant (id, name) values (8, 'Typing Room Group');
insert into restaurant (id, name) values (9, 'Portland Restaurant Group');
insert into restaurant (id, name) values (10, 'Chez Bruce Group');

CREATE TABLE IF NOT EXISTS subsidiary_restaurant (
	id INT,
	name VARCHAR(80),
	restaurant_id INT
);
insert into subsidiary_restaurant (id, name, restaurant_id) values (1, 'The Ledbury', 1);
insert into subsidiary_restaurant (id, name, restaurant_id) values (2, 'The Five Fields', 2);
insert into subsidiary_restaurant (id, name, restaurant_id) values (3, 'Scotts Restaurant', 3);
insert into subsidiary_restaurant (id, name, restaurant_id) values (4, 'Restaurant Story London', 4);
insert into subsidiary_restaurant (id, name, restaurant_id) values (5, 'Restaurant Gordon Ramsay', 5);
insert into subsidiary_restaurant (id, name, restaurant_id) values (6, 'Anglo restaurant', 6);
insert into subsidiary_restaurant (id, name, restaurant_id) values (7, 'Mere', 7);
insert into subsidiary_restaurant (id, name, restaurant_id) values (8, 'Typing Room', 8);
insert into subsidiary_restaurant (id, name, restaurant_id) values (9, 'Portland Restaurant', 9);
insert into subsidiary_restaurant (id, name, restaurant_id) values (10, 'Chez Bruce', 10);

CREATE TABLE IF NOT EXISTS addresses (
	id INT,
	subsidiary_restaurant_id INT,
	address_line_one VARCHAR(80),
	address_line_two VARCHAR(80),
	city VARCHAR(50),
	country VARCHAR(50),
	postcode VARCHAR(50),
	long VARCHAR(50),
	lat VARCHAR(50)
);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (1, 1, '127', 'Ledbury Rd', 'London', 'United Kingdom', 'W11 2AQ', -2.70309, 53.763201);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (2, 2, '8-9', 'Blacklands Terrace', 'London', 'United Kingdom', 'SW3 2SP', -0.766168, 52.501244);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (3, 3, '20', 'Mount St', 'London', 'United Kingdom', 'W1K 2HE', -1.4730092, 53.3788422);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (4, 4, '199', 'Tooley St', 'London', 'United Kingdom', 'SE1 2JX', -2.2508745, 56.968436);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (5, 5, '68', 'Royal Hospital Rd', 'London', 'United Kingdom', 'SW3 4HP', -0.9009942, 52.2063851);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (6, 6, '30', 'St Cross St', 'London', 'United Kingdom', 'EC1N 8UH', -1.4631269, 53.3326454);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (7, 7, '74', 'Charlotte St', 'London', 'United Kingdom', 'W1T 4QH', -1.48003, 53.800245);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (8, 8, 'Town Hall Hotel', 'Patriot Square', 'London', 'United Kingdom', 'E2 9NF', -2.3523889, 51.5598572);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (9, 9, '113', 'Great Portland St', 'London', 'United Kingdom', 'W1W 6QQ', -2.244703, 52.721723);
insert into addresses (id, subsidiary_restaurant_id, address_line_one, address_line_two, city, country, postcode, long, lat) values (10, 10, '2', 'Bellevue Rd', 'London', 'United Kingdom', 'SW17 7EG', -0.1365486, 51.5136143);

CREATE TABLE IF NOT EXISTS restaurant_info (
	id INT,
	subsidiary_restaurant_id INT,
	addresses_id INT,
	seating VARCHAR(3),
	cuisine VARCHAR(80)
);
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (1, 1, 1, 270, 'British');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (2, 2, 2, 72, 'British');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (3, 3, 3, 268, 'Seafood');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (4, 4, 4, 154, 'British');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (5, 5, 5, 254, 'French');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (6, 6, 6, 25, 'British');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (7, 7, 7, 68, 'South Pacific–influenced French');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (8, 8, 8, 71, 'European');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (9, 9, 9, 16, 'European');
insert into restaurant_info (id, subsidiary_restaurant_id, addresses_id, seating, cuisine) values (10, 10, 10, 341, 'High-end Modern French');

CREATE TABLE IF NOT EXISTS menu_item (
	id INT,
	subsidiary_restaurant_id INT,
	course VARCHAR(80),
	description VARCHAR(500),
	price VARCHAR(80),
	ingredients VARCHAR(80)
);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (1, 'Taxi zum Klo', 'Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', '£5.73', 'Cabbage Roll', 1);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (2, 'Lupin III: First Contact', 'Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', '£23.65', 'Passion Fruit', 2);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (3, 'Who Is Cletis Tout?', 'In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus.', '£31.01', 'Bread - Pumpernickel', 3);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (4, 'Fellinis Roma', 'Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.', '£29.00', 'Squash - Guords', 4);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (5, 'Justice League: The Flashpoint Paradox', 'Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.', '£16.82', 'Sole - Iqf', 5);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (6, 'Best Seller', 'In congue. Etiam justo. Etiam pretium iaculis justo.', '£12.37', 'Broom - Corn', 6);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (7, 'True Heart Susie', 'Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. Integer non velit.', '£5.62', 'Tamarillo', 7);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (8, 'Second Chorus', 'Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.', '£21.88', 'Oregano - Fresh', 8);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (9, 'O Último Mergulho', 'Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.', '£32.09', 'Dikon', 9);
insert into menu_item (id, course, description, price, ingredients, subsidiary_restaurant_id) values (10, 'It Came from Hollywood', 'Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', '£30.68', 'Pasta - Tortellini, Fresh', 10);

COMMIT;