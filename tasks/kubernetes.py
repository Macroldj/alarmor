from kubernetes import client, config
config.kube_config.load_kube_config(config_file="kubeconfig.yaml")


def k8s_tasks():
    pass