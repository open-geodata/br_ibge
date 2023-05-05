# BR > IBGE

O [**GeoFTP do IBGE**](http://geoftp.ibge.gov.br/) é o servidor do [**Instituto Brasileiro de Geografia e Estatistica (IBGE)**](https://www.infraestruturameioambiente.sp.gov.br) que disponibiliza diversas informações relevantes, majoritariamente em formato _shapefile_, ou seja, em formato editável, sendo que os dados armazenados nesse repositório são derivados destes.

---

<br>

## Objetivo do repositório

Este repositório tem a finalidade de disponibilizar as rotinas empregadas para fazer o _download_ e tratamento dos dados, bem como disponibilizar os dados de maneira remota, sendo facilmente utilizado em outras aplicações.

- **_Download_**: tentativa de busca dos dados por meio do _link_ dos metadados;
- **_Tratamento dos Atributos_**: deletar colunas desnecessárias, renomear colunas etc;
- **_Transformação de Projeção_**: buscar padronizar a base de dados em EPSG: 4326, tento em vista ser o mais empregado em _webmaps_;
- **_Excluir Lixos_**: deletar arquivos intermediários, mantendo apenas o arquivo bruto e a versão que utilizo em outros códigos.
