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
  - `flood_complaints`: Traffy fondue flood complaints

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



# **Budget MIS API Documentation**

## **Endpoint**
`GET /api/v1/budget_mis/`

Fetches budget information from Bangkok's MIS budget system.

---

## **Query Parameters**

| **Parameter**     | **Description**                      | **Default**  | **Example Values**                |
|------------------|--------------------------------------|--------------|-----------------------------------|
| `source_id`       | Funding source ID                   | `01`         | `01` (Annual Budget), `02` (Additional Budget) |
| `book_id`         | Budget document identifier          | `0`          | `0` (Annual Budget), `1-9` (Additional Budgets) |
| `fiscal_year`     | Fiscal year of the budget           | `66`         | `66` (corresponding to 2566 BE), `67` |
| `department_id`   | Department code                     | `11000000`   | `11000000` (Bureau), `xxxx0000` (District Office) |
| `exp_object_id`   | Expenditure category                | `07`         | `01` (Salaries), `07` (Other Expenditures) |

---

## **Responses**

### **200 Success**
```json
{
    "success": true,
    "data": [
        {
            "DEPARTMENT_NAME": "Department Name",
            "SECTOR_NAME": "Sector Name",
            "PROGRAM_NAME": "Program Name",
            "FUNC_NAME": "Project Function Name",
            "EXPENDITURE_NAME": "Expenditure Description",
            "FUNC_ID": "Project Function Code",
            "APPROVE_ON_HAND": "Approved Budget Amount",
            "ALLOT_APPROVE": "Approved Allocation Amount",
            "ALLOT_DATE": "Allocation Approval Date",
            ...
        }
    ],
    "status_code": 200
}
```

---

### **400 Bad Request**
```json
{
    "success": false,
    "error": "Invalid request parameters"
}
```

---

### **500 Server Error**
```json
{
    "success": false,
    "error": "Request Error"
}
```

---

## **Authentication**
The Budget MIS API requires **basic authentication**:

- **Username**: `ocp-cdl`  
- **Password**: `S345#Miv-976X`  

---
