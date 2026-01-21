
# 🌦️ Tactical Weather Intelligence Project

A microservices-based application built with **FastAPI** designed to ingest, process, and store weather data. The project is containerized and deployed on an **OpenShift/Kubernetes** cluster.

## 🏗️ System Architecture

The application follows a linear pipeline architecture:

1. **Service A (Ingest):** Receives external API requests and forwards raw data to Service B.
2. **Service B (Clean):** Processes and cleans the incoming data, then forwards it to Service C.
3. **Service C (Storage):** Receives the refined data and persists it into the MySQL database.
4. **MySQL (StatefulSet):** A reliable database layer with persistent storage (PVC).

---

## 🚀 Deployment Instructions

### 1. Database Layer

Deploy the MySQL StatefulSet and its Headless Service first to ensure the backend storage is ready:

**Bash**

```
oc apply -f k8s/mysql-statefulset.yaml
oc apply -f k8s/mysql-service.yaml
```

### 2. Application Layer

Deploy the three core services. Ensure the images are pushed to your registry before applying:

**Bash**

```
oc apply -f k8s/service-a-deploy.yaml
oc apply -f k8s/service-b-deploy.yaml
oc apply -f k8s/service-c-deploy.yaml
```

### 3. External Access

Expose Service A to create a Route for external traffic:

**Bash**

```
oc expose svc svc-service-a
oc get routes
```

---

## ⚙️ Configuration (Environment Variables)

The services communicate using internal DNS names defined in the Deployment manifests. Ensure the following environment variables are set correctly:

| **Service**   | **Environment Variable** | **Value**        | **Description**     |
| ------------------- | ------------------------------ | ---------------------- | ------------------------- |
| **Service A** | `SERVIS_B_HOST`              | `svc-service-b`      | Internal DNS of Service B |
| **Service B** | `SERVIS_C_HOST`              | `svc-service-c`      | Internal DNS of Service C |
| **Service C** | `DB_HOST`                    | `headless-svc-mysql` | Internal DNS of MySQL     |
| **Service C** | `DB_PASSWORD`                | `password`           | MySQL Root Password       |
| **Service C** | `DB_NAME`                    | `weather_db`         | Target Database Name      |

---

## 🛠️ Verification

To verify the deployment, you can send a POST request to the Service A Route:

**Bash**

```
curl -X POST "http://<your-route-url>/ingest?location=London"
```
