# 1. Quantas classes estão definidas na Ontologia?
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT (COUNT(DISTINCT ?class) AS ?numClasses)
WHERE {
  ?class rdf:type owl:Class .
}
```
# 2. Quantas Object Properties estão definidas na Ontologia?
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT (COUNT(DISTINCT ?property) AS ?numObjectProperties)
WHERE {
  ?property rdf:type owl:ObjectProperty .
}
```
# 3. Quantos indivíduos existem na tua ontologia?
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT (COUNT(DISTINCT ?individual) AS ?numIndividuals)
WHERE {
  ?individual rdf:type owl:NamedIndividual .
}
```

# 4. Quem planta tomates?
PREFIX ex: <http://example.org/ontology#>
```
SELECT ?who
WHERE {
  ?who :proprietario/ex:cultiva ex:Tomates .
}
```
# 5. Quem contrata trabalhadores temporários?
```
PREFIX ex: <http://example.org/ontology#>

SELECT ?who
WHERE {
    ?a a :TrabalhadorTemporario.
    ?who ex:contrata ?a.
}
```