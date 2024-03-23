import json
import unicodedata
import requests
import re
from django.shortcuts import render
# import conmariadbdb
# import csv
# import convertcsvtojson
# import bundlesdata
# import random

def datatofhir(request):

### Good Patient valided 

    f = open("pbmconnector/static/data/patient0124.json",'r')
    pat = f.read()
    patient = json.loads(pat)
    if patient:
        exito = "yes"
    else:
        exito = "no"
    print('Success read Patient file: ', exito)
    
### Good Condition valided 
    import codecs
    ff = open("pbmconnector/static/data/condition0124.json", encoding='latin-1')
    con = ff.read()
    
    # print(con)
    condition = json.loads(con)
    if condition:
        exito = "yes"
    else:
        exito = "no"
    print('Success read Condition file: ', exito)

### Good EpisodeOfCare valided
 
    eoc = open("pbmconnector/static/data/episodeofcare0124.json","r")
    eocare = eoc.read()
    episodeofcare = json.loads(eocare)
    if episodeofcare:
        exito = "yes"
    else:
        exito = "no"
    print('Success read EpisodeOfCare file: ', exito)

### Good for procedure valided

    pro = open("pbmconnector/static/data/procedure0124.json", encoding='latin-1')
    proce = pro.read()
    procedure = json.loads(proce)
    if procedure:
        exito = "yes"
    else:
        exito = "no"
    print('Success read Procedure file: ', exito)

 ### Good for Encounter valided   

    enc = open("pbmconnector/static/data/encounter0124v2.json", encoding="latin-1")
    encount = enc.read()
    encounter = json.loads(encount)
    if encounter:
        exito = "yes"
    else:
        exito = "no"
    print('Success read Encounter file: ', exito)

### Good for Observation valided

    obs = open("pbmconnector/static/data/observation0124.json","r")
    observa = obs.read()
    observation = json.loads(observa)
    if observation:
        exito = "yes"
    else:
        exito = "no"
    print('Success read Procedure file: ', exito)

### Good for MedicationAdministration valided

    medadmin = open("pbmconnector/static/data/medicaadmon0124v1.json","r")
    mead = medadmin.read()
    medicaadmin = json.loads(mead)
    if medicaadmin:
        exito = "yes"
    else:
        exito = "no"
    print('Success read Procedure file: ', exito)

#####


    # obs = open("pbmconnector/static/data/observationtest.py","r")
    # observa = obs.read()
    # observation = json.loads(observa)
    # print(observation[0])
    
# med = open("medicationadministration.py","r")
# medica = med.read()
# # print(medica)
# medicaadmin = json.loads(medica)
# print(medicaadmin[0])

# print(patient[1]['name'][0]['given'])
# print(patient)
# bund = bundlesdata.patient
# print(bund1)
#sql = "SELECT * FROM patients"
# connected.connMariadb(sql)






# Assign ID randomly
# id = random.randint(100000, 160000)
# y[0]['identifier'][0]['value'] = str(id)
# print(str(id))           
# url = "http://192.168.0.190:8080/fhir/Patient"
    url5 = "http://192.168.0.190:8080/fhir/Patient/2"
    urlwithoutID = "http://192.168.0.190:8080/fhir/Patient/"
# url = "http://192.168.0.190:8080/fhir"
    urlpatient = "http://192.168.0.190:8080/fhir/Patient"
    urlcondition = "http://192.168.0.190:8080/fhir/Condition"
    urlconditionup302 = "http://192.168.0.190:8080/fhir/Condition/302"
    urlprocedure = "http://192.168.0.190:8080/fhir/Procedure"
    urlepisodeofcare = "http://192.168.0.190:8080/fhir/EpisodeOfCare"
    urlencounter = "http://192.168.0.190:8080/fhir/Encounter"
    urlobservation = "http://192.168.0.190:8080/fhir/Observation"
    urlobservation1 = "http://192.168.0.190:8080/fhir/Observation"
    urlmedicaadmin = "http://192.168.0.190:8080/fhir/MedicationAdministration"

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    headersupdate = {'Content-type': 'application/fhir+json', 'Accept': 'text/plain'}
    # print('Numero de patients in file', len(patient))

    # for patadd in patient:
    #     r = requests.post(urlpatient, data=json.dumps(patadd), headers=headers)
    #     if r:
    #         print('Patient was created succesfully')
    #     else:
    #         print('Error for create patient')
    
    ###
    ##  For update record Condition we need to get from Hapi Fhir server first and
    ##  then make the necessary changes for PUT the update over the Hapi Fhir server
    ###
    
    
    # condic = condition[0]
       
    # getcondi = requests.get(urlconditionup302)
    # getcondjson = json.loads(getcondi.text)
    # print("cond recuperado", getcondjson )
    # getcondjson['code']['coding'][0]['display'] = condition[0]['code']['coding'][0]['display']
    # print("actualizado", getcondjson)
    # for cond in condition:
    #     rcc = requests.post(urlcondition, data=json.dumps(cond), headers=headers)
        
    #     if rcc:            
    #         print('Condition was created successfully')
    #     else:
    #         print('Error when Condition try to create')
##

    
    # for epoc in episodeofcare:
        
    #     r = requests.post(urlepisodeofcare, data=json.dumps(epoc), headers=headers)
    #     if r:
    #         print('EpisodeOfCare was created successfully')
    #     else:
    #         print('Error EpisodeOfCare try to create', r)

# r = requests.post(urlobservation, data=json.dumps(observation[0]), headers=headers)
# if r:
#     print('Registro exitoso Observation')
# else:
#     print('Error en registro Observation')
##

    # for procs in procedure:
    #     r = requests.post(urlprocedure, data=json.dumps(procs), headers=headers)
    #     if r:
    #         print('Registro exitoso de Procedure')
    #     else:
    #         print('Error en registro de Procedure')

##

# r = requests.post(urlencounter, data=json.dumps(encounter[0]), headers=headers)
# if r:
#     print('Registro exitoso de Encounter',r)
# else:
#     print('Error en registro de Encounter',r)


    # r = requests.post(urlobservation, data=json.dumps(observation[0]), headers=headers)
    # if r:
    #     print('Registro exitoso de Observation',r)
    # else:
    #     print('Error en registro de Observation',r)

    # r = requests.put(urlmedicaadmin, data=json.dumps(medicaadmin[0]), headers=headers)
    # if r:
    #     print('Registro exitoso MedicationAdministration')
    # else:
    #     print('Error en registro MedicationAdministration')
    # g = requests.get(url5)
    # if g:
    #     record = g.text
    #     jrecord = json.loads(record)
    #     jrecord['name'][0]['family'] = "Perez6"
    #     # print('Los datos son:')
    #     # print(jrecord['name'][20]['family'])
    #     # print(jrecord['name'])
    # else:
    #     print('hubo error en la lectura')
    # idpat = "2"
    # jrecordupdate = jrecord
    
    # print(jrecord["id"])
    # print(jrecordupdate['id'])
    # urlnew = patUpdate(urlwithoutID, idpat)
    
    # r.config['keep_alive'] = False
    # rr = requests.put(url5, data=json.dumps(jrecord), headers=headers)
    # if rr:
    #     print('Patient updated')
    # else:
    #     print('Error updating patient with ID patient', rr)
    # jrecordupdate['id'] =  idpat
    # jrecordupdate['identifier'][0]['value'] = idpat  
    
    # r = requests.put(urlnew, data=json.dumps(jrecordupdate), headers=headers)
    # if r:
    #     print('Patient updated')
    # else:
    #     print('Error patient updated', r)
    
    # r = 'No esta activo'
    # todosreg = traeIDs()
    # observa = {'obsfhir': observation, 'typeresource': 'Observation', 'status': r,
    #            "patient":jrecord, "todosreg": todosreg }
    
    idpatient = arrayPatient(patient)
    idconditions, idcondref = arrayCondition(condition)
    idencounter, diagreferences = arrayEncounter(encounter)
    idepisodeofcare = arrayEpisodeofcare(episodeofcare)
    idobservation = arrayObservation(observation)
    idmedicaadmin = arrayMedicationAdmin(medicaadmin)
    idprocedure = arrayProcedure(procedure)
    print('Array dimension of Diagnosis in Encounters: ', diagreferences[980])
    
    arrDiagsInEnconters, foundincond, fpe, npee = findDiagInEncounter(idencounter, idconditions, diagreferences)
    
    np, nofinded, totalpatients, notfindedreference = detectPatientAllresource(idpatient, idconditions, idcondref, idencounter, idepisodeofcare, 
                                            idobservation, idmedicaadmin, idprocedure)
    npp, nofindedp, totalpatientsp = detectPatientIntoProcedures(idpatient, idprocedure)
    npe, nofindede, totalpatientsp = detectPatientIntoEpisodeofcare(idpatient, idepisodeofcare)
    npm, nofoundm, totalpatientsp = detectPatientIntoMedica(idpatient, idmedicaadmin)
    npen, nofounden, totalpatientsp = detectPatientIntoEncounter(idpatient, idencounter)
    
    npob, nofoundob, totalpatientsp = detectPatientIntoObservation(idpatient, idobservation)
    
    observa = {"reporte": "Reporte de consitencia de datos","nopnotfinded": np,
               "pnotfinded": nofinded, "idpatient": idpatient, "idconditions": idconditions,
               "notfindedreference": notfindedreference, "totalpatients": totalpatients,
               "nofindedp": nofindedp, "npp": npp, "nofindede": nofindede, "npe": npe,
               "nofoundm": nofoundm, "npm": npm, "nofounden": nofounden, "npen": npen,
               "nofoundob": nofoundob, "npob": npob, "arrDiagsInEnconters": arrDiagsInEnconters,
               "foundincond": foundincond,"fpe": fpe, "npee": npee}
    
    return render(request, 'index.html', context=observa)

# g = requests.get(url5)
# if g:
#     record = g.text
#     jrecord = json.loads(record)
#     print('Los datos son:')
#     # print(jrecord['name'][20]['family'])
#     print(jrecord)
# else:
#     print('hubo error en la lectura')
    # -----temporal
# ccsvtojson = convertcsvtojson
# csvFilePath = r'./LoincTableCore.csv'
# jsonFilePath = r'./data.json'
# stringsData = ccsvtojson.csv_to_json(csvFilePath, jsonFilePath)
# print(stringsData[0]['LOINC_NUM'])


def patUpdate(urlwithoutID, idpat):
    urlnew = urlwithoutID+idpat
    print(urlnew)
    return urlnew

def traeIDs():
    urlbundle = "http://192.168.0.190:8080/fhir/Patient"
    bundle = requests.get(urlbundle)
    bundle1 = bundle.text
    bundle2 = json.loads(bundle1)
    # print("todos los pacientes: \n", json.loads(bundle1))
    # idstotal = bundle1['resourceType']
    # print(idstotal)
    linksarray = bundle2['entry']
    idsa = []
    idspatient = []
    for ids in linksarray:
        # print(ids['resource']['id'])
        idsa.append(ids['resource']['id'])
        idspatient.append(ids['resource']['identifier'][0]['value'])
        # if ids['resource']['id'] == "52":
        
    print(idsa, idspatient)
    
    try:
        ids = "2"
        idsa.index(ids)
        print('Si esta el identificador: ', ids)
    except ValueError:
        print('No se encuentra identificador', ids)
    # [0]['resource']['id']
    # print('Valor de primer id: ', linksarray)
    return bundle1

## Validation of unique patient

def uniquePatient(idpatient):
    print(idpatient)
    
def arrayPatient(patient):
    idpatients = []
    for ids in patient:
        idpatients.append(ids['identifier'][0]['value'])
    return idpatients

def arrayCondition(conditions):
    idconditions = []
    idcondref1 = []
    for ids in conditions:
        idconditions.append(ids['identifier'][0]['value'])
        idcondref1.append(ids['subject'])
    return idconditions, idcondref1

def arrayEpisodeofcare(episodeofcare):
    idepisodeofcare = []
    for ids in episodeofcare:
        idepisodeofcare.append(ids['identifier'][0]['value'])
    return idepisodeofcare

def arrayProcedure(procedure):
    idprocedure = []
    for ids in procedure:
        idprocedure.append(ids['identifier'][0]['value'])
    return idprocedure

def arrayEncounter(encounter):
    idencounter = []
    diagreferences = []
    for ids in encounter:
        idencounter.append(ids['identifier'][0]['value'])
        diagreferences.append(ids['diagnosis'][0]['condition']['reference'])
    return idencounter, diagreferences

def arrayObservation(observation):
    idobservation = []
    for ids in observation:
        idobservation.append(ids['identifier'][0]['value'])
    return idobservation

def arrayMedicationAdmin(medicaadmin):
    idmedicaadmin = []
    for ids in medicaadmin:
        idmedicaadmin.append(ids['identifier'][0]['value'])
    return idmedicaadmin

def detectPatientAllresource(idpatient,  idconditions, idconditionsreference, idencounter, idepisodeofcare,
                             idobsevation, idmedicaadmin, idprocedure):
## find the ID patient in all resource
# patientes encontrados
    np = 0
    fp = 0
    fp1 = 0
    totalpatients = len(idpatient)
    nofinded = []
    notfindedreference = []
    for elemento in idpatient:
        
        # indexfinded = idcondictions.index(elemento)
        # findedpatient = [idconditions for i in idconditions if elemento in idconditions]
        findedpatient = any(elemento in i for i in idconditions)
        # findedpatientr = any(elemento in i for i in idconditionsreference)
        # for i in idconditionsreference:
        #     if elemento in i['reference']:
        #         fp1 = fp1 + 1
        #         print('Valor de reference: ', i['reference'], elemento, fp1)
            # else:
            #     print('No se encontro elemento: ', i['reference'], elemento)    
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Si encontrado: ', elemento, ":::", np)
        else:
            finded = "No"
            np = np + 1
            nofinded.append(elemento)
            notfindedreference.append(elemento)
            # print('No encontrado: ', elemento, ":::", np)
    if fp == totalpatients:
        print('Conditions have diags for each Patient')
    else:
        print('Conditions have not diags on: ', fp, np)    
    return np, nofinded, totalpatients, notfindedreference 

### For find if Procedures has all patients
#
def detectPatientIntoProcedures(idpatient, idprocedure):
## find the ID patient in Procedures
# Finded patients
    np = 0
    fp = 0
    totalpatients = len(idpatient)
    nofinded = []
    for elemento in idpatient:
            
        findedpatient = any(elemento in i for i in idprocedure)
           
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Finded in Procedures: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            nofinded.append(elemento)
            print('No finded in procedures: ', elemento, ":::", np)
            
    if fp == totalpatients:
        print('All Patients are in Procedure')
    else:
        print('Patients have not in Procedures: ', fp, np)    
    return np, nofinded, totalpatients  


## For find if EpisodeOfCare has all patients
#
def detectPatientIntoEpisodeofcare(idpatient, idepisodeofcare):
## find the ID patient in Procedures
# Finded patients
    np = 0
    fp = 0
    totalpatients = len(idpatient)
    nofinded = []
    for elemento in idpatient:
            
        findedpatient = any(elemento in i for i in idepisodeofcare)
           
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Found in EpisodeOfCare: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            nofinded.append(elemento)
            print('No found in EpisodeOfCare: ', elemento, ":::", np)
            
    if fp == totalpatients:
        print('All Patients are in EpisodeOfCare')
    else:
        print('Patients have not in EpisodeOfCare: ', fp, np)    
    return np, nofinded, totalpatients  

## For find if MedicationAdministration has all patients
#
def detectPatientIntoMedica(idpatient, idmedicaadmin):
## find the ID patient in Procedures
# Finded patients
    np = 0
    fp = 0
    totalpatients = len(idpatient)
    nofound = []
    for elemento in idpatient:
            
        findedpatient = any(elemento in i for i in idmedicaadmin)
           
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Found in MedicationAdministration: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            nofound.append(elemento)
            print('No foundd in MedicationAdministration: ', elemento, ":::", np)
            
    if fp == totalpatients:
        print('All Patients are in MedicationAdministration')
    else:
        print('Patients have not in MedicationAdministration: ', fp, np)    
    return np, nofound, totalpatients  


## For find if Encounter has all patients
#
def detectPatientIntoEncounter(idpatient, idencounter):
## find the ID patient in Procedures
# Finded patients
    np = 0
    fp = 0
    totalpatients = len(idpatient)
    nofound = []
    for elemento in idpatient:
            
        findedpatient = any(elemento in i for i in idencounter)
           
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Found in Encounters: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            nofound.append(elemento)
            print('No foundd in Encounters: ', elemento, ":::", np)
            
    if fp == totalpatients:
        print('All Patients are in Encounters')
    else:
        print('Patients have not in Encounters: ', fp, np)    
    return np, nofound, totalpatients  


## For find if Observation has all patients
#
def detectPatientIntoObservation(idpatient, idobservation):
## find the ID patient in Procedures
# Finded patients
    np = 0
    fp = 0
    totalpatients = len(idpatient)
    nofound = []
    for elemento in idpatient:
            
        findedpatient = any(elemento in i for i in idobservation)
           
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Found in Observation: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            nofound.append(elemento)
            print('No foundd in Observation: ', elemento, ":::", np)
            
    if fp == totalpatients:
        print('All Patients are in Observation')
    else:
        print('Patients have not in Observation: ', fp, np)    
    return np, nofound, totalpatients 

## For find if Observation has all patients
#
def detectMedicaInObserva(idpatient, idmedicaadmin, idcondition):
## find the ID patient in Procedures
# Finded patients
    np = 0
    fp = 0
    totalpatients = len(idpatient)
    nofound = []
    for elemento in idpatient:
            
        findedpatient = any(elemento in i for i in idobservation)
           
        if findedpatient >0:
            finded = "Yes"
            fp = fp + 1
            # print('Found in Observation: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            nofound.append(elemento)
            print('No foundd in Observation: ', elemento, ":::", np)
            
    if fp == totalpatients:
        print('All Patients are in Observation')
    else:
        print('Patients have not in Observation: ', fp, np)    
    return np, nofound, totalpatients 

##
# Find the diagnosis in Encounters
##

def findDiagInEncounter(idencounter, idconditions, diagreferences):
    notfound = []
    foundincond = []
    fp = 0
    np = 0
    for ids in idconditions:
        findiaginrefEnc = any(ids in i for i in diagreferences)
           
        if findiaginrefEnc >0:
            finded = "Yes"
            fp = fp + 1
            foundincond.append(ids)
            # print('Found in Observation: ', elemento, ":::", fp)
            
        else:
            finded = "No"
            np = np + 1
            notfound.append(ids)
            # print('No foundd in Encounters: ', ids, ":::", np)
    print('Encontrados: ', fp, " No encontrados: ", np)
    
    return notfound, foundincond, fp, np