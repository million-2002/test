# README_experiments.md

## 一、实验目标
优化 [目标任务，如“用户转化预测”] 模型准确率，验证学习率对模型性能的影响。


## 二、实验版本对比（MLflow 跟踪）
| 实验版本（Run 名称） | 核心超参数          | 测试集准确率 | 状态   |
|----------------------|---------------------|--------------|--------|
| `model_v1`           | `learning_rate=0.01` | 0.85         | 已完成 |
| `model_v2`           | `learning_rate=0.001`| 0.92         | 已完成 |

### 关键结论
1. 降低学习率（0.01→0.001）使准确率提升 7%，`v2` 泛化能力更优；
2. `v2` 训练稳定性更好（需补充损失日志验证）。


## 三、推荐模型与复现
### 1. 推荐版本
`model_v2`（准确率更高，适合生产试用）

### 2. 复现步骤
```bash
# 安装依赖
pip install mlflow argparse

# 复现 v1 实验
python ml/train.py --version v1

# 复现 v2 实验
python ml/train.py --version v2

# 查看实验结果（DagsHub MLflow 地址）
# https://dagshub.com/million-2002/test.mlflow
