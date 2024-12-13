# BMA GeoJSON API Documentation

## Endpoints

### Get GeoJSON Data
`GET /api/v1/geojson/{layer_type}/`

Fetches GeoJSON data from Bangkok's GeoServer.

#### Path Parameters
- `layer_type` (required): Type of GeoJSON layer
  - `risk_points`: Risk point locations
  - `main_canal`: Main canal network
  - `districts_boundary`: District boundaries

#### Responses

##### 200 Success
```json
{
    "success": true,
    "data": {
        "type": "FeatureCollection",
        "features": [...]
    },
    "error": null
}
```

##### 400 Bad Request
```json
{
    "success": false,
    "error": "Invalid layer type"
}
```

##### 500 Server Error
```json
{
    "success": false,
    "error": "Request Error"
}
```