# 🧪 software-testing-learning

📚 我的软件测试学习记录与作品集

> 从零开始学软件测试 | 2026.06.20 起 | 目标：2026年10月拿到实习Offer

---

## 🎯 学习路线

| 阶段 | 时间 | 内容 | 状态 |
|------|------|------|------|
| 第一阶段 | 6.20-7.31 | 手工测试 + 理论基础 | 🔄 进行中 |
| 第二阶段 | 8.01-8.31 | 接口测试 + SQL + Linux | ⏳ 待开始 |
| 第三阶段 | 9.01-9.30 | Python + 自动化测试 | ⏳ 待开始 |
| 第四阶段 | 10.01-10.15 | 实战收官 + 面试冲刺 | ⏳ 待开始 |

---

## 📁 仓库结构


```
software-testing-learning/
├── 📄 README.md                    ← 💎 面试官第一眼看的门面
│
├── 📁 test-cases/                  ← 手工测试能力证明
│   ├── 01-登录模块用例.md
│   ├── 02-下单流程用例.md
│   ├── 03-金融项目用例.md
│   └── ...
│
├── 📁 bug-reports/                 ← Bug发现能力证明
│   ├── BUG-20260620-001.md
│   ├── BUG-20260621-002.md
│   └── ...
│
├── 📁 test-scripts/
│   ├── 📁 sql/                     ← SQL能力证明
│   │   └── practice-queries.sql
│   ├── 📁 api-tests/               ← 接口测试能力证明
│   │   ├── postman-collection.json
│   │   ├── test_api.py
│   │   └── jmeter-script.jmx
│   ├── 📁 ui-tests/               ← 💎 自动化能力证明（最重要）
│   │   ├── pages/                  ← POM 页面对象
│   │   ├── tests/                  ← 测试用例
│   │   ├── reports/                ← Allure 报告
│   │   └── conftest.py
│   └── 📁 python-basics/          ← 编程基础
│       └── daily-practice/
│
├── 📁 notes/                       ← 学习笔记
│   ├── linux-commands.md
│   ├── sql-cheatsheet.md
│   ├── interview-qa.md
│   └── 📁 git学习资源/
│       ├── git-practice-websites.md
│       └── git-common-commands.md
│
└── 📁 screenshots/                 ← 各种截图证明
    ├── test-results/
    └── bug-screenshots/
```
---

## 🛠️ 技能清单

- [ ] 测试用例设计（等价类/边界值/场景法/判定表）
- [ ] 缺陷管理（禅道/JIRA）
- [ ] 接口测试（Postman）
- [ ] SQL 数据库操作
- [ ] Linux 常用命令
- [x] Git 版本控制（基本命令 + VSCode 操作）
- [ ] Python 编程
- [ ] Selenium Web UI 自动化
- [ ] Pytest 测试框架
- [ ] JMeter 性能测试
- [ ] Allure 测试报告
- [ ] CI/CD 集成（Jenkins / GitHub Actions）

---

## 📝 学习日志

### 2026.06.24
- ✅ 学习 Git 基本命令（add / commit / push / pull / branch / merge 等）
- ✅ 掌握在 VSCode 中使用 Git 进行版本控制
- ✅ 整理 Git 学习资源与常用命令速查

---

## 🚀 如何使用

```bash
# 克隆仓库
git clone https://github.com/1452388/software-testing-learning.git
cd software-testing-learning

# 运行 Python 接口测试
cd test-scripts/api-tests
pip install requests pytest
pytest test_api.py -v

# 运行 SQL 练习（需 MySQL 环境）
mysql -u root -p < test-scripts/sql/practice-queries.sql
```

---

> 💪 每天进步一点点，10月见分晓！
