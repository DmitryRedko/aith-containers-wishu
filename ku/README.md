kubectl delete pods,pvc,pc --all
kubectl delete pods --all



docker build -t wishu .

minikube image load wishu


Поднять манифесты:

kubectl apply -f pg_configmap.yml
kubectl apply -f server_configmap.yml
kubectl apply -f pg_secret.yml
kubectl apply -f server_secret.yml

kubectl apply -f pg_volume.yml
kubectl apply -f pg_volume_claim.yml
kubectl apply -f server_volume_claim.yml

kubectl apply -f pg_service.yml
kubectl apply -f server_service.yml

kubectl apply -f pg_deployment.yml
kubectl apply -f server_deployment.yml


kubectl port-forward wishu-server-5df57c5869-4l4bm  8000:8000
kubectl port-forward service/wishu-server 8000:8000

