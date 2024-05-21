# Ex 1
A resposta ao Exercicio um encotra-se disponível na pasta ex1.
A ontologia definida no Protegé encontra-se em [historia.ttl](historia.ttl) e as queries no ficheiro [queries.md](ex1/queries.md)

# Ex 2
De forma a gerar as ontologias é necessário executar ```python3 generate.py``` no diretorio [ex2](ex2).
Visto que existem dependencias encontra-se disponivel um ficheiro ```requirements.txt``` que podem ser instaladas usando ```pip3 install -r requirements.txt```

As Queries requeridas encontram-se no ficheiro [Queries.md](ex2/Queries.md)


Explicação:

Foi inicialmente carregado a ontologia base, de seguida foi procurada nas doenças e os seus sintomas quais as doenças ainda não encontraddas se fossem novas uma nova intancia de Disease era criada. Em simultaneo para cada conjunto novo de sintomas daquela doença era criada uma instancia (com o nome de doença e um identificador unico numerico) cujo tipo era a doença.
Por fim os tratamentos e sintomas foram adicionados a doença acabando por se adicionar também os utilizadores.
