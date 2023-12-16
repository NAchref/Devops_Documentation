#
# DevOps Interview Questions

## Question 1:
### Docker vs Vagrant

```
Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation
Docker Containers are generally more lightweight than virtual machines, so starting and stopping containers is extremely fast. 
Both Vagrant and Docker have a vast library of community-contributed "images" or "boxes" to choose from.
```


## Question 2:
### What is SAAS, PAAS & IAAS stand for?
```
SAAS: Software as a Service, also known as cloud application services, SaaS utilizes the internet to deliver applications, which are managed by a third-party vendor, to its users. A majority of SaaS applications run directly through your web browser, which means they do not require any downloads or installations on the client side.

PAAS: Cloud platform services, also known as Platform as a Service, PaaS delivers a framework for developers that they can build upon and use to create customized applications. All servers, storage, and networking can be managed by the enterprise or a third-party provider while the developers can maintain management of the applications.

IAAS: Cloud infrastructure services, known as Infrastructure as a Service, Cloud infrastructure services, known as Infrastructure as a Service
```

## Question 3:
### What is VPC?
```
VPC is Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
```

## Question 4:
### What is IAC?
```
IAC is Infrastructure as Code which is managing and provisioning of infrastructure through code instead of through manual processes.
```

## Question 5:
### What is Cloud Formation?
```
AWS CloudFormation is a service that gives developers and businesses an easy way to create a collection of related AWS and third-party resources, and provision and manage them in an orderly and predictable fashion.
```

## Question 6: (Kubernetes)
### What is Kubernetes and how does it work?
```
Kubernetes is an open-source platform that automates the deployment, scaling, and management of containerized applications. It works by creating a cluster of worker nodes that can run containerized applications, and managing those nodes and applications through a central control plane.

```

## Question 7:
### Can you explain the difference between a pod and a deployment in Kubernetes?
```
A pod is the smallest deployable unit in Kubernetes, consisting of one or more containers that share the same network and storage resources. A deployment is a higher-level abstraction that manages a set of replica pods, ensuring that the desired number of replicas are running and that they are updated and rolled out gracefully.

```

## Question 8:
### How do you scale a deployment in Kubernetes?
```
You can scale a deployment in Kubernetes by updating its replica count using the kubectl scale command or by modifying its YAML configuration file and applying the changes using kubectl apply.

```

## Question 9:
### How do you monitor and troubleshoot a Kubernetes cluster?
```
You can monitor and troubleshoot a Kubernetes cluster using various tools and techniques, including logging and metrics collection, tracing, and debugging. Common tools for monitoring and troubleshooting Kubernetes include Prometheus, Grafana, Jaeger, and kubectl commands like kubectl logs and kubectl exec.

```

## Question 10:
### How do you deploy a containerized application to Kubernetes?
```
To deploy a containerized application to Kubernetes, you need to create a Kubernetes deployment or a pod YAML configuration file that describes the application's container image, resource requirements, and other settings. You can then apply the configuration using kubectl apply or create commands.

```

## Question 11:
### What are the different types of Kubernetes volumes and when would you use each type?

```
There are several types of Kubernetes volumes, including hostPath, emptyDir, configMap, secret, persistentVolumeClaim, and more. Each type is designed to support different use cases and storage requirements, such as temporary storage, shared configuration, or persistent data storage.
```

## Question 12:
### Can you explain the concept of a Kubernetes namespace?
```
A namespace is a way to partition a Kubernetes cluster into multiple virtual clusters. It provides a way to group related objects together and to provide isolation between different parts of your application. You can use namespaces to limit resource usage, provide access control, and simplify management of your Kubernetes cluster.
```

## Question 13:
### How do you perform a rolling update of a Kubernetes deployment?

```
You can perform a rolling update of a Kubernetes deployment by updating the deployment manifest file with the new container image or configuration options and then using kubectl apply to apply the changes. Kubernetes will automatically roll out the update to the pods in the deployment, one at a time, while keeping the application available to users.
```