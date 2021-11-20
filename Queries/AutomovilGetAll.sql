START TRANSACTION;

DELIMITER $$
DROP PROCEDURE IF EXISTS AutomovilGetAll $$
CREATE PROCEDURE AutomovilGetAll()
BEGIN

    SELECT  u.id, ma.nombre, mo.modelo,
            mo.color, mo.precio, mo.foto
    FROM    unidad AS u, marca AS ma, modelo AS mo
    WHERE   u.automovil=mo.id AND mo.marca=ma.id;

END $$
DELIMITER ;

COMMIT;
