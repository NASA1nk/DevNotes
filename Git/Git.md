<!-- TOC -->

- [Git原理](#git原理)
  - [版本库](#版本库)
  - [目录结构](#目录结构)
  - [暂存区](#暂存区)
  - [文件状态](#文件状态)
  - [快照](#快照)
  - [协同分支](#协同分支)
- [Git命令](#git命令)
  - [初始化](#初始化)
  - [添加](#添加)
  - [提交](#提交)
  - [撤销](#撤销)
  - [查看](#查看)
    - [查看git仓库](#查看git仓库)
    - [查看文件内容](#查看文件内容)
    - [查看暂存区](#查看暂存区)
    - [查看日志](#查看日志)
  - [分支](#分支)
    - [查看分支](#查看分支)
    - [创建新分支](#创建新分支)
    - [切换分支](#切换分支)
    - [合并分支](#合并分支)
    - [合并冲突](#合并冲突)
  - [修改记录暂存](#修改记录暂存)
- [远程仓库](#远程仓库)
  - [Github](#github)
  - [配置其他仓库](#配置其他仓库)
- [Git工具](#git工具)
  - [VSCode](#vscode)

<!-- /TOC -->

# Git原理

版本管理

- 全量方案
- 增量方案

![git](Git.assets/git.png)

## 版本库

所有版本信息存放在`.git`文件夹中（不要传上去）

文件命名：使用文件的`SHA-1`值作为文件名

SHA-1是一个哈希函数，使用文件的内容计算出一串数字作为文件特征。这样回滚后相同内同的文件也只会保留一份。

![SHA-1](Git.assets/SHA-1.png)

## 目录结构

树形结构

- blob：数据文件（二进制）
- tree：目录结构

![目录结构](Git.assets/%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)

使用`object`管理所有的目录结构，并且用SHA-1的前两位对文件分级（避免存储过多，索引太慢）

![文件分级](Git.assets/%E6%96%87%E4%BB%B6%E5%88%86%E7%BA%A7.png)

## 暂存区

本地仓库

- git add
- git commit

![暂存](Git.assets/%E6%9A%82%E5%AD%98.png)

## 文件状态

![文件状态1](Git.assets/%E6%96%87%E4%BB%B6%E7%8A%B6%E6%80%811.png)

![文件状态2](Git.assets/%E6%96%87%E4%BB%B6%E7%8A%B6%E6%80%812.png)

## 快照

`commit`会产生一个新的快照（多次commit形成一条链表），每个对应不同的SHA-1值，HEAD会指向最新的快照

## 协同分支

冲突和合并

合并方式：

- Merge：
  - git checkout
  - git merge
- Rebase（会修改历史，建议本地用）
  - git checkout
  - git rebase
- Cheey-pick（合并某一版本）
  - git checkout
  - git cheery-pick

# Git命令

## 初始化

创建隐藏文件夹.git

```bash
git init
```

## 添加

由本地添加到暂存区

```bash
git add file_name

#全部加入
git add .
```

## 提交

add后提交到版本库，可以在head文件中看到

```bash
git commit -m "注释"
```

## 撤销

```bash
#1.提示命令，在想撤销的命令后一条输入（紧挨着）
gitjk

#git add的撤销(git reset)
git add .
gitjk

#git commit的撤销git reset --soft 'HEAD^'()
git commit file_name -m "注释"
gitjk

#2.版本回退
git checkout SHA-1

#3.版本回退并将之创建为新的分支
git checkout -b SHA-1
```

## 查看

### 查看git仓库

```bash
cd .git && ls -la
cd objects && ls -la
```

![查看库内容](Git.assets/查看库内容.png)

这里面objects下就是存放的文件目录分级

61就是存在的文件的SHA-1值的前两位，打开后就是剩下的SHA-1值，拼接后才是完整的文件的SHA-1值，就可以定位到文件

### 查看文件内容

```bash
git cat-file -p SHA-1
```

### 查看暂存区

```bash
git ls-files --stage
```

### 查看日志

```bash
git log 
```

## 分支

### 查看分支

```bash
git status
```

### 创建新分支

创建后不会自动切换到新的分支

```bash
git branch branch_name
```

### 切换分支

```bash
git checkout branch_name
```

在新的分支上对文件的修改**不会影响**到原来分支上的文件

### 合并分支

```bash
#先回到master主分支
git checkout master
#合并分支
git merge branch_name
```

### 合并冲突

假设a分出b和c

a分出的分支b对**原分支**a的合并会直接覆盖，不会冲突

独立无关的分支b和c相互合并则会冲突

- 放弃合并

  ```bash
  git merge -abort
  ```

- 手动修改冲突

  ```bash
  #1.打开冲突文件,git会自动显示冲突的内容（2者均显示）
  #	branch1
  #   <<<< 
  #   file1
  #	====
  #   file2
  #   >>>>
  #   branch2
  
  #2.修改内容，并删除内容外的所有指示符号（<,=,>,branch_name）
  
  #3.重新提交修改后内容
  ```

![合并冲突](Git.assets/合并冲突.png)

## 修改记录暂存

假如在你修改的时候需要去pull远程仓库的内容，此时可能报错

所以我们需要把我们的修改暂存到一个地方

```bash
#1.执行后文件回到修改之前,先pull
git stash

#2.pull后查看之前的修改
git stash list

#3.添加之前的修改
git stash apply

#4.清除暂存的修改
git stash clear
```



# 远程仓库

```bash
git remote
```

## Github

本地一般使用master做主分支，git使用main做主分支，需要修改

![github](Git.assets/github.png)

```bash
#1.create a new repository
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:NASA1nk/test.git
git push -u origin main

#2.push an existing repository
git remote add origin git@github.com:NASA1nk/test.git
git branch -M main
git push -u origin main

#3.从远程仓库拉取文件,默认origin(main)分支
git pull

#4.提交文件到远程仓库,默认origin(main)分支
git push
```

## 配置其他仓库

```bash
#1.查看远程仓库分支
git remote

#2.查看远程仓库分支内容
#  可以查看配置的仓库内容进而修改
git remote show branch_name

#3.删除配置
git remote remove branch_name

#4.配置仓库url
git remote add origin repository_url

#5.提交
git push -u origin main
```

# Git工具

## VSCode

1.初始化

新建文件夹，在终端中执行git init

![VSCode创建仓库](Git.assets/VSCode创建仓库.png)

2.在git模块点√提交文件（输入的是commit的注释）

- U：unstage


- M：modified


![VSCodeGit状态](Git.assets/VSCodeGit状态.png)

3.查看历史信息

可以git checkout SHA-1切换版本

![VSCode查看信息](Git.assets/VSCode查看信息.png)

4.创建和切换分支

点击左下角的mian图标

![VSCode创建分支](Git.assets/VSCode创建分支.png)

5.提交文件

在main图标旁边的就是push按钮