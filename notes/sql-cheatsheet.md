# SQL 速查表

---

## 📖 基础查询

```sql
-- 查询所有列
SELECT * FROM table_name;

-- 查询指定列
SELECT col1, col2 FROM table_name;

-- 去重
SELECT DISTINCT col1 FROM table_name;

-- 别名
SELECT col1 AS 别名 FROM table_name;

-- 限制条数（MySQL）
SELECT * FROM table_name LIMIT 10;

-- 限制条数（Oracle）
SELECT * FROM table_name WHERE ROWNUM <= 10;
```

---

## 🔍 条件查询

| 操作符 | 说明 | 示例 |
|--------|------|------|
| `=` | 等于 | `WHERE status = 'active'` |
| `!=` / `<>` | 不等于 | `WHERE status != 'deleted'` |
| `>` `<` `>=` `<=` | 比较 | `WHERE age >= 18` |
| `BETWEEN` | 范围 | `WHERE age BETWEEN 18 AND 60` |
| `IN` | 多值匹配 | `WHERE city IN ('BJ', 'SH')` |
| `LIKE` | 模糊查询 | `WHERE name LIKE '%test%'` |
| `IS NULL` | 空值 | `WHERE deleted_at IS NULL` |
| `AND` / `OR` | 逻辑组合 | `WHERE a=1 AND b=2` |

---

## 📊 聚合函数

```sql
SELECT
    COUNT(*)   AS 总数,
    SUM(amount) AS 合计,
    AVG(amount) AS 平均,
    MAX(amount) AS 最大,
    MIN(amount) AS 最小
FROM orders;
```

---

## 🔗 表连接

```sql
-- INNER JOIN（交集）
SELECT * FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN（左表全量）
SELECT * FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- RIGHT JOIN（右表全量）
SELECT * FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## 📝 增删改

```sql
INSERT INTO users (name, email) VALUES ('张三', 'zhang@test.com');

UPDATE users SET status = 'inactive' WHERE id = 1;

DELETE FROM users WHERE id = 1;
```

---

## 🎯 面试常考

```sql
-- 查询每个部门的平均工资（分组）
SELECT dept_id, AVG(salary) FROM employees GROUP BY dept_id;

-- 查询工资>平均工资的员工（子查询）
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- 查询第11-20条记录（分页）
SELECT * FROM users LIMIT 10 OFFSET 10;

-- 查询重复数据
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;
```
