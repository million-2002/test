import os
import sys
import pytest
from dotenv import load_dotenv  # 用于测试时临时加载环境变量

# 配置项目路径（确保能导入 app.app）
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file))
sys.path.append(project_root)

from app.app import dedupe_header, save_to_database


# -------------------------- 测试 dedupe_header 函数 --------------------------
def test_dedupe_header_no_duplicates():
    """测试无重复列名的情况"""
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]


def test_dedupe_header_all_duplicates():
    """测试所有列名均重复的情况"""
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]


def test_dedupe_header_mixed_duplicates():
    """测试混合重复的列名（核心示例）"""
    input_cols = ["id", "name", "id", "name", "name"]
    expected_cols = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(input_cols) == expected_cols


def test_dedupe_header_empty_input():
    """测试空列表输入"""
    assert dedupe_header([]) == []


def test_dedupe_header_special_characters():
    """测试含特殊字符的列名（空格、标点等）"""
    input_cols = ["user@name", "user@name", "age!"]
    expected_cols = ["user@name", "user@name.1", "age!"]
    assert dedupe_header(input_cols) == expected_cols


# -------------------------- 测试 save_to_database 函数 --------------------------
def test_save_to_database_with_valid_password(monkeypatch):
    """测试环境变量中存在 DB_PASSWORD 时，函数正常执行"""
    # 用 monkeypatch 临时设置环境变量（模拟 .env 或系统变量）
    monkeypatch.setenv("DB_PASSWORD", "test_password_123")
    
    # 调用函数（应正常执行，无异常）
    columns = ["id", "name"]
    save_to_database(columns)  # 若未抛出异常，说明通过


def test_save_to_database_without_password(monkeypatch):
    """测试环境变量中无 DB_PASSWORD 时，函数抛出 ValueError"""
    # 确保环境变量中没有 DB_PASSWORD（删除可能存在的变量）
    monkeypatch.delenv("DB_PASSWORD", raising=False)
    
    # 调用函数，预期会抛出 ValueError
    columns = ["id", "name"]
    with pytest.raises(ValueError) as exc_info:
        save_to_database(columns)
    
    # 验证异常信息是否正确
    assert "数据库密码未配置，请检查.env或环境变量" in str(exc_info.value)


def test_save_to_database_with_empty_password(monkeypatch):
    """测试环境变量中 DB_PASSWORD 为空字符串时，函数抛出 ValueError"""
    # 设置空密码
    monkeypatch.setenv("DB_PASSWORD", "")
    
    # 调用函数，预期抛出异常
    columns = ["id", "name"]
    with pytest.raises(ValueError):
        save_to_database(columns)
