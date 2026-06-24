-- ============================================
-- SQL 练习：日常查询语句
-- 学习日期：2026.06.20 起
-- ============================================

-- ---------- 基础查询 ----------

-- 1. 查询所有用户信息
SELECT * FROM users;

-- 2. 查询指定列（用户名 + 邮箱）
SELECT username, email FROM users;

-- 3. 条件查询：查询状态为"已激活"的用户
SELECT * FROM users WHERE status = 'active';

-- 4. 排序：按注册时间倒序
SELECT * FROM users ORDER BY created_at DESC;

-- 5. 限制返回条数：前10条
SELECT * FROM users LIMIT 10;

-- ---------- 模糊查询 ----------

-- 6. 查询用户名包含"test"的用户
SELECT * FROM users WHERE username LIKE '%test%';

-- 7. 查询邮箱以@gmail.com结尾的用户
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- ---------- 聚合函数 ----------

-- 8. 统计用户总数
SELECT COUNT(*) AS total_users FROM users;

-- 9. 按状态分组统计
SELECT status, COUNT(*) AS count FROM users GROUP BY status;

-- 10. 查询每个用户的订单数（JOIN）
SELECT u.username, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;

-- ---------- 子查询 ----------

-- 11. 查询订单金额 > 平均订单金额的订单
SELECT * FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);

-- 12. 查询有订单记录的所有用户
SELECT * FROM users
WHERE id IN (SELECT DISTINCT user_id FROM orders);

-- ---------- 增删改 ----------

-- 13. 插入新用户
INSERT INTO users (username, email, password, created_at)
VALUES ('newuser', 'newuser@test.com', 'hashed_pwd', NOW());

-- 14. 更新用户状态
UPDATE users SET status = 'inactive' WHERE id = 1;

-- 15. 删除测试数据
DELETE FROM users WHERE username LIKE 'test_%';
