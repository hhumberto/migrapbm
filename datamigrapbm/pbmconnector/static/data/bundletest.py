{
  "resourceType": "Bundle",
  "id": "73a99d81-8d0c-4249-bacc-a4b4ddbec6d0",
  "meta": {
    "lastUpdated": "2023-12-31T05:31:05.779+00:00"
  },
  "type": "searchset",
  "total": 2,
  "link": [ {
    "relation": "self",
    "url": "http://localhost:8080/fhir/Patient?_pretty=true"
  } ],
  "entry": [ {
    "fullUrl": "http://localhost:8080/fhir/Patient/52",
    "resource": {
      "resourceType": "Patient",
      "id": "52",
      "meta": {
        "versionId": "1",
        "lastUpdated": "2023-12-19T21:54:39.866+00:00",
        "source": "#MvucS800Ct3m8dji"
      },
      "identifier": [ {
        "system": "localHospitalName",
        "value": "patient1"
      } ],
      "name": [ {
        "use": "official",
        "family": "One",
        "given": [ "Patient" ]
      } ],
      "gender": "male",
      "birthDate": "2010-11-25"
    },
    "search": {
      "mode": "match"
    }
  }, {
    "fullUrl": "http://localhost:8080/fhir/Patient/2",
    "resource": {
      "resourceType": "Patient",
      "id": "2",
      "meta": {
        "versionId": "3",
        "lastUpdated": "2023-12-23T05:11:29.966+00:00",
        "source": "#EZI7h1YAbSlGhykr"
      },
      "identifier": [ {
        "system": "localHospitalName",
        "value": "245698"
      } ],
      "name": [ {
        "use": "official",
        "family": "Perez",
        "given": [ "Patient" ]
      } ],
      "gender": "female",
      "birthDate": "2010-11-25"
    },
    "search": {
      "mode": "match"
    }
  } ]
}