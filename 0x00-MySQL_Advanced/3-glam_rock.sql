-- Select band_name, difference between formed and split columns as lifespan from metal_bands table where main_style is 'Glam rock' and order them by lifespan in descending order
SELECT band_name, TIMESTAMPDIFF(YEAR, formed, split) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;

