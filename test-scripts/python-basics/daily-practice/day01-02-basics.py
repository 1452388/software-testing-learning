#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================
# Python 每日练习
# 日期：2026.06.20
# 主题：基础语法 + 数据类型
# ============================================

# ---------- Day 1: 变量与数据类型 ----------

# 1. 变量赋值
name = "测试工程师"
age = 22
salary = 15000.00
is_intern = True

print(f"我叫{name}，今年{age}岁，期望薪资{salary}")

# 2. 列表操作
test_types = ["功能测试", "接口测试", "性能测试", "自动化测试"]
test_types.append("安全测试")
print(f"测试类型: {test_types}")
print(f"共{len(test_types)}种测试类型")

# 3. 字典操作 - 测试用例
test_case = {
    "id": "TC-001",
    "title": "登录验证",
    "priority": "P0",
    "steps": ["打开页面", "输入账号", "输入密码", "点击登录"]
}
print(f"用例 {test_case['id']}: {test_case['title']}")

# ---------- Day 2: 循环与条件 ----------

# 4. 遍历测试数据
test_data = [
    ("admin", "123456", True),
    ("admin", "wrong", False),
    ("", "123456", False),
]

for username, password, expected in test_data:
    # 模拟登录逻辑
    if username == "admin" and password == "123456":
        result = True
    else:
        result = False
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"{status} | user={username}, pwd={password}")

# 5. 列表推导式 - 生成测试数据
test_ids = [f"TC-{i:03d}" for i in range(1, 11)]
print(test_ids)

# ---------- 运行 ----------
# python daily-practice.py
