# Prometheus Application

Esta aplicação configura o Prometheus no cluster Kubernetes através do ArgoCD.

## Configuração

- **Nome**: prometheus
- **Namespace**: tools
- **Imagem**: prom/prometheus:latest
- **Porta**: 9090

## Acesso

- **URL**: http://prometheus.shareit.com

## Recursos

- **Deployment**: 1 réplica do Prometheus
- **Service**: ClusterIP na porta 80 (redireciona para 9090)
- **Ingress**: Traefik com host prometheus.shareit.com

## Customização

Para customizar a aplicação, edite os arquivos YAML conforme necessário.
