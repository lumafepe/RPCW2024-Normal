from rdflib import Graph,URIRef,Literal,Namespace
from rdflib.namespace import RDF,OWL
import json
import csv
from collections import defaultdict

ids=0

g=Graph()
g.parse("medical.ttl")

namespace = Namespace("http://www.example.org/disease-ontology#")


with open("Disease_Syntoms.csv") as f:
    csv_reader = csv.DictReader(f)
    symptoms=set()
            
    for row in csv_reader:
        Disease = row["Disease"].strip().replace(' ','_')
        Symptoms = [row["Symptom_1"],row["Symptom_2"],row["Symptom_3"],row["Symptom_4"],row["Symptom_5"],row["Symptom_6"],row["Symptom_7"],row["Symptom_8"],row["Symptom_9"],row["Symptom_10"],row["Symptom_11"],row["Symptom_12"],row["Symptom_13"],row["Symptom_14"],row["Symptom_15"],row["Symptom_16"],row["Symptom_17"]]
        Symptoms = list(map(lambda x: x.strip().replace(' ','_'),filter(lambda x: x!='',Symptoms)))
        
        URIDisease = URIRef(f"{namespace}{Disease}")
        
        #add doença
        g.add((URIDisease,RDF.type,namespace.Disease))
        URIDiseaseInstance = URIRef(f"{namespace}{Disease}_{ids}")
        ids+=1
        g.add((URIDiseaseInstance,RDF.type,URIDisease))
        
        for sim in Symptoms:
            URISymptom = URIRef(f"{namespace}{sim}")
            if sim not in symptoms:
                symptoms.add(sim)
                g.add((URISymptom,RDF.type,namespace.Symptom))
            g.add((URIDiseaseInstance,namespace.hasSymptom,URISymptom))
        
with open("Disease_Description.csv") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        Disease = row["Disease"].strip().replace(' ','_')
        Description = row["Description"]
        
        URIDisease = URIRef(f"{namespace}{Disease}")
        
        g.add((URIDisease,URIRef(f"{namespace}description"),Literal(Description)))

    
with open("med_doencas.ttl","w") as f:
    f.write(g.serialize())
    
treatments=set()

with open("Disease_Treatment.csv") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        Disease = row["Disease"].strip().replace(' ','_')
        Precautions = list(map(lambda x: x.strip().replace(' ','_'),filter(lambda x:x!='',[row["Precaution_1"],row["Precaution_2"],row["Precaution_3"],row["Precaution_4"]])))
        
        URIDisease = URIRef(f"{namespace}{Disease}")
        
        for precausion in Precautions:
            URIPrecaution = URIRef(f"{namespace}{precausion}")
            if precausion not in treatments:
                treatments.add(precausion)
                g.add((URIPrecaution,RDF.type,namespace.Treatment))
        
            g.add((URIDisease,namespace.hasTreatment,URIPrecaution))
            
            
with open("med_tratamentos.ttl","w") as f:
    f.write(g.serialize())
    
ids=0
with open("pg54009.json") as f:
    data = json.load(f)
    for person in data:
        URIPerson = URIRef(f"{namespace}PERSON{ids}")
        ids+=1
        Symptoms=list(map(lambda x: x.strip().replace(' ','_'),person['sintomas']))
        
        g.add((URIPerson,RDF.type,namespace.Patient))
        g.add((URIPerson,namespace.name,Literal(person['nome'])))
        for sim in Symptoms:
            URISymptom = URIRef(f"{namespace}{sim}")
            g.add((URIPerson,namespace.exhibitsSymptom,URISymptom))

with open("med_doentes.ttl","w") as f:
    f.write(g.serialize())
    