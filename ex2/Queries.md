# Quantas doenças estão presentes na ontologia?
```
PREFIX : <http://www.example.org/disease-ontology#>
SELECT (COUNT(?DOENÇAS) as ?NÚMERODOENÇAS)
WHERE{
 ?DOENÇAS a :Disease.
}
```
## R: 42
# Que doenças estão associadas ao sintoma "yellowish_skin"?
```
PREFIX : <http://www.example.org/disease-ontology#>
SELECT DISTINCT ?c
WHERE{
    ?c a :Disease.
    ?d a ?c.
 ?d :hasSymptom :yellowish_skin.
}
```
## R: Alcoholic_hepatitis,Chronic_cholestasis,Hepatitis_B,Hepatitis_C,Hepatitis_D,Hepatitis_E,Jaundice,hepatitis_A
# Que doenças estão associadas ao tratamento "exercise"?
```
PREFIX : <http://www.example.org/disease-ontology#>
SELECT DISTINCT ?c
WHERE{
    ?c a :Disease.
 	?c :hasTreatment :exercise.
}
```
## R: Arthritis,Cervical_spondylosis,Diabetes,GERD,Hypothyroidism,Paralysis_(brain_hemorrhage)

# Produz uma lista ordenada alfabeticamente com o nome dos doentes.
```
PREFIX : <http://www.example.org/disease-ontology#>
SELECT ?n
WHERE{
    ?c a :Patient;
	:name ?n; 
}
ORDER BY ?n
```
## R: Demasiado grande para ser aqui demonstrada

#  Cria uma query CONSTRUCT que diagnostique a doença de cada pessoa, ou seja, produza uma lista de triplos com a forma :patientX :hasDisease :diseaseY. No fim, acrescenta estes triplos à ontologia;
```
PREFIX : <http://www.example.org/disease-ontology#>

CONSTRUCT {
  ?patient :hasDisease ?Maindisease .
}
WHERE {
  ?patient a :Patient .
  ?Maindisease a :Disease .
  ?instance a ?Maindisease.
  ?instance :hasSymptom ?symptomI .
  ?patient :exhibitsSymptom ?symptomP .
    FILTER(?symptomI = ?symptomP)
}
```
## R: para inserir basta trocar o CONSTRUCT por um INSERT

# Cria um query SPARQL que poduza uma distribuição dos doentes pelas doenças, ou seja, dá como resultado uma lista de pares (doença, nº de doentes);
```
PREFIX : <http://www.example.org/disease-ontology#>

SELECT ?disease (COUNT(?patient) AS ?numberOfPatients)
WHERE {
  ?patient :hasDisease ?disease .
}
GROUP BY ?disease
```

# Cria um query SPARQL que poduza uma distribuição das doenças pelos sintomas, ou seja, dá como resultado uma lista de pares (sintoma, nº de doenças com o sintoma)
```
SELECT ?symptom (COUNT(DISTINCT ?disease) AS ?numberOfDiseases)
WHERE {
    ?disease a :Disease.
    ?diseaseI a ?disease
    ?diseaseI :hasSymptom ?symptom .
}
GROUP BY ?symptom
```
#  Cria um query SPARQL que poduza uma distribuição das doenças pelos tratamentos, ou seja, dá como resultado uma lista de pares (tratamento, nº de doenças com o tratamento).

```
SELECT ?treatment (COUNT(DISTINCT ?disease) AS ?numberOfDiseases)
WHERE {
    ?disease a :Disease.
    ?disease :hasTreatment ?symptom .
}
GROUP BY ?treatment
```