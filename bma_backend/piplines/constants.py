GEOJSON_URLS = {
    "risk_points": "http://flood.bangkok.go.th:8443/geoserver/open_lift/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=open_lift%3Arisk_point&maxFeatures=50&outputFormat=application%2Fjson",
    "main_canal": "http://flood.bangkok.go.th:8443/geoserver/Bangkok_TH/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Bangkok_TH%3ACANAL_Main&maxFeatures=50&outputFormat=application%2Fjson",
    "districts_boundary": "http://flood.bangkok.go.th:8443/geoserver/Bangkok_TH/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Bangkok_TH%3AADMIN_DISTRICT_BND&maxFeatures=50&outputFormat=application%2Fjson"

}
BUDGET_MIS_API = "https://connect.bangkok.go.th/misbudget/bmabudget?source_id='01'&book_id='0'&fiscal_year='68'&department_id='11000000'&exp_object_id='07'"
