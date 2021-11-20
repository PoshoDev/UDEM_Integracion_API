START TRANSACTION;

DELIMITER $$
DROP PROCEDURE IF EXISTS AutomovilGetFecha $$
CREATE PROCEDURE AutomovilGetFecha(f1 DATE, f2 DATE)
BEGIN

  SELECT  u.id, ma.nombre, mo.modelo,
          mo.color, mo.precio, mo.foto
  FROM    modelo AS mo, unidad AS u, marca AS ma, (
          SELECT  id
          FROM    unidad
          WHERE   unidad.id NOT IN (
                  SELECT  unidad.id
                  FROM    unidad, reserva_unidad, reserva
                  WHERE   unidad.id=reserva_unidad.unidad
                          AND reserva_unidad.reserva=reserva.id
                          AND (
                              (f1<=reserva.fecha_desde AND f2>=reserva.fecha_desde)
                              OR (f1 <= reserva.fecha_hasta AND f2 >= reserva.fecha_hasta)
                              OR (reserva.fecha_desde<=f1 AND reserva.fecha_hasta>=f1)
                              OR (reserva.fecha_desde<=f2 AND reserva.fecha_hasta>=f2))
                          )
            ) AS mientras
    WHERE u.automovil=mo.id
          AND u.id=mientras.id
          AND mo.marca=ma.id;

END $$
DELIMITER ;

COMMIT;
