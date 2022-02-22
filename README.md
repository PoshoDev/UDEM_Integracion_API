# 🚗 UDEM_Integracion
API e aplicación web para un sistema de renta de autos. Lol.



# 🗃️ API

Ejemplos del uso de nuestro API:



### <u>Inventario</u>


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
[
  {
    "color": "Rayo McQueen",
    "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
    "id": 2,
    "marca": "Chevrolet",
    "modelo": "Corvette",
    "precio": 6969
  },
  {
    "color": "Rayo McQueen",
    "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
    "id": 4,
    "marca": "Chevrolet",
    "modelo": "Corvette",
    "precio": 6969
  },
  {
    "color": "Rayo McQueen",
    "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
    "id": 5,
    "marca": "Chevrolet",
    "modelo": "Corvette",
    "precio": 6969
  },
  {
    "color": "Bumblebee",
    "foto": "https://image.winudf.com/v2/image/Y29tLk92ZXJ3YXRjaGRldi5NRUNITU9EX3NjcmVlbnNob3RzXzBfMTYyMGRmYzA/screen-0.jpg?fakeurl=1&type=.jpg",
    "id": 1,
    "marca": "Chevrolet",
    "modelo": "Camaro",
    "precio": 420
  },
  {
    "color": "Blanco",
    "foto": "https://media.mattel.com/root/HWCarsCatalog/Web/MainImage/DTX49_c_17_003.png",
    "id": 3,
    "marca": "Mercedes-Benz",
    "modelo": "Sedan",
    "precio": 2000
  },
  {
    "color": "Blanco",
    "foto": "https://media.mattel.com/root/HWCarsCatalog/Web/MainImage/DTX49_c_17_003.png",
    "id": 6,
    "marca": "Mercedes-Benz",
    "modelo": "Sedan",
    "precio": 2000
  }
]
```
</details>


<details>
<summary>Ejemplo: Ver Inventario Por Marcas</summary>

```http
GET udem-autos-api.herokuapp.com/inventario/?marca=Chevrolet
```

```json
[
  {
    "color": "Rayo McQueen",
    "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
    "id": 2,
    "marca": "Chevrolet",
    "modelo": "Corvette",
    "precio": 6969
  },
  {
    "color": "Rayo McQueen",
    "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
    "id": 4,
    "marca": "Chevrolet",
    "modelo": "Corvette",
    "precio": 6969
  },
  {
    "color": "Rayo McQueen",
    "foto": "https://i.pinimg.com/originals/7d/43/8c/7d438c6693b7844806db4ed3e8cab54f.jpg",
    "id": 5,
    "marca": "Chevrolet",
    "modelo": "Corvette",
    "precio": 6969
  },
  {
    "color": "Bumblebee",
    "foto": "https://image.winudf.com/v2/image/Y29tLk92ZXJ3YXRjaGRldi5NRUNITU9EX3NjcmVlbnNob3RzXzBfMTYyMGRmYzA/screen-0.jpg?fakeurl=1&type=.jpg",
    "id": 1,
    "marca": "Chevrolet",
    "modelo": "Camaro",
    "precio": 420
  }
]
```

</details>


<details>
<summary>Ejemplo: Ver Inventario Por Fechas</summary>

```http
GET udem-autos-api.herokuapp.com/inventario/?desde=2021-11-20&hasta=2021-11-22
```

```
[
  {
    "color": "Bumblebee",
    "foto": "https://image.winudf.com/v2/image/Y29tLk92ZXJ3YXRjaGRldi5NRUNITU9EX3NjcmVlbnNob3RzXzBfMTYyMGRmYzA/screen-0.jpg?fakeurl=1&type=.jpg",
    "id": 1,
    "marca": "Chevrolet",
    "modelo": "Camaro",
    "precio": 420
  },
  {
    "color": "Blanco",
    "foto": "https://media.mattel.com/root/HWCarsCatalog/Web/MainImage/DTX49_c_17_003.png",
    "id": 3,
    "marca": "Mercedes-Benz",
    "modelo": "Sedan",
    "precio": 2000
  },
  {
    "color": "Blanco",
    "foto": "https://media.mattel.com/root/HWCarsCatalog/Web/MainImage/DTX49_c_17_003.png",
    "id": 6,
    "marca": "Mercedes-Benz",
    "modelo": "Sedan",
    "precio": 2000
  }
]
```

</details>



### <u>Reserva</u>


| Parámetro          | Descripción                                                  |
| ------------------ | ------------------------------------------------------------ |
| id1                | El ID del primer automóvil que se desea reservar.            |
| id2 *(opcional)*   | El ID del segundo automóvil que se desea reservar.           |
| id3 *(opcional)*   | El ID del tercer automóvil que se desea reservar.            |
| desde              | La fecha desde la cual se va a reservar.                     |
| hasta              | La fecha hasta la cual se va a reservar.                     |
| cuenta             | La cuenta de banco del usuario que va a realizar la transacción. |
| pin                | La contraseña de la cuenta de banco que se va a usar.        |

<details>
<summary>Ejemplo: Realizar una Reserva</summary>

```http
GET http://localhost:5000/reserva/?desde=2023-11-20&hasta=2023-11-22&id1=2&id2=4&id3=5&cuenta=4255555567&pin=123
```

```
{
  "message": "¡Reserva exitosa!",
  "precio": 41814,
  "reserva": 39
}
```

</details>






# lol

![](https://github.com/PoshoDev/UDEM_Integracion/blob/main/lol.png?raw=true)
