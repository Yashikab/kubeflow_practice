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

### dockerのインストール

#### chrome bookの場合

```shell
sudo apt update
sudo apt install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# これはbashじゃないと実行できない (fishではむり)
bash echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# dockerをnon root userで実行できるようにする
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
# 動作確認
docker run hello-world
```

### kubeflowのデプロイ

#### chromeosの場合

- croshでlxc containerにネスティングを許可する必要がある
- ctl+alt+T でcroshを開く

```shell
crosh> vmc laungh termina
(termina) chronos@localhost ~ $ lxc config set penguin security.nesting true
(termina) chronos@localhost ~ $ lxc restart penguin
```

- cluster.yamlを作る

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
featureGates:
  KubeletInUserNamespace: true
```

- `kind create cluster --config ./cluster.yaml` を実行

#### 普通の場合

- clusterをkindを使って作成する

    ```shell
    kind create cluster
    ```

#### k3sのインストール

- chromeosではserverが立ち上がらない

```shell
curl -sfL https://get.k3s.io | sh -
sudo apt install kmod
sudo k3s server &
```

#### kubeflowのデプロイ

    ```shell
    export PIPELINE_VERSION=2.0.0
    sudo kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
    sudo kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
    sudo kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
    sudo kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
    ```

## 参考

- [公式手順](https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/)
