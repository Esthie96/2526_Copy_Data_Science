-- Active: 1759398218711@@aws-1-eu-north-1.pooler.supabase.com@6543
SELECT boetes, spelers.naam
FROM spelers INNER JOIN boetes
on spelers.spelersnr = boetes.spelersnr;

