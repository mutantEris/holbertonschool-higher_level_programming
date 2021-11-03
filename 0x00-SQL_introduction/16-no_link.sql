-- lists scores and names
SELECT score, name FROM second_table WHERE name IS NOT NULL SORT BY score DESC;
