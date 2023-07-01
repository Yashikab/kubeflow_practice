# ローカルへのKubeflowのインストール

## 概要

kubeflowはkubernetes上で動くため、ローカルにkindやminikubeをつかってkubernetes clusterを構築し、その上にデプロイする。

## Kubernetes環境の構築

### kindのインストール

```shell
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
kind --version  # 確認用
```

### kubeflowのデプロイ

- clusterをkindを使って作成する

    ```shell
    kind create cluster
    ```

- kubeflowのデプロイ

    ```shell
    export PIPELINE_VERSION=2.0.0
    sudo kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
    sudo kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
    sudo kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
    sudo kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
    ```

## 参考

- [公式手順](https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/)
