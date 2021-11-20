START TRANSACTION;

DELIMITER $$
DROP PROCEDURE IF EXISTS AutomovilGetMarca $$
CREATE PROCEDURE AutomovilGetMarca(_marca CHAR(32))
BEGIN

  SELECT  u.id, ma.nombre, mo.modelo,
          mo.color, mo.precio, mo.foto
  FROM    unidad AS u, marca AS ma, modelo AS mo
  WHERE   u.automovil=mo.id AND mo.marca=ma.id
          AND ma.nombre=_marca;

END $$
DELIMITER ;

COMMIT;
