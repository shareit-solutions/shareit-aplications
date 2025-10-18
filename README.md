# ShareIt Applications

Este repositório gerencia as aplicações que são configuradas no ArgoCD para diferentes organizações.

## Estrutura

```
orgs/
├── shareit/
│   └── grafana/
│       ├── app.yaml
│       └── README.md
```

## Como Funciona

1. Cada organização tem seu próprio diretório dentro de `orgs/`
2. Cada aplicação dentro da organização tem seu próprio diretório
3. Cada aplicação contém um arquivo `app.yaml` com a configuração do ArgoCD
4. O GitHub Actions automaticamente detecta mudanças e cria/atualiza as aplicações no ArgoCD

## Configuração do GitHub Actions

Para que o CI funcione, você precisa configurar os seguintes secrets no GitHub:

- `ARGOCD_SERVER`: URL do servidor ArgoCD (ex: `argocd.example.com`)
- `ARGOCD_AUTH_TOKEN`: Token de autenticação do ArgoCD

### Como gerar o token do ArgoCD

```bash
# Login no ArgoCD
argocd login <ARGOCD_SERVER>

# Gerar token
argocd account generate-token
```

## Adicionando uma Nova Aplicação

1. Crie um novo diretório dentro de `orgs/<organization>/`
2. Adicione um arquivo `app.yaml` com a configuração do ArgoCD
3. (Opcional) Adicione um `README.md` com documentação da aplicação
4. Commit e push - o GitHub Actions irá criar a aplicação automaticamente

## Exemplo de app.yaml

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/helm-charts
    targetRevision: 1.0.0
    chart: my-app
  destination:
    server: https://kubernetes.default.svc
    namespace: my-app
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

## Organizações

- **shareit**: Aplicações da organização ShareIt
  - grafana: Sistema de monitoramento e dashboards
