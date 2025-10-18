#!/usr/bin/env python3
import os
import yaml
import requests


ARGOCD_TOKEN = os.getenv("ARGOCD_TOKEN")
ARGOCD_SERVER = os.getenv("ARGOCD_SERVER")

orgs_path = "./orgs"
orgs = [d for d in os.listdir(orgs_path) if os.path.isdir(os.path.join(orgs_path, d))]



def get_apps():
    apps = []
    for org in orgs:
        org_path = os.path.join(orgs_path, org)
        for app in os.listdir(org_path):
            app_path = os.path.join(org_path, app)
            if os.path.isdir(app_path):
                app_yaml = os.path.join(app_path, "app.yaml")
                if os.path.isfile(app_yaml):
                    apps.append(app_yaml)
    return apps


def install_app(app_path):

    """
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
        name: grafana
        namespace: argocd
    spec:
        project: default
        source:
            repoURL: https://github.com/shareit-solutions/observability
            targetRevision: main
            path: .
        destination:
            server: https://kubernetes.default.svc
            namespace: grafana
    """

    # get data from app.yaml    
    with open(app_path, 'r') as f:
        app_data = yaml.safe_load(f)
        app_name = app_data['metadata']['name']
        repo_url = app_data['spec']['source']['repoURL']
        target_revision = app_data['spec']['source']['targetRevision']
        path = app_data['spec']['source']['path']
        dest_server = app_data['spec']['destination']['server']
        dest_namespace = app_data['spec']['destination']['namespace']
    payload = {
        "apiVersion": "argoproj.io/v1alpha1",
        "kind": "Application",
        "metadata": {
            "name": app_name,
            "namespace": "argocd"
        },
        "spec": {
            "project": "default",
            "source": {
                "repoURL": repo_url,
                "targetRevision": target_revision,
                "path": path
            },
            "destination": {
                "server": dest_server,
                "namespace": dest_namespace
            }
        }
    }
    response = requests.post(f"https://{ARGOCD_SERVER}/api/v1/applications", json=payload, headers={"Authorization": f"Bearer {ARGOCD_TOKEN}"}, verify=False)
    if response.status_code == 200:
        print(f"Successfully installed {app_name}")
    else:
        print(f"Failed to install {app_name}: {response.content}")


# iterate over all apps and print their paths
if __name__ == "__main__":
    apps = get_apps()
    for app in apps:
        install_app(app)
        