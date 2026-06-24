# ============================================
# 接口自动化测试 - test_api.py
# 使用 Requests + Pytest 框架
# ============================================

import requests
import pytest

# ---------- 基础配置 ----------
BASE_URL = "https://jsonplaceholder.typicode.com"


class TestUserAPI:
    """用户模块接口测试"""

    def test_get_users_status_code(self):
        """GET /users - 验证状态码200"""
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200
        print(f"✅ 状态码: {response.status_code}")

    def test_get_users_response_body(self):
        """GET /users - 验证返回数据不为空"""
        response = requests.get(f"{BASE_URL}/users")
        data = response.json()
        assert len(data) > 0, "返回数据为空"
        print(f"✅ 返回用户数: {len(data)}")

    def test_get_single_user(self):
        """GET /users/1 - 验证单个用户数据"""
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()
        assert "name" in data
        assert "email" in data
        print(f"✅ 用户: {data['name']}, 邮箱: {data['email']}")

    def test_create_user(self):
        """POST /users - 验证创建用户"""
        payload = {
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
        response = requests.post(f"{BASE_URL}/users", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test User"
        print(f"✅ 创建成功, ID: {data['id']}")

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_multiple_users(self, user_id):
        """GET /users/{id} - 参数化测试"""
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        assert response.status_code == 200


# ---------- 运行命令 ----------
# pytest test_api.py -v -s
# pytest test_api.py -v --html=report.html --self-contained-html
