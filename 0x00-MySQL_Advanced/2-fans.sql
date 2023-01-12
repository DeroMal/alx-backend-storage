-- Select origin, sum of nb_fans from metal_bands table, group them by origin and order them by sum of nb_fans in descending order
SELECT origin, SUM(nb_fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

