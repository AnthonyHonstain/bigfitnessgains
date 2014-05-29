
/* Insert muscle groups as enum-type, pulled from bodybuilding.com */
INSERT INTO mainapp_musclegroup	(id, muscle_group_name, created, modified)
VALUES 
    (1, 'Unknown', now(), now()),
    (2, 'Neck', now(), now()),
    (3, 'Traps (trapezius)', now(), now()),
    (4, 'Shoulders (deltoids)', now(), now()),
    (5, 'Chest (pectoralis)', now(), now()),
    (6, 'Biceps (biceps brachii)', now(), now()),
    (7, 'Forearm (brachioradialis)', now(), now()),
    (8, 'Abs (rectus abdominis)', now(), now()),
    (9, 'Quads (quadriceps)', now(), now()),
    (10, 'Calves (gastrocnemius)', now(), now()),
    (11, 'Lats (latissimus dorsi)', now(), now()),
    (12, 'Middle Back (rhomboids)', now(), now()),
    (13, 'Lower Back', now(), now()),
    (14, 'Glutes (gluteus maximus and medius)', now(), now()),
    (15, 'Hamstrings (biceps femoris)', now(), now()),
    (16, 'Triceps', now(), now());


/* Insert exercises as enum-type, to start. Also bodybuilding.com */

INSERT INTO mainapp_exercise (id, exercise_name, created, modified)
VALUES
	(1, 'Back squat', now(), now()),
	(2, 'Front squat', now(), now()),
	(3, 'Overhead squat', now(), now()),
	(4, 'Deadlift', now(), now()),
	(5, 'Deadlift (straight leg)', now(), now()),
	(6, 'Hang clean', now(), now()),
	(7, 'Power clean', now(), now()),
	(8, 'Barbell row (overhand)', now(), now()),
	(9, 'Barbell row (underhand)', now(), now()),
	(10, 'Barbell shrug', now(), now()),
	(11, 'Bench press (flat)', now(), now()),
	(12, 'Bench press (incline)', now(), now()),
	(13, 'Bench press (decline)', now(), now()),
	(14, 'Overhead press', now(), now()),
	(15, 'Overhead press (Klokov)', now(), now()),
	(16, 'Pull-up', now(), now()),
	(17, 'Chin-up', now(), now()),
	(18, 'Push-up', now(), now()),
	(19, 'Dip', now(), now()),
	(20, 'Tricep pushdown', now(), now()),
	(21, 'Dumbbell bench (flat)', now(), now()),
	(22, 'Dumbbell bench (incline)', now(), now()),
	(23, 'Dumbbell bench (decline)', now(), now()),
	(24, 'Dumbbell row', now(), now()),
	(25, 'Barbell curl', now(), now()),
	(26, 'Dumbbell curl', now(), now()),
	(27, 'Hammer curl', now(), now()),
	(28, 'Preacher curl', now(), now()),
	(29, 'Overhead cable curl', now(), now()),
	(30, 'Calf press', now(), now()),
	(31, 'Pec fly', now(), now()),
	(32, 'Dumbbell fly', now(), now()),
	(33, 'Chest press (machine)', now(), now()),
	(34, 'Chest press (cable)', now(), now()),
	(35, 'Kettlebell swings', now(), now()),
	(36, 'Kettlebell row', now(), now()),
	(37, 'Kettlebell floor press', now(), now()),
	(38, 'Turkish get-up', now(), now()),
	(39, 'Farmer''s carry', now(), now()),
	(40, 'Kneeling squat', now(), now()),
	(41, 'Good morning', now(), now()),
	(42, 'Barbell lunge', now(), now()),
	(43, 'Dumbbell lunge', now(), now()),
	(44, 'Leg curls', now(), now()),
	(45, 'Barbell pullover', now(), now()),
	(46, 'Dumbbell pullover', now(), now()),
	(47, 'Lat pulldown', now(), now()),
	(48, 'Muscle up', now(), now()),
	(49, 'Hyperextensions', now(), now()),
	(50, 'Rack pull', now(), now()),
	(51, 'Atlas stone lift', now(), now()),
	(52, 'Good morning (seated)', now(), now()),
	(53, 'Good morning (straight leg)', now(), now()),
	(54, 'Inverted row', now(), now()),
	(55, 'Cable row', now(), now()),
	(56, 'Dumbbell squat', now(), now()),
	(57, 'Goblet squat', now(), now()),
	(58, 'Pistol squat', now(), now()),
	(59, 'Leg extension', now(), now()),
	(60, 'Leg press', now(), now()),
	(61, 'Zercher squat', now(), now()),
	(62, 'Dumbbell press', now(), now()),
	(63, 'Side dumbbell raise', now(), now()),
	(64, 'Kettlebell press', now(), now()),
	(65, 'Face pull', now(), now()),
	(66, 'Front dumbbell raise', now(), now()),
	(67, 'Plate lift', now(), now()),
	(68, 'Iron cross', now(), now()),
	(69, 'Cable shrug', now(), now()),
	(70, 'Dumbbell shrug', now(), now()),
	(71, 'Dumbbell upright row (standing)', now(), now()),
	(72, 'Tricep extension (barbell)', now(), now()),
	(73, 'Tricep extension (dumbbell)', now(), now()),
	(74, 'Skullcrusher', now(), now()),
	(75, 'Unknown', now(), now());


/*  Link exercises to the appropriate muscle groups */
INSERT INTO mainapp_exercisetomusclegroup (id, exercise_fk_id, muscle_group_fk_id, is_primary, created, modified)
VALUES
	/* id, ex, grp, primary? */
	(1, 1, 10, TRUE, now(), now()),
	(2, 1, 9, FALSE, now(), now()),
	(3, 1, 13, FALSE, now(), now()),
	(4, 1, 14, FALSE, now(), now()),
	(5, 1, 15, FALSE, now(), now()),
	
	(6, 2, 10, TRUE, now(), now()),
	(7, 2, 9, FALSE, now(), now()),
	(8, 2, 14, FALSE, now(), now()),
	(9, 2, 15, FALSE, now(), now()),

	(10, 5, 10, TRUE, now(), now()),
	(11, 5, 9, FALSE, now(), now()),
	(12, 5, 13, FALSE, now(), now()),
	(13, 5, 14, FALSE, now(), now()),
	(14, 5, 15, FALSE, now(), now()),

	(15, 4, 13, TRUE, now(), now()),
	(16, 4, 3, FALSE, now(), now()),
	(17, 4, 7, FALSE, now(), now()),
	(18, 4, 9, FALSE, now(), now()),
	(19, 4, 10, FALSE, now(), now()),
	(20, 4, 11, FALSE, now(), now()),
	(21, 4, 12, FALSE, now(), now()),
	(22, 4, 14, FALSE, now(), now()),
	(23, 4, 15, FALSE, now(), now()),

	(24, 5, 15, TRUE, now(), now()),
	(25, 5, 14, FALSE, now(), now()),
	(26, 5, 13, FALSE, now(), now()),

	(27, 6, 9, TRUE, now(), now()),
	(28, 6, 7, FALSE, now(), now()),
	(29, 6, 10, FALSE, now(), now()),
	(30, 6, 3, FALSE, now(), now()),
	(31, 6, 4, FALSE, now(), now()),
	(32, 6, 13, FALSE, now(), now()),
	(33, 6, 14, FALSE, now(), now()),
	(34, 6, 15, FALSE, now(), now()),

	(35, 7, 13, TRUE, now(), now()),
	(36, 7, 7, FALSE, now(), now()),
	(37, 7, 10, FALSE, now(), now()),
	(38, 7, 3, FALSE, now(), now()),
	(39, 7, 4, FALSE, now(), now()),
	(40, 7, 13, FALSE, now(), now()),
	(41, 7, 14, FALSE, now(), now()),
	(42, 7, 15, FALSE, now(), now()),
	(43, 7, 12, FALSE, now(), now()),
	(44, 7, 9, FALSE, now(), now()),

	(45, 8, 12, TRUE, now(), now()),
	(46, 8, 6, FALSE, now(), now()),
	(47, 8, 11, FALSE, now(), now()),
	(48, 8, 4, FALSE, now(), now()),
	
	(49, 9, 12, TRUE, now(), now()),
	(50, 9, 6, FALSE, now(), now()),
	(51, 9, 11, FALSE, now(), now()),
	(52, 9, 4, FALSE, now(), now()),
	
	(53, 10, 3, TRUE, now(), now()),
	
	(54, 11, 5, TRUE, now(), now()),
	(55, 11, 4, FALSE, now(), now()),
	(56, 11, 16, FALSE, now(), now()),
	
	(57, 12, 5, TRUE, now(), now()),
	(58, 12, 4, FALSE, now(), now()),
	(59, 12, 16, FALSE, now(), now()),
	
	(60, 13, 5, TRUE, now(), now()),
	(61, 13, 4, FALSE, now(), now()),
	(62, 13, 16, FALSE, now(), now()),

	(63, 14, 4, TRUE, now(), now()),
	(64, 14, 16, FALSE, now(), now()),
	
	(65, 15, 4, TRUE, now(), now()),
	(66, 15, 16, FALSE, now(), now()),

	(67, 16, 11, TRUE, now(), now()),
	(68, 16, 6, FALSE, now(), now()),
	(69, 16, 12, FALSE, now(), now()),
	
	(70, 17, 11, TRUE, now(), now()),
	(71, 17, 6, FALSE, now(), now()),
	(72, 17, 12, FALSE, now(), now()),
	(73, 17, 7, FALSE, now(), now()),
	
	(74, 18, 5, TRUE, now(), now()),
	(75, 18, 4, FALSE, now(), now()),
	(76, 18, 16, FALSE, now(), now()),
	
	(77, 19, 16, TRUE, now(), now()),
	(78, 19, 4, FALSE, now(), now()),
	(79, 19, 5, FALSE, now(), now()),

	(80, 20, 16, TRUE, now(), now()),

	(81, 21, 5, TRUE, now(), now()),
	(82, 21, 4, FALSE, now(), now()),
	(83, 21, 16, FALSE, now(), now()),

	(84, 22, 5, TRUE, now(), now()),
	(85, 22, 4, FALSE, now(), now()),
	(86, 22, 16, FALSE, now(), now()),

	(87, 23, 5, TRUE, now(), now()),
	(88, 23, 4, FALSE, now(), now()),
	(89, 23, 16, FALSE, now(), now()),

	(90, 24, 12, TRUE, now(), now()),
	(91, 24, 6, FALSE, now(), now()),
	(92, 24, 11, FALSE, now(), now()),
	(93, 24, 4, FALSE, now(), now()),

	(94, 25, 6, TRUE, now(), now()),
	(95, 25, 7, FALSE, now(), now()),

	(96, 26, 6, TRUE, now(), now()),
	(97, 26, 7, FALSE, now(), now()),

	(98, 27, 6, TRUE, now(), now()),

	(99, 28, 6, TRUE, now(), now()),

	(100, 29, 6, TRUE, now(), now()),

	(101, 30, 10, TRUE, now(), now()),

	(102, 31, 5, TRUE, now(), now()),

	(103, 32, 5, TRUE, now(), now()),

	(104, 33, 5, TRUE, now(), now()),
	(105, 33, 4, FALSE, now(), now()),
	(106, 33, 16, FALSE, now(), now()),

	(107, 34, 5, TRUE, now(), now()),
	(108, 34, 4, FALSE, now(), now()),
	(109, 34, 16, FALSE, now(), now()),

	(110, 35, 15, TRUE, now(), now()),
	(111, 35, 10, FALSE, now(), now()),
	(112, 35, 14, FALSE, now(), now()),
	(113, 35, 13, FALSE, now(), now()),
	(114, 35, 4, FALSE, now(), now()),

	(115, 36, 12, TRUE, now(), now()),
	(116, 36, 6, FALSE, now(), now()),
	(117, 36, 11, FALSE, now(), now()),

	(118, 37, 5, TRUE, now(), now()),
	(119, 37, 16, FALSE, now(), now()),

	(120, 38, 4, TRUE, now(), now()),
	(121, 38, 8, FALSE, now(), now()),
	(122, 38, 15, FALSE, now(), now()),
	(123, 38, 9, FALSE, now(), now()),
	(124, 38, 16, FALSE, now(), now()),

	(125, 39, 7, TRUE, now(), now()),
	(126, 39, 8, FALSE, now(), now()),
	(127, 39, 9, FALSE, now(), now()),
	(128, 39, 14, FALSE, now(), now()),
	(129, 39, 15, FALSE, now(), now()),
	(130, 39, 13, FALSE, now(), now()),
	(131, 39, 3, FALSE, now(), now()),
	
	(132, 40, 14, TRUE, now(), now()),
	(133, 40, 8, FALSE, now(), now()),
	(134, 40, 15, FALSE, now(), now()),
	(135, 40, 13, FALSE, now(), now()),

	(136, 41, 5, TRUE, now(), now()),
	(137, 41, 4, FALSE, now(), now()),

	(138, 42, 9, TRUE, now(), now()),
	(139, 42, 10, FALSE, now(), now()),
	(140, 42, 14, FALSE, now(), now()),
	(141, 42, 15, FALSE, now(), now()),

	(142, 43, 9, TRUE, now(), now()),
	(143, 43, 10, FALSE, now(), now()),
	(144, 43, 14, FALSE, now(), now()),
	(145, 43, 15, FALSE, now(), now()),

	(146, 44, 15, TRUE, now(), now()),

	(147, 45, 11, TRUE, now(), now()),
	(148, 45, 5, FALSE, now(), now()),
	(149, 45, 4, FALSE, now(), now()),
	(150, 45, 16, FALSE, now(), now()),

	(151, 46, 11, TRUE, now(), now()),
	(152, 46, 5, FALSE, now(), now()),
	(153, 46, 4, FALSE, now(), now()),
	(154, 46, 16, FALSE, now(), now()),

	(155, 47, 11, TRUE, now(), now()),
	(156, 47, 4, FALSE, now(), now()),
	(157, 47, 6, FALSE, now(), now()),
	(158, 47, 12, FALSE, now(), now()),

	(159, 48, 11, TRUE, now(), now()),
	(160, 48, 3, FALSE, now(), now()),
	(161, 48, 4, FALSE, now(), now()),
	(162, 48, 6, FALSE, now(), now()),
	(163, 48, 7, FALSE, now(), now()),
	(164, 48, 8, FALSE, now(), now()),
	(165, 48, 12, FALSE, now(), now()),
	(166, 48, 16, FALSE, now(), now()),

	(167, 49, 13, TRUE, now(), now()),
	(168, 49, 14, FALSE, now(), now()),
	(169, 49, 15, FALSE, now(), now()),

	(170, 50, 13, TRUE, now(), now()),
	(171, 50, 7, FALSE, now(), now()),
	(172, 50, 14, FALSE, now(), now()),
	(173, 50, 15, FALSE, now(), now()),
	(174, 50, 3, FALSE, now(), now()),

	(175, 51, 13, TRUE, now(), now()),
	(176, 51, 3, FALSE, now(), now()),
	(177, 51, 6, FALSE, now(), now()),
	(178, 51, 7, FALSE, now(), now()),
	(179, 51, 8, FALSE, now(), now()),
	(180, 51, 9, FALSE, now(), now()),
	(181, 51, 10, FALSE, now(), now()),
	(182, 51, 12, FALSE, now(), now()),
	(183, 51, 14, FALSE, now(), now()),
	(184, 51, 15, FALSE, now(), now()),

	(185, 52, 15, TRUE, now(), now()),
	(186, 52, 8, FALSE, now(), now()),
	(187, 52, 14, FALSE, now(), now()),
	(188, 52, 13, FALSE, now(), now()),

	(189, 53, 15, TRUE, now(), now()),
	(190, 53, 8, FALSE, now(), now()),
	(191, 53, 14, FALSE, now(), now()),
	(192, 53, 13, FALSE, now(), now()),

	(193, 54, 12, TRUE, now(), now()),
	(194, 54, 11, FALSE, now(), now()),

	(195, 55, 12, TRUE, now(), now()),
	(196, 55, 6, FALSE, now(), now()),
	(197, 55, 11, FALSE, now(), now()),
	(198, 55, 4, FALSE, now(), now()),

	(199, 56, 9, TRUE, now(), now()),
	(200, 56, 10, FALSE, now(), now()),
	(201, 56, 14, FALSE, now(), now()),
	(202, 56, 15, FALSE, now(), now()),
	(203, 56, 13, FALSE, now(), now()),

	(204, 57, 9, TRUE, now(), now()),
	(205, 57, 10, FALSE, now(), now()),
	(206, 57, 14, FALSE, now(), now()),
	(207, 57, 15, FALSE, now(), now()),
	(208, 57, 4, FALSE, now(), now()),

	(209, 58, 9, TRUE, now(), now()),
	(210, 58, 10, FALSE, now(), now()),
	(211, 58, 14, FALSE, now(), now()),
	(212, 58, 15, FALSE, now(), now()),
	(213, 58, 4, FALSE, now(), now()),

	(214, 59, 9, TRUE, now(), now()),

	(215, 60, 9, TRUE, now(), now()),
	(216, 60, 10, FALSE, now(), now()),
	(217, 60, 14, FALSE, now(), now()),
	(218, 60, 15, FALSE, now(), now()),

	(219, 61, 9, TRUE, now(), now()),
	(220, 61, 10, FALSE, now(), now()),
	(221, 61, 14, FALSE, now(), now()),
	(222, 61, 15, FALSE, now(), now()),

	(223, 62, 4, TRUE, now(), now()),
	(224, 62, 16, FALSE, now(), now()),

	(225, 63, 4, TRUE, now(), now()),

	(226, 64, 4, TRUE, now(), now()),
	(227, 64, 10, FALSE, now(), now()),
	(228, 64, 9, FALSE, now(), now()),
	(229, 64, 16, FALSE, now(), now()),

	(230, 65, 4, TRUE, now(), now()),
	(231, 65, 12, FALSE, now(), now()),

	(232, 66, 4, TRUE, now(), now()),

	(233, 67, 4, TRUE, now(), now()),

	(234, 68, 4, TRUE, now(), now()),
	(235, 68, 5, FALSE, now(), now()),
	(236, 68, 14, FALSE, now(), now()),
	(237, 68, 15, FALSE, now(), now()),
	(238, 68, 13, FALSE, now(), now()),
	(239, 68, 9, FALSE, now(), now()),
	(240, 68, 3, FALSE, now(), now()),

	(241, 69, 3, TRUE, now(), now()),

	(242, 70, 3, TRUE, now(), now()),
	
	(243, 71, 3, TRUE, now(), now()),
	(244, 71, 6, FALSE, now(), now()),
	(245, 71, 4, FALSE, now(), now()),
	
	(246, 72, 16, TRUE, now(), now()),
	
	(247, 73, 16, TRUE, now(), now()),

	(248, 74, 16, TRUE, now(), now()),
	(249, 74, 7, FALSE, now(), now());