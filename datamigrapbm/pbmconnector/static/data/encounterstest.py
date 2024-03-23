[{
    "resourceType": "Encounter",
    
    "identifier":  [
        {
            "system": "hospitalNaval",
            "value": "125477encount1"
        }
    ],
    "status": "finished",
    "class": {
     
        "system": "http://terminology.hl7.org/ValueSet/v3-ActEncounterCode",
        "code": "IMP"
    },
    "subject": {
        "reference": "Patient?identifier=hospitalNaval|125477"
    },
    "episodeOfCare": {
        "reference": "EpisodeOfCare?identifier=hospitalNaval|125477Ep1"
    },
    "serviceType": {
        "coding":  [
            {
                "display": "Allgemeine Chirurgie",
                "system": "http://fhir.de/CodeSystem/dkgev/Fachabteilungsschluessel",
                "code": "1500"
            }
        ]
    },
    "period": {
        "start": "2019-01-02T13:10:00-06:00",
        "end": "2019-01-10T05:19:00-06:00"
    },
    "location":  [
        {
            "location": {
                "display": "Allgemeine Chirurgie",
                "identifier": {
                    "system": "http://fhir.de/CodeSystem/dkgev/Fachabteilungsschluessel",
                    "value": "1500"
                }
            }
        }
    ],
    "diagnosis":  [
        {
            "condition": {
                "reference": "Condition?identifier=hospitalNaval|125477diag1"
            },
            "use": {
                "coding":  [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                        "code": "AD"
                    }
                ]
            }
        },
        {
            "condition": {
                "reference": "Condition?identifier=hospitalNaval|125477diag2"
            },
            "use": {
                "coding":  [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/diagnosis-role",
                        "code": "CC"
                    }
                ]
            }
        },
        {
            "condition": {
                "reference": "Procedure?identifier=hospitalNaval|125477cas1proc1"
            }
        }
    ]
}]
