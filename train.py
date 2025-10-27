import mlflow
import argparse  # 用于接收版本参数

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", type=str, required=True, help="版本名称（如 v1、v2）")
    args = parser.parse_args()

    # 设置 MLflow 跟踪地址
    mlflow.set_tracking_uri("https://dagshub.com/million-2002/test.mlflow")
    
    # 启动运行时指定版本名称（run_name）
    with mlflow.start_run(run_name=f"model_{args.version}"):
        # 版本1和版本2的差异参数
        if args.version == "v1":
            mlflow.log_param("learning_rate", 0.01)
            mlflow.log_metric("accuracy", 0.85)
        elif args.version == "v2":
            mlflow.log_param("learning_rate", 0.001)  # 调整学习率
            mlflow.log_metric("accuracy", 0.92)       # 精度提升
        print(f"版本 {args.version} 运行完成，已同步到 DagsHub")

if __name__ == "__main__":
    main()
