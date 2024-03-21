SELECT name,
      ROUND((salary*10)/100, 2) AS tax
FROM people
WHERE salary > 3000;