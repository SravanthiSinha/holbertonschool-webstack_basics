-- computes the score average of all records in the table second_table
SELECT  SUM(score)/COUNT(score) AS average FROM second_table;
