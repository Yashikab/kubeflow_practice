# ローカルへのKubeflowのインストール

## 概要

kubeflowはkubernetes上で動くため、ローカルにkindやminikubeをつかってkubernetes clusterを構築し、その上にデプロイする。

## Virtual Machineの構築

ローカルPC環境は汚したくないため、virtual machineを構築し軽量なlubuntu22.04を入れる。

1. [Oracle VM VirtualBoxのパッケージ](https://www.oracle.com/jp/virtualization/technologies/vm/downloads/virtualbox-downloads.html)を取得する
2. 取得したパッケージで virtual boxをインストールする
3. [lubuntu22.04のisoイメージ](https://lubuntu.me/downloads/)をDLする

## Kubernetes環境の構築

## 参考

- [公式手順](https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/)
