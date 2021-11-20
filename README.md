# 🚗 UDEM_Integracion
API e aplicación web para un sistema de renta de autos.



# 🗃️ API

Ejemplos del uso de nuestro API:



<u>Ver Inventario Completo:</u>

```http
[url]/inventario/
```

```json
{
    '0':{
        'id': 1,
        'modelo': 1,
        'color': 'Corvette',
        'precio': 'Rayo McQueen',
        'unidades': 6969
    },
    '1':{
        'id': 2, 
        'modelo': 2, 
        'color': 'Sedan', 
        'precio': 'Blanco', 
        'unidades': 2000
    },
    '2':{
        'id': 3, 
        'modelo': 1, 
        'color': 'Camaro', 
        'precio': 'Bumblebee', 
        'unidades': 420
    },
}
```



<u>Ver Inventario por Marcas:</u>

```http
[url]/inventario/?marca=Chevrolet
```

```json
{
    '0':{
        'id': 1,
        'modelo': 'Corvette',
        'color': 'Rayo McQueen',
        'precio': 6969,
        'unidades': 1
    },
    '1':{
        'id': 3,
        'modelo': 'Camaro',
        'color': 'Bumblebee',
        'precio': 420,
        'unidades': 2
    },
}
```



# lol

![](https://github.com/PoshoDev/UDEM_Integracion/blob/main/lol.png?raw=true)
