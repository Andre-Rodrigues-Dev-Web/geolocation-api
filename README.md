### Geolocation FreeAPI
Is a simple API develop in PYTHON and Flask, to integration in LocationIQ for free user :)

### How to teste API

Endpoint demo Request GET:

```
https://geolocation.contrateumdev.com.br/api/geocode?lat=-19.9177437&lon=-44.1000478
```

Response SUCCESS:

```json
[
    {
    "place_id": "320469537366",
    "osm_id": "28935774",
    "osm_type": "way",
    "licence": "https://locationiq.com/attribution",
    "lat": "-19.8238465",
    "lon": "-44.0076998",
    "boundingbox": [
        "-19.8264259",
        "-19.8214398",
        "-44.008683",
        "-44.0067474"
    ],
    "class": "highway",
    "type": "residential",
    "display_name": "Rua Ana Alvarenga Campos, Céu Azul, Ribeirão das Neves, Minas Gerais, 31585000, Brazil",
    "display_place": "Rua Ana Alvarenga Campos",
    "display_address": "Céu Azul, Ribeirão das Neves, Minas Gerais, 31585000, Brazil",
    "address": {
        "name": "Rua Ana Alvarenga Campos",
        "suburb": "Céu Azul",
        "city": "Ribeirão das Neves",
        "state": "Minas Gerais",
        "postcode": "31585000",
        "country": "Brazil",
        "country_code": "br"
        }
    }
]
```
### How to consume API in $.POST Jquery

```javascript
function getData()
{
    $.post({
        method: 'GET',
        url: 'https://geolocation.contrateumdev.com.br/api/geocode?lat=-19.9177437&lon=-44.1000478',
        success: function(resultado, status, xhr) {
            if (resultado) {
                console.log(resultado?.data)
            }else{
                error = JSON.parse(data);
                console.log(resultado?.data)
            }
        },
        error: function(data) {
            console.log(data.error)
        }
    })
}
```
