from kubernetes import client, config

def update_deployment(api_instance, deployment):
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name = deployment.metadata.name,
        namespace = deployment.metadata.namespace,
        body = deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))

# Create an instance of the API class
config.load_kube_config()
apps_v1 = client.AppsV1Api()

# Getting the deployment
deployment = apps_v1.read_namespaced_deployment("scalability", "default")
print(deployment.metadata.name)
print(deployment.spec.template.spec.containers[0].image)
print(deployment.spec.replicas)
#print(deployment)

deployment.spec.template.spec.containers[0].image = "californibrs/kubeznn-scalability"
deployment.spec.replicas = 2
update_deployment(apps_v1, deployment)
