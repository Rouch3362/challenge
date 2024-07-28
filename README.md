# Mobile Shop

## suggestion for project features

* #### updating status (availability) of products.
* #### deleting products.
* #### discounting on products.
* #### rating for products.
* #### sorting based on price, popularity, count etc.
* #### most sold phones in last month or year.


## Project Paths

### Creating New Brand

```http
POST /brands/new
```

### Getting Brands
```http
GET /brands
```
#### Query Parameter

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `brand` | `string` | filtering based on brand name |
| `region` | `string` | filtering based on brand region |



```http
POST /products/new
```

### Getting Phones
```http
GET /products
```
#### Query Parameter

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `brand` | `string` | filtering based on phone brand name |
| `region` | `string` | filtering based on phone region |
| `same_region` | `bool` | returns if phone region and brand region are the same |

