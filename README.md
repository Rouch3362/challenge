# Mobile Shop


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
