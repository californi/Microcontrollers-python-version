from kubernetes import client, config
   
def create_deployment_object(deployment_name, deployment_image, deployment_replicas):
    # Configureate Pod template container
    container = client.V1Container(
        name = deployment_name,
        image= deployment_image,
        #ports=[client.V1ContainerPort(container_port=80)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "200Mi"},
            limits={"cpu": "500m", "memory": "500Mi"}
        )
    )
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": deployment_name }),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=deployment_replicas,
        template=template,
        selector={'matchLabels': {'app': deployment_name}})
    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=deployment_name),
        spec=spec)

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment, deployment_name, new_image):
    # Update container image
    deployment.spec.template.spec.containers[0].image = new_image
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=deployment_name,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def delete_deployment(api_instance, deployment_name):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=deployment_name,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


# Create an instance of the API class
config.load_kube_config()
apps_v1 = client.AppsV1Api()




# Getting the deployment
deployment_name = "kube-znn"
deployment_image = "cmendes/znn:100k"
deployment_replicas = 2

current_deployment = apps_v1.read_namespaced_deployment("kube-znn", "default")
#current_deployment.spec.replicas = 0
#update_deployment(apps_v1, current_deployment, deployment_name, deployment_image)
#current_deployment.spec.replicas = deployment_replicas
update_deployment(apps_v1, current_deployment, deployment_name, deployment_image)


#delete_deployment(apps_v1, deployment_name)


#deployament = create_deployment_object(deployment_name, deployment_image, deployment_replicas)
#create_deployment(apps_v1, deployament)

#delete_deployment(apps_v1, deployment_name)


#deployment_name = "kube-znn"
#deployment_image = "cmendes/kube-znn:text"
#deployment_replicas = 2
#deployment = create_deployment_object(deployment_name, deployment_image, deployment_replicas)
#create_deployment(apps_v1, deployment)

#print("finished!")

#current_deployment = apps_v1.read_namespaced_deployment("kube-znn", "default")
#current_deployment.spec.template.spec.containers[0].image = "cmendes/kube-znn:text"
#created_object = create_deployment_object(current_deployment)
#delete_deployment(apps_v1, current_deployment)
#create_deployment(apps_v1, created_object)



#print(deployment.metadata.name)
#print(deployment.spec.template.spec.containers[0].image)
#print(deployment.spec.replicas)
#print(deployment)

# Rollout
#deployment.spec.replicas = 0
#update_deployment(apps_v1, deployment)
#deployment.spec.template.spec.containers[0].image = "cmendes/kube-znn:text"
#deployment.spec.replicas = 2
#update_deployment(apps_v1, deployment)

# Scale
#deployment.spec.replicas = 2
#update_deployment(apps_v1, deployment)
