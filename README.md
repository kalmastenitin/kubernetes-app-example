# kubernetes-app-example
It's an example setup of kubernetes dev environment using skaffold

Multiple services are in communication with each other. Backend is in python fastapi
Mysql docker image with secrets and PersistantVolumeClaim
Nginx static file server which acts as static server for uploaded file serving service.

#Requirement:
  kubernetes
  minikube
  skaffold
  nginx-ingress-controller
  fastapi
  mysql
  nginx
