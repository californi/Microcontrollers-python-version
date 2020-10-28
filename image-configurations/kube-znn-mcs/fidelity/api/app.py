from fastapi import FastAPI, Request, Response
import httpx
#from pydantic import BaseModel
import asyncio

#class Message(BaseModel):
#    id: int
#    message: str


from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
#config.load_incluster_config()

#v1 = client.CoreV1Api()
#vStr = "Listing pods with their IPs:"
#ret = v1.list_pod_for_all_namespaces(watch=False)
#for i in ret.items:
#    vStr = vStr + " Other " + i.status.pod_ip + " - " + i.metadata.namespace + " - " + i.metadata.name



app = FastAPI()

#url_host = 'http://<service-name>:<port>'
#url_host = 'http://analyser:5001'
#microcontrollers Base64    bWljcm9jb250cm9sbGVycw==
headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format('bWljcm9jb250cm9sbGVycw==')}

@app.post("/decreaseFidelity/")
def decreaseFidelity():

    # decreaseFidelity

    # updating the Knowledge

    return "empty"

@app.post("/increaseFidelity/")
def increaseFidelity():

    # increaseFidelity

    # updating the Knowledge

    return "empty"




DEPLOYMENT_NAME = "nginx-deployment"


def create_deployment_object():
    # Configureate Pod template container
    container = client.V1Container(
        name="nginx",
        image="nginx:1.15.4",
        ports=[client.V1ContainerPort(container_port=80)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "200Mi"},
            limits={"cpu": "500m", "memory": "500Mi"}
        )
    )
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=3,
        template=template,
        selector={'matchLabels': {'app': 'nginx'}})
    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec)

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    deployment.spec.template.spec.containers[0].image = "nginx:1.16.0"
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def delete_deployment(api_instance):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_incluster_config()
    apps_v1 = client.AppsV1Api()

    # Uncomment the following lines to enable debug logging
    # c = client.Configuration()
    # c.debug = True
    # apps_v1 = client.AppsV1Api(api_client=client.ApiClient(configuration=c))

    # Create a deployment object with client-python API. The deployment we
    # created is same as the `nginx-deployment.yaml` in the /examples folder.
    deployment = create_deployment_object()

    create_deployment(apps_v1, deployment)

    #update_deployment(apps_v1, deployment)

    #delete_deployment(apps_v1)

main()