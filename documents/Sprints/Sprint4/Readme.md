## Sprint - 4️⃣ 🎯
Nesta Sprint refinamos o código do site, corrigimos problemas de bugs, tornamos o sistema responsivo e o subimos para um serviço de hospedagem web (AWS) em conjunto com o Docker, possibilitando o acesso do Data-SARS de qualquer máquina ou dispositivo. 

## Como Subimos a apliacação Web:
 - primeiramente criamos uma instância ubuntu no serviço da AWS
 - configuramos as regras de host 
 - criamos uma docker file para a aplicação
 - buildamos uma imagem da aplicação
 - subimos ambos para o servidor

> A aplicação não possuí um domínio, portanto é preciso acessa-la pelo ip: [3.209.143.219:5000]();
> para acessar é preciso que a intância esteja ativa, então é só digitar o ip no navegador de sua preferência.
<hr>

## Backlog da Sprint
<hr>

| Item | Prioridade|ID                                                                                                                                                                                                                               | Descrição | 
|:-------:|:--------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------:|
| Formatação do Site e Estilização                         |  Médio                | #11 | Refinamento de código e adição de recursos responsivos |
| Testes                                                   |  Médio                | #12 | Teste da aplicação cpm intuito de encontrar e corrigir erros e bugs |
| README                                                   |  Baixa                | #13 | Documentação do projeto |

### User Story's 📝

| ID US | Sprint | US                                                                                                                                                                                                                                           | ID Requisito          |
|:-------:|:--------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------:|
| US01  | 4      | "Eu, como desenvolvedor, desejo refinar o CSS do Data SARS, com o intuito de embelezar o sistema e adicionar funcionalidades extras que garantam uma boa expeiência de usuário"                                                                                                      |  #11                  |
| US02  | 4      | "Eu, como desenvolvedor, quero adicionar textos explicativos sobre o projeto à página Home."                                                                                                             |  #11                  |
| US03  | 4      | "Eu, como desenvolvedor, quero adicionar textos explicativos sobre o grupo e realização do projeto à página Quem Somos."                                                                                           |  #11                  |
| US04  | 4      | "Eu, como desenvolvedor, quero corrigir os erros e bugs encontrados."                                                                                                             |  #11                  |
| US05  | 4      | "Eu, como desenvolvedor, quero testar a aplicação, no intuito de encontrar e corrigir possíveis bugs e erros."                                                                                                                  |  #12                  |
| US06  | 4      | "Eu, como desenvolvedor, quero disponibilizar um arquivo README que instrua o usuário sobre como utilizar o sistema e informe sobre os porcessos por trás da aplicação."                                            |  #13                  |


