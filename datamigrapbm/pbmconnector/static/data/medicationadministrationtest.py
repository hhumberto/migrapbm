[{
    "resourceType": "MedicationAdministration",
    "identifier":  [
        {
            "system": "hospitalNaval",
            "value": "125477cas1trans1"

        }
    ],
    "status": "completed",

    "subject": {
        "reference": "Patient?identifier=hospitalNaval|125477"
    },
    "context": {
        "reference": "Encounter?identifier=hospitalNaval|125477encount1"

    },
    "medicationCodeableConcept": {
        "coding":  [
            {
                "system": "http://snomed.info/sct",
                "code": "256395009",
           
                "display": "Platelet product (product)"

            }
        ]
    },
    "dosage": {
        "dose": {
            "unit": "{count}",
 
            "system": "http://unitsofmeasure.org",
            "value": 1
        }
    },
    "effectiveDateTime": "2019-06-01T12:00:00-06:00"

}]
