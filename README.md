# Flask-App-Deployment-with-mysql-phpAdmin

## Overview
This project demonstrates the deployment of a **Flask application** integrated with **MySQL** and managed using **phpMyAdmin**. The deployment is achieved using Kubernetes, with configurations for services, persistent volumes, and environment variables.

---

## Features

1. **Flask Application**:
   - Serves as the main API backend.
   - Connects to a MySQL database to manage application data.

2. **MySQL Database**:
   - Stores application data with persistent volume support for durability.

3. **phpMyAdmin**:
   - Provides a graphical interface to manage the MySQL database.

4. **Kubernetes Deployment**:
   - Fully containerized services managed via Kubernetes configurations.

---

## Prerequisites

- Kubernetes cluster (Minikube or other providers).
- kubectl CLI tool installed and configured.
- Docker for containerization.
- NodePort access for external services.

---

## Deployment Steps

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/Flask-App-Deployment-with-mysql-phpAdmin.git
cd Flask-App-Deployment-with-mysql-phpAdmin
```
### **2. Set Up MySQL**
1. Apply the mysql-config.yaml file to create the necessary ConfigMap:
```bash
kubectl apply -f mysql-config.yaml
```
2. Deploy the MySQL service and PersistentVolume:
```bash
kubectl apply -f mysql-deployment.yaml
```
### **3. Deploy Flask Application**
1. Build and push the Flask Docker image (optional for local Minikube):
```bash
docker build -t flask-mysql-app .
```
2. Deploy the Flask app:
```bash
kubectl apply -f flask-deployment.yaml
```
### **4. Set Up phpMyAdmin**
Deploy phpMyAdmin for database management:
```bash
kubectl apply -f phpmyadmin-deployment.yaml
```
## Accessing the Application

1. **Flask Application**:
   - **NodePort**: `30001`
   - Access via browser: `http://<node-ip>:30001`

2. **phpMyAdmin**:
   - **NodePort**: `30000`
   - Access via browser: `http://<node-ip>:30000`

---

## File Structure

- `flask-deployment.yaml`: Deployment and Service for the Flask application.
- `mysql-config.yaml`: ConfigMap for MySQL environment variables.
- `mysql-deployment.yaml`: Deployment, PersistentVolume, and Service for MySQL.
- `phpmyadmin-deployment.yaml`: Deployment and Service for phpMyAdmin.

---

## Environment Variables

### Configured in `mysql-config.yaml`:
```yaml
MYSQL_DATABASE: "admindb"
MYSQL_USER: "adminuser"
MYSQL_PASSWORD: "adminpassword"
```
### Configured in `flask-deployment.yaml`:
- `MYSQL_HOST`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_DATABASE`

---

## Future Enhancements

- Automate CI/CD for building and deploying Docker images.
- Add HTTPS support using Kubernetes Ingress and Let's Encrypt.
- Implement resource quotas and limits for efficient resource usage.
- Scale the application horizontally by increasing replicas.

---

## Acknowledgments

This project was developed to showcase the deployment of a Flask application integrated with MySQL and phpMyAdmin using Kubernetes. Special thanks to the open-source communities for providing the tools and resources.

---

## License

This project is licensed under the [MIT License](LICENSE).

