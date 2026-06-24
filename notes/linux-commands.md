# Linux 常用命令速查

---

## 📁 文件与目录操作

| 命令 | 说明 | 示例 |
|------|------|------|
| `ls -la` | 列出所有文件（含隐藏） | `ls -la /var/log` |
| `cd` | 切换目录 | `cd /home/user` |
| `pwd` | 显示当前路径 | `pwd` |
| `mkdir -p` | 递归创建目录 | `mkdir -p a/b/c` |
| `rm -rf` | 递归强制删除 | `rm -rf temp/` |
| `cp -r` | 递归复制 | `cp -r src/ dst/` |
| `mv` | 移动/重命名 | `mv old.txt new.txt` |
| `find` | 查找文件 | `find . -name "*.log"` |
| `tail -f` | 实时查看日志 | `tail -f app.log` |
| `chmod` | 修改权限 | `chmod 755 script.sh` |

---

## 📊 进程与系统

| 命令 | 说明 |
|------|------|
| `ps -ef` | 查看所有进程 |
| `top` | 实时查看系统资源 |
| `kill -9 PID` | 强制终止进程 |
| `df -h` | 查看磁盘使用 |
| `free -m` | 查看内存使用 |
| `netstat -tunlp` | 查看端口占用 |

---

## 🔍 日志分析（测试必备）

```bash
# 查看最近100行日志
tail -100 app.log

# 搜索ERROR关键字
grep "ERROR" app.log

# 统计ERROR出现次数
grep -c "ERROR" app.log

# 查看ERROR上下5行
grep -C 5 "ERROR" app.log

# 按时间范围提取日志
sed -n '/2026-06-20 10:00/,/2026-06-20 11:00/p' app.log
```

---

## 🐳 Docker（常用）

```bash
docker ps -a              # 查看所有容器
docker logs -f 容器名      # 查看容器日志
docker exec -it 容器名 bash # 进入容器
docker-compose up -d       # 启动服务
docker-compose down        # 停止服务
```
