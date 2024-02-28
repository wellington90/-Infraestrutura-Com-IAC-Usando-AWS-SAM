## Resumo do Projeto - Sistema CRUD com AWS SAM, DynamoDB, API Gateway e Lambda Python:

1. **Descrição do Projeto:**
    - O projeto consiste em criar um sistema CRUD (Create, Read, Update, Delete) usando AWS SAM (Serverless Application Model), AWS DynamoDB como banco de dados, AWS Lambda para funções serverless e API Gateway para expor endpoints RESTful.

2. **Tecnologias Utilizadas:**
    - AWS SAM: Para facilitar a criação e implantação de aplicativos serverless.
    - AWS DynamoDB: Um serviço de banco de dados NoSQL totalmente gerenciado pela AWS.
    - AWS Lambda: Para executar código sem a necessidade de provisionar ou gerenciar servidores.
    - API Gateway: Para criar, publicar, manter, monitorar e proteger APIs RESTful.

3. **Estrutura do Projeto:**
    - Arquivo `template.yaml`: Define a infraestrutura como código (IaC) usando a AWS SAM para criar recursos como funções Lambda, tabela DynamoDB e integrações com a API Gateway.
    - Funções Lambda Python: Cada função (Create, Get, List) contém código Python que é executado quando acionado por eventos da API Gateway.

4. **Funcionalidades:**
    - **Create Function**: Recebe solicitações POST para criar novos itens na tabela DynamoDB.
    - **Get Function**: Recebe solicitações GET com um ID como parâmetro de rota para recuperar um item específico da tabela DynamoDB.
    - **List Function**: Recebe solicitações GET para listar todos os itens na tabela DynamoDB.

5. **Integração com DynamoDB:**
    - As funções Lambda têm permissões (políticas) que concedem acesso total à tabela DynamoDB, permitindo operações CRUD.

6. **Interoperabilidade e Escalabilidade:**
    - A infraestrutura é projetada para ser altamente escalável e resiliente, com integração direta com os serviços gerenciados da AWS.

7. **Documentação:**
    - O arquivo `template.yaml` é documentado com comentários que explicam cada seção do código, facilitando o entendimento e manutenção do projeto.

Esse é um resumo geral do projeto que utiliza AWS SAM, DynamoDB, API Gateway e Lambda Python para criar um sistema CRUD serverless na AWS. O uso de infraestrutura como código (IaC) simplifica a implantação e gerenciamento dos recursos na nuvem.



# ferramenta para testes Postaman

```bash
{
    "name": "Nome do item"
}
```

# Criar roles Dynamodb segmentadas




