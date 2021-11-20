# 🚗 UDEM_Integracion
API e aplicación web para un sistema de renta de autos.



# 🗃️ API

Ejemplos del uso de nuestro API:




| Parámetro          | Descripción                                                  |
| ------------------ | ------------------------------------------------------------ |
| marca *(opcional)* | La marca de automóvil que se desea buscar.                   |
| desde *(opcional)* | La fecha desde la cual se buscan automóviles disponibles. *Requiere del parámetro **hasta** si se usa.* |
| hasta *(opcional)* | La fecha hasta la cual se buscan automóviles disponibles. *Requiere del parámetro **desde** si se usa.* |

<details>
<summary>Ejemplo: Ver Inventario Completo</summary>

```http
GET udem-autos-api.herokuapp.com/inventario
```

```json
{
  "inventario": [
    {
      "color": "Rayo McQueen",
      "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
      "id": 2,
      "modelo": "Corvette",
      "nombre": "Chevrolet",
      "precio": 6969
    },
    {
      "color": "Rayo McQueen",
      "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
      "id": 4,
      "modelo": "Corvette",
      "nombre": "Chevrolet",
      "precio": 6969
    },
    {
      "color": "Rayo McQueen",
      "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
      "id": 5,
      "modelo": "Corvette",
      "nombre": "Chevrolet",
      "precio": 6969
    },
    {
      "color": "Bumblebee",
      "foto": "https://image.winudf.com/v2/image/Y29tLk92ZXJ3YXRjaGRldi5NRUNITU9EX3NjcmVlbnNob3RzXzBfMTYyMGRmYzA/screen-0.jpg?fakeurl=1&type=.jpg",
      "id": 1,
      "modelo": "Camaro",
      "nombre": "Chevrolet",
      "precio": 420
    },
    {
      "color": "Blanco",
      "foto": "https://media.mattel.com/root/HWCarsCatalog/Web/MainImage/DTX49_c_17_003.png",
      "id": 3,
      "modelo": "Sedan",
      "nombre": "Mercedes-Benz",
      "precio": 2000
    },
    {
      "color": "Blanco",
      "foto": "https://media.mattel.com/root/HWCarsCatalog/Web/MainImage/DTX49_c_17_003.png",
      "id": 6,
      "modelo": "Sedan",
      "nombre": "Mercedes-Benz",
      "precio": 2000
    }
  ]
}
```
</details>


<details>
<summary>Ejemplo: Ver Inventario Por Marcas</summary>

```http
GET udem-autos-api.herokuapp.com/inventario?marca=Chevrolet
```

```json
{
  "inventario": [
    {
      "color": "Rayo McQueen",
      "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
      "id": 2,
      "modelo": "Corvette",
      "nombre": "Chevrolet",
      "precio": 6969
    },
    {
      "color": "Rayo McQueen",
      "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
      "id": 4,
      "modelo": "Corvette",
      "nombre": "Chevrolet",
      "precio": 6969
    },
    {
      "color": "Rayo McQueen",
      "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
      "id": 5,
      "modelo": "Corvette",
      "nombre": "Chevrolet",
      "precio": 6969
    },
    {
      "color": "Bumblebee",
      "foto": "https://image.winudf.com/v2/image/Y29tLk92ZXJ3YXRjaGRldi5NRUNITU9EX3NjcmVlbnNob3RzXzBfMTYyMGRmYzA/screen-0.jpg?fakeurl=1&type=.jpg",
      "id": 1,
      "modelo": "Camaro",
      "nombre": "Chevrolet",
      "precio": 420
    }
  ]
}
```

</details>



<u>Realizar una reserva:</u>

```http
GET udem-autos-api.herokuapp.com/reserva
```

| Parámetro          | Descripción                                                  |
| ------------------ | ------------------------------------------------------------ |
| id1                | El ID del primer automóvil que se desea reservar.            |
| id2 *(opcional)*   | El ID del segundo automóvil que se desea reservar.           |
| id3 *(opcional)*   | El ID del tercer automóvil que se desea reservar.            |
| desde *(opcional)* | La fecha desde la cual se va a reservar.                     |
| hasta *(opcional)* | La fecha hasta la cual se va a reservar.                     |
| cuenta             | La cuenta de banco del usuario que va a realizar la transacción. |
| pin                | La contraseña de la cuenta de banco que se va a usar.        |





# lol

![](https://github.com/PoshoDev/UDEM_Integracion/blob/main/lol.png?raw=true)
