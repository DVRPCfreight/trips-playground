COPY(
SELECT row_to_json(qq) FROM (
SELECT q.paths, q.timestamps, t.vehicle as vendor
FROM trips t
INNER JOIN
(SELECT tripid, ARRAY_AGG(ARRAY[longitude, latitude] ORDER BY unixtime) paths, ARRAY_AGG(unixtime ORDER BY unixtime) timestamps 
    FROM waypoints 
    GROUP BY tripid) q
on t.tripid = q.tripid
WHERE t.vehicle != 1
) qq
)
TO 'C:\Temp\tripsv1.json';
