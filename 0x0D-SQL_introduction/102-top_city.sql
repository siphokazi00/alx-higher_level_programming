-- This script displays the tope 3 of cities' temp during Jul and Aug ordered by temp.
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;

