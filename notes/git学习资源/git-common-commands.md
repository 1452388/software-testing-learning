# 🔧 Git 常用命令速查

---

## 📦 基础操作

```bash
# 初始化仓库
git init

# 克隆仓库
git clone <url>

# 查看状态
git status

# 查看日志
git log --oneline --graph --all
```

---

## 📝 暂存与提交

```bash
# 添加到暂存区
git add <file>          # 添加指定文件
git add .               # 添加所有文件

# 提交
git commit -m "commit message"

# 查看差异
git diff                # 工作区 vs 暂存区
git diff --staged       # 暂存区 vs 最新提交
```

---

## 🌿 分支操作

```bash
# 查看分支
git branch              # 本地分支
git branch -a           # 所有分支（含远程）

# 创建/切换分支
git branch <name>       # 创建分支
git checkout <name>     # 切换分支
git checkout -b <name>  # 创建并切换

# 合并/删除
git merge <branch>      # 合并分支
git branch -d <name>    # 删除分支
```

---

## 🔄 撤销操作

```bash
# 撤销工作区修改
git restore <file>

# 撤销暂存区
git restore --staged <file>

# 回退版本
git reset --soft HEAD~1   # 保留修改
git reset --hard HEAD~1   # 丢弃修改

# 反做某次提交（安全）
git revert <commit-hash>
```

---

## ☁️ 远程仓库

```bash
# 查看远程
git remote -v

# 推送/拉取
git push origin <branch>
git pull origin <branch>
git fetch origin

# 关联远程
git remote add origin <url>
```

---

## 🛠️ 实用技巧

```bash
# 储藏当前修改（临时切换分支）
git stash
git stash pop

# 修改最后一次提交信息
git commit --amend -m "new message"

# 查看某行代码是谁写的
git blame <file>

# 打标签
git tag v1.0.0
git push --tags
```
