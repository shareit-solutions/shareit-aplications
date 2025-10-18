# Grafana Application

Esta aplicação configura o Grafana no cluster Kubernetes através do ArgoCD.

## Configuração

- **Nome**: grafana
- **Namespace**: grafana
- **Chart**: grafana/grafana (Helm)
- **Versão**: 7.3.7

## Características

- Sincronização automática habilitada
- Self-healing habilitado
- Criação automática de namespace
- Persistência de dados habilitada (10Gi)

## Credenciais Padrão

- **Usuário**: admin
- **Senha**: admin (deve ser alterada após o primeiro login)

## Customização

Para customizar a aplicação, edite o arquivo `app.yaml` e ajuste os valores do Helm conforme necessário.
