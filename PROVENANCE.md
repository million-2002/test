# PROVENANCE.md

## 1. 文档说明
记录推荐模型 `model_v2` 从数据采集到训练部署的全链路溯源信息，确保每个环节可追溯、可验证。

## 2. 核心溯源链路
```mermaid
graph TD
    A[原始数据] --> B[数据清洗]
    B --> C[模型训练(v2)]
    C --> D[MLflow记录]
    
    A["文件: training_data.csv<br>路径: data/training_data.csv<br>样本量: 1万条"]
    B["操作: 去重32条、删空行5条<br>脚本: ml/data_pipeline.py"]
    C["超参: learning_rate=0.001<br>脚本: ml/train.py<br>环境: 本地CPU(8核)"]
    D["Run ID: [从DagsHub获取]<br>地址: https://dagshub.com/million-2002/test.mlflow<br>指标: accuracy=0.92"]
