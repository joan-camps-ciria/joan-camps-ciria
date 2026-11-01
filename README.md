<div align="center">

<a href="https://joan-camps-ciria.github.io/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg"><img alt="Joan Camps Ciria, Linux Systems Engineer" src="assets/hero-dark.svg" width="100%"></picture></a>

<a href="https://joan-camps-ciria.github.io/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/boton-portfolio-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/boton-portfolio-light.svg"><img alt="Ver portfolio" src="assets/boton-portfolio-dark.svg" height="44"></picture></a>
<a href="https://www.linkedin.com/in/joan-camps-ciria/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/boton-linkedin-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/boton-linkedin-light.svg"><img alt="LinkedIn" src="assets/boton-linkedin-dark.svg" height="44"></picture></a>

<a href="https://joan-camps-ciria.github.io/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/cifras-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/cifras-light.svg"><img alt="Más de 7 años en producción, RHCSA, IaC con Ansible y AWX, K8s con OpenShift y Docker" src="assets/cifras-dark.svg" width="100%"></picture></a>

</div>

## `01.` kubectl describe joan

```yaml
apiVersion: humano/v1
kind: Ingeniero
metadata:
  name: joan-camps-ciria
  labels:
    modo: aprender-haciendo
spec:
  replicas: 1            # aún no escalo horizontalmente
  rol: Linux Systems Engineer
  enfoque: [Linux, automatización, contenedores]
  aprendiendo: Terraform
  regla: "si no lo he montado yo, no lo he entendido"
status:
  phase: Running
  restarts: "solo con café"
```

## `02.` Laboratorios

Todo montado en local, paso a paso y documentado para que cualquiera pueda repetirlo.

| Lab | De qué va | Stack |
|---|---|---|
| 🚀 [**Kubernetes**](https://github.com/joan-camps-ciria/Proyectos-Laboratorio/tree/master/Kubernetes-Lab) | Clúster local y comandos esenciales | `minikube` `kubectl` `Docker` |
| 🐍 [**API de Python en K8s**](https://github.com/joan-camps-ciria/Proyectos-Laboratorio/tree/master/Python-App-K8s-Lab) | Gestor de tareas en contenedor, con datos persistentes | `FastAPI` `Docker` `Kubernetes` |
| 📊 [**Monitorización**](https://github.com/joan-camps-ciria/Proyectos-Laboratorio/tree/master/Monitoring-K8s-Lab) | Métricas, alertas y paneles con YAML escrito a mano, sin Helm | `Prometheus` `Grafana` `node-exporter` |
| 🤖 [**Ansible**](https://github.com/joan-camps-ciria/Proyectos-Laboratorio/tree/master/Ansible-Docker-Lab) | Tres nginx tras un balanceador, sobre nodos Docker multidistro | `Ansible` `Docker Compose` `nginx` |

## `03.` Ruta de laboratorios

```mermaid
flowchart LR
    A["🚀 Kubernetes"] --> B["🐍 Apps en K8s"]
    B --> C["📊 Monitorización"]
    C --> D["🤖 Ansible"]
    D --> E["🏗️ Terraform"]
    E --> F["🤝 Terraform + Ansible"]

    classDef hecho fill:#0a9b6e,stroke:#3ddc97,color:#ffffff
    classDef siguiente fill:#161b26,stroke:#3ddc97,color:#e6eaf2
    class A,B,C,D hecho
    class E,F siguiente
```

## `04.` Herramientas

![Red Hat](https://img.shields.io/badge/Red%20Hat-161b26?style=flat-square&logo=redhat&logoColor=3ddc97)
![Ansible](https://img.shields.io/badge/Ansible-161b26?style=flat-square&logo=ansible&logoColor=3ddc97)
![Kubernetes](https://img.shields.io/badge/Kubernetes-161b26?style=flat-square&logo=kubernetes&logoColor=3ddc97)
![OpenShift](https://img.shields.io/badge/OpenShift-161b26?style=flat-square&logo=redhatopenshift&logoColor=3ddc97)
![Docker](https://img.shields.io/badge/Docker-161b26?style=flat-square&logo=docker&logoColor=3ddc97)
![Podman](https://img.shields.io/badge/Podman-161b26?style=flat-square&logo=podman&logoColor=3ddc97)
![Prometheus](https://img.shields.io/badge/Prometheus-161b26?style=flat-square&logo=prometheus&logoColor=3ddc97)
![Grafana](https://img.shields.io/badge/Grafana-161b26?style=flat-square&logo=grafana&logoColor=3ddc97)
![Bash](https://img.shields.io/badge/Bash-161b26?style=flat-square&logo=gnubash&logoColor=3ddc97)
![Python](https://img.shields.io/badge/Python-161b26?style=flat-square&logo=python&logoColor=3ddc97)
![Git](https://img.shields.io/badge/Git-161b26?style=flat-square&logo=git&logoColor=3ddc97)
