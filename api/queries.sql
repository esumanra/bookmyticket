-- SQLite
DELETE FROM api_movie;
DELETE FROM api_city;
DELETE FROM api_theatre;
DELETE FROM api_show;
DELETE FROM api_mapping;

INSERT INTO api_movie (id, name, language)
VALUES
(1, 'Uppena', 'Telugu'),
(2, 'Tenet', 'English')
;

INSERT INTO api_city (id, name)
VALUES (1, 'Hyderabad');

INSERT INTO api_theatre (id, name, city_id)
VALUES
(1, 'AMB', 1),
(2, 'Cinepolis', 1)
;

INSERT INTO api_show (id, name, start_time, end_time, total_seats, available_seats)
VALUES
(1, 'Morning', '2020-09-29 10:00', '2020-09-29 12:30', 100, 100),
(2, 'Evening', '2020-09-29 18:00', '2020-09-29 20:30', 100, 100),
(3, 'Night', '2020-09-29 21:15', '2020-09-30 01:45', 100, 100)
;

INSERT INTO api_mapping (id, city_id, movie_id, show_id, theatre_id)
VALUES
(1, 1, 1, 1, 1),
(2, 1, 2, 2, 2)
;
