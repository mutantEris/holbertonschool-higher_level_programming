-- counts similar scores
SELECT score, COUNT(score) number FROM second_table ORDER BY number DESC;
