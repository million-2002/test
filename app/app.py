from collections import defaultdict
from typing import List
import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

def dedupe_header(columns: List[str]) -> List[str]:
    seen_counts = defaultdict(int)
    result = []
    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1
    return result

def save_to_database(columns: List[str]):
    db_password = os.getenv("DB_PASSWORD")
    if not db_password:
        raise ValueError("数据库密码未配置，请检查.env或环境变量")
    print(f"使用密码 {db_password} 连接数据库，写入列名：{columns}")

if __name__ == "__main__":
    test_input = ["id", "name", "id", "name", "name"]
    deduped = dedupe_header(test_input)
    print("去重后列名：", deduped)
    # save_to_database(deduped)
