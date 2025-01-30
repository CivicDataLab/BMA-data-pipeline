GEOJSON_URLS = {
    "risk_points": "http://flood.bangkok.go.th:8443/geoserver/open_lift/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=open_lift%3Arisk_point&maxFeatures=50&outputFormat=application%2Fjson",
    "main_canal": "http://flood.bangkok.go.th:8443/geoserver/Bangkok_TH/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Bangkok_TH%3ACANAL_Main&maxFeatures=50&outputFormat=application%2Fjson",
    "districts_boundary": "http://flood.bangkok.go.th:8443/geoserver/Bangkok_TH/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Bangkok_TH%3AADMIN_DISTRICT_BND&maxFeatures=50&outputFormat=application%2Fjson",
    "flood_complaints": "https://publicapi.traffy.in.th/teamchadchart-stat-api/geojson/v1?output_format=json&name=Prajna&org=Civicdatalab&purpose=Visualisation&email=prajna@civicdatalab.in&limit=1000"

}

BUDGET_MIS_URL = "https://connect.bangkok.go.th/misbudget/bmabudget"

BUDGET_MIS_AUTH = {
    "username": "ocp-cdl",
    "password": "S345#Miv-976X"
}
