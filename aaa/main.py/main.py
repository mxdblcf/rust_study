from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod
from diagrams.k8s.infra import Kubelet
from diagrams.k8s.network import Service
from diagrams.k8s.rbac import RoleBinding
from diagrams.k8s.storage import PV
from diagrams.k8s.group import Namespace
from diagrams.k8s import ETCD, API, Controller, Scheduler
from diagrams.onprem.client import User
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github

with Diagram("K8s Create Pod", show=False, direction="TB"):
    user = User("User")
    jenkins = Jenkins("Jenkins CI")
    github = Github("Github")
    with Cluster("Kubernetes Cluster"):
        namespace = Namespace("Namespace")
        api = API("API Server")
        etcd = ETCD("ETCD")
        scheduler = Scheduler("Scheduler")
        controller = Controller("Replication Controller")
        with Cluster("Node"):
            kubelet = Kubelet("Kubelet")
            with Cluster("Pod"):
                pod = Pod("Pod")
                with Cluster("Container"):
                    container = Service("Container")

    user >> jenkins >> github
    github >> jenkins >> namespace >> api >> etcd
    api >> scheduler
    api >> controller
    scheduler >> kubelet
    controller >> kubelet
    kubelet >> pod
    pod >> container
    container >> PV("PV")
    namespace >> RoleBinding("Role Binding")