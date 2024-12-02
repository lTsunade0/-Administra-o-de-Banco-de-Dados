
CREATE DATABASE dopib;


USE dopib;


EXPLAIN SELECT * FROM pib_corrigido;


CREATE INDEX idx_pib_corrigido_sc ON pib_corrigido(sc(100));
CREATE INDEX idx_pib_corrigido_pib ON pib_corrigido(pib);




INSERT INTO pib_por_estado (sc, pib_total)
SELECT 
    sc, 
    SUM(pib) AS pib_total
FROM 
    pib_corrigido
GROUP BY 
    sc;




CREATE INDEX idx_pib_por_estado_sc ON pib_por_estado(sc(100));



SELECT * FROM pib_por_estado;



CREATE TABLE pib_maior_menor_estado AS
SELECT 
    sc AS estado,
    MAX(pib) AS maior_pib,
    MIN(pib) AS menor_pib
FROM 
    pib_corrigido
GROUP BY 
    sc;


CREATE INDEX idx_pib_maior_menor_estado_sc ON pib_maior_menor_estado(estado(100));



SELECT * FROM pib_maior_menor_estado;

