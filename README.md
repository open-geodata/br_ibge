# BR > IBGE



O [**GeoFTP do IBGE**](http://geoftp.ibge.gov.br/) é o servidor do [**Instituto Brasileiro de Geografia e Estatistica (IBGE)**](https://www.infraestruturameioambiente.sp.gov.br) que disponibiliza diversas informações relevantes, majoritariamente em formato *shapefile*, ou seja, em formato editável, sendo que os dados armazenados nesse repositório são derivados destes.



## Objetivo do repositório

Este repositório tem a finalidade de disponibilizar as rotinas empregadas para fazer o *download* e tratamento dos dados, bem como disponibilizar os dados de maneira remota, sendo facilmente utilizado em outras aplicações.


- ***Download***: tentativa de busca dos dados por meio do *link* dos metadados;

- ***Tratamento dos Atributos***: deletar colunas desnecessárias, renomear colunas etc;

- ***Transformação de Projeção***: buscar padronizar a base de dados em EPSG: 4326, tento em vista ser o mais empregado em *webmaps*;

- ***Excluir Lixos***: deletar arquivos intermediários, mantendo apenas o arquivo bruto e a versão que utilizo em outros códigos.

