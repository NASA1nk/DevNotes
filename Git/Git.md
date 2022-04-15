# Git原理

版本管理

- 全量方案
- **增量方案**

![git](Git.assets/git.png)

## 版本库

所有版本信息存放在`.git`文件夹中（不会传上去）

文件命名
- 使用文件的`SHA-1`值作为文件名
- **`SHA-1`是一个哈希函数，使用文件的内容计算出一串数字作为文件特征，这样回滚后相同内容的文件也只会保留一份**

![SHA-1](Git.assets/SHA-1.png)

## 目录结构

树形结构

- `blob`：二进制数据文件
- `tree`：目录结构

![目录结构](Git.assets/%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)

使用`object`管理所有的目录结构

- `.git/objects`目录包含了创建的各种对象及内容

- **使用SHA-1的前两位对文件分级**（避免存储过多，索引太慢）

![文件分级](Git.assets/%E6%96%87%E4%BB%B6%E5%88%86%E7%BA%A7.png)

## 工作区和暂存区

**工作区**：本地目录

- 使用`git add`将文件添加到暂存区

**暂存区**：index或stage，一般存放在`.git/index`中，所以暂存区有时也叫作索引

- 使用`git commit`将文件提交到版本库

**版本库**：`.git`目录

![暂存](Git.assets/%E6%9A%82%E5%AD%98.png)

## 文件状态

![文件状态1](Git.assets/%E6%96%87%E4%BB%B6%E7%8A%B6%E6%80%811.png)

![文件状态2](Git.assets/%E6%96%87%E4%BB%B6%E7%8A%B6%E6%80%812.png)

## 快照

- 每一次`commit`都会产生一个新的快照，多次commit形成一条链表
- **每个快照都对应不同的SHA-1值，HEAD会指向最新的快照**

## 协同分支

冲突和合并

**合并方式**

- **Merge**
  - `git checkout`
  - `git merge`
- **Rebase**（会修改历史，建议本地用）
  - `git checkout`
  - `git rebase`
- Cheey-pick（合并某一版本）
  - `git checkout`
  - `git cheery-pick`



# Git配置

初始化：`git init`

- 当前本地仓库的配置文件如下

 ![git.config](Git.assets/.git.config.png)

## 配置用户信息

`--glboal`：修改Git的**全局配置文件**`~/.gitconfig`，而不是Git仓库里的配置文件`.git/config`

```bash
# 查看当前Git环境所有配置
# 可以配置一些命令别名
git config --list 
```

 ![设置个人信息](Git.assets/设置个人信息.png)

## 配置代理

```bash
# 全局配置代理
git config –-global http.proxy 10.134.143.124:1080
git config –-global https.proxy 10.134.143.124:1080

# 查看代理
git config –-global --get http.proxy
git config –-global --get https.proxy

# 取消代理
git config –-global --unset http.proxy
git config –-global --unset https.proxy
```



## SSH连接GitHub

在`config`文件中保存着连接的url

- 使用https url，通过git提交的时候要输入用户名和密码
- 使用ssh url，通过git提交的时候不需要繁琐的验证过程

 ![gitconfig](Git.assets/gitconfig.png)

### 创建密钥

在`~/.ssh`目录下生成密钥

```bash
ssh-keygen -t rsa -C "541640794@qq.com"
```

![生成密钥](Git.assets/生成密钥.png)

### 获取密钥

将公钥`id_rsa.pub`作为ssh key

![获取SSHKey](Git.assets/获取SSHKey.png)

### 创建SSH Key

1. `GitHub-Setting`
2. `SSH and GPG keys`
3. `New SSH key`
4. 复制`id_rsa.pub`即可 



## Git默认编码

使用命令行提交代码的时候会出现中文乱码问题，**因为UTF-8编码在git默认的配置上不能正常显示**

![gitbash乱码](Git.assets/gitbash乱码.png)

### 设置编码

windows：修改`core.quotepath`参数

- `core.quotepath`设为`false`就不会对`0×80`以上的字符进行quote，中文显示正常

```bash
# status编码

git config --global core.quotepath false

# gui编码
git config --global gui.encoding utf-8

# commit编码
git config --global i18n.commit.encoding utf-8

# log编码
git config --global i18n.logoutputencoding utf-8
```

linux：进入git安装目录，修改配置

`/etc/gitconfig`

```bash
# 代码库统一使用utf-8
[gui]
encoding = utf-8

# log编码 
[i18n]
commitencoding = utf-8

# 支持中文路径  
[svn]
pathnameencoding = utf-8
```



# Git命令

## 初始化

**将文件夹变成仓库**，创建隐藏文件夹`.git`

```bash
git init
```

## 添加到暂存区

将本地文件添加到**暂存区**

```bash
# 查看已修改的文件
git status

git add fileName

# 全部加入
git add .
```

## 提交

### 提交到本地仓库

`git add`后再提交到版本的本地库，可以在`head`文件中看到

- 每个commit都是一个版本（快照）

- 使用`git log`查看提交历史，可以查看`commit id`

```bash
# -m添加本次提交的注释
git commit -m "注释"
```

### 提交到远程仓库

```bash
git push 远程仓库
```

## 分支

**在新的分支上对文件的修改不会影响到原来分支上的文件**

### 查看分支

```bash
git branch

# 查看远程分支
git branch -r

# 查看本地和远程分支
git branch -a

# 查看远程分支和本地分支的对应关系
git remote show origin
```

### 创建新分支

```bash
# 仅创建新分支
git branch branchName

# 创建新分支并切换到该分支下
git checkout -b branchName
```

### 重命名分支

```bash
# 重命名分支
git branch -m oldName newName 

# -M：强制重命名，即使newName分支存在
git branch -M oldName newName

# 或者切换到要重命名的分支下执行
git branch -M newName
```

### 切换分支

```bash
# 切换到对应分支
git checkout branchName

# 切换到上一个分支
git checkout -
```

### 修改默认分支

> 以前默认是master分支

```bash
# 修改默认分支为main分支
git config --global init.defaultBranch main
```

### 删除分支

```bash
# 删除本地分支
git branch -d branchName

# 删除远程分支
git branch -d -r branchName 

# 删除upstream分支中被删除了的本地分支
git fetch -p
```

### 合并分支

```bash
# 先回到master主分支
git checkout master

# 合并分支
git merge branchName
```

### 分支冲突

假设a分出b和c

- a分出的分支b对**原分支**a的合并会直接覆盖，不会冲突

- 独立无关的分支b和c相互合并则会冲突

**放弃合并**

```bash
git merge -abort
```

**手动修改冲突**

```bash
# 1.打开冲突文件，git会自动显示冲突的内容（2者均显示）
#	branch1
#   <<<< 
#   file1
#	====
#   file2
#   >>>>
#   branch2

# 2.修改内容，并删除内容外的所有指示符号（<,=,>,branch_name）

# 3.重新提交修改后内容
```

 ![合并冲突](Git.assets/合并冲突.png)

## 暂存修改

**应用场景**

- 在开发时，突然需要去`pull`远程仓库的修改，此时可能报错，**所以需要把修改暂存到一个地方**
- 在开发时，忘记切换分支，在`master`上进行了开发，需要重新切回到`dev`分支上进行开发，可以暂存开发的代码，切回到`dev`分支后，恢复内容

> `stash`中的内容不仅仅可以恢复到原先开发的分支，也可以恢复到其他任意指定的分支上

```bash
# 1.执行后文件回到修改之前的状态，然后再pull，不会有冲突
git stash

# 1.可以添加注释
git stash save "stash1"

# 2.pull后查看之前暂存的修改
git stash list

# 3.恢复暂存的修改，会删除暂存的修改
git stash pop

# 3.恢复之前的修改，不会删除暂存的修改，可以应用多次到多个分支
git stash apply

# 4.移除某个指定的stash
git stash drop stash@{n}

# 4.移除所有暂存的修改
git stash clear

# 5.查看最新保存的stash和当前目录的差异
git stash show

# 5.查看最新保存的stash和当前目录的详细差异
git stash show -p

# 5.查看指定保存的stash和当前目录的差异
git stash show stash@{n}
```

把**暂存的内容**添加到上一次的commit

```bash
git commit --amend
```

将**未暂存的内容**移动到一个**新分支**

- 实际就是从当前分支创建一个新分支，修改的内容也同步过去了

> 此时只要恢复当前分支，即可取消修改

```bash
git checkout -b branchName
```

将未暂存的内容移动到一个**已存在的分支**

```bash
# 先暂存
git stash

# 再切换
git checkout branchName

# 再恢复
git stash pop  
```

## 修改和撤销

### Head

`HEAD`会指向最新的快照

- `HEAD^`：前1个commit
- `HEAD^^`：前2个commit
- `HEAD~4`：前4个commit

### Reset

`git reset`：用于回退版本，可以指定退回某一次提交的版本

- `--mixed`：默认参数，**重置暂存区的文件，使其和上一次的commit保持一致**，但工作区文件内容保持不变

```bash
git reset [--soft | --mixed | --hard] [HEAD]
```

### 取消暂存区的修改

```bash
# 取销add的内容
git reset

# 本地的修改还在，取消了add的状态
git reset --mixed 
```

### 修改commit

修改**未推送**的`commit`信息

```bash
# 打开默认编辑器, 可以编辑信息
git commit --amend --only  

# 直接修改
git commit --amend --only -m 'commit message' 
```

在错误的分支上commit，修改到正确的分支

```bash
# 1.在main下创建一个新分支，不切换到新分支，仍在main下，此时新分支上仍然有提交
git branch branchName
# 2.把main分支重置到前一个提交，即恢复main分支内容
git reset --hard HEAD^
# 3.切换到新分支，重新提交
git checkout branchName
```

从`commit`中移除一个文件

```bash
git checkout HEAD^ fileName  
git add -A  
git commit --amend 
```

### 删除提交

删除**已推送**的最后一次提交

```bash
git reset HEAD^ --hard

# 强制推送
git push -f remoteBranch 
```

删除**未推送**的最后一次提交

```bash
git reset --soft HEAD@{1}
git reset --soft 'HEAD^'()
```

### `reset --hard`后恢复内容

Git对每件事都会有日志，且都会保存几天

- 在日志中看到一个过去提交列表和一个重置的提交
- 选择想要回到的提交的SHA，再重置一次

```bash
git reflog  
git reset --hard SHA1234
```

### 取消rebase和merge

- Git在进行危险操作的时候会把原始的`HEAD`保存在一个叫`ORIG_HEAD`的变量里

```bash
git reset --hard ORIG_HEAD  
```



## 查看

### 查看git仓库

- `objects`下就是存放的文件目录分级

- `61`是存在的文件的**SHA-1值的前两位**，打开后就是**剩下的SHA-1值**
  - 拼接后才是完整的文件的SHA-1值，就可以定位到文件

```bash
cd .git && ls -la
cd objects && ls -la
```

 ![查看库内容](Git.assets/查看库内容.png)

### 查看文件内容

```bash
git cat-file -p SHA-1
```

### 查看暂存区

```bash
git ls-files --stage
```

### 查看日志

按q退出

```bash
git log 
```

### 查看提交内容

显示当前`HEAD`上的最近一次的commit

```bash
git show

git log -n1 -p
```



### 查看区别

`git diff commit_id_1 commit_id_2`

```bash
# 比较两个版本之间的差异
git diff commit_id_1 commit_id_2 > d:/diff.txt
# 结果文件diff.txt中
# "-"号开头的表示 commit_id_2 相对 commit_id_1 减少了的内容。
# "+"号开头的表示 commit_id_2 相对 commit_id_1 增加了的内容。
```

# 远程仓库

`origin`：远程地址的别名

```bash
# 显示远程仓库
git remote

# fetch 和 push
git remote -v

# 查看远程仓库信息
git remote show remoteUrl
```

## 链接远程仓库

- 因为使用命令行创建的存储库的默认分支名称是`master`，而在GitHub中创建的仓库默认分支是`main`，所以需要修改

  ![修改分支名](Git.assets/修改分支名.png)

- 远程仓库的名字默认是`origin`


```bash
# 1.create a new repository
git init
git add .
git commit -m "first commit"
# 修改分支名
git branch -M main
# 将本地仓库与远端仓库建立链接
# origin是远程仓库名
git remote add origin git@github.com:NASA1nk/test.git
git push -u origin main
```

## 删除远程仓库

```bash
git remote rm name
```

## 修改远程仓库名

```bash
git remote rename oldName newName
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

新建文件夹，在终端中执行`git init`

![VSCode创建仓库](Git.assets/VSCode创建仓库.png)

2.在git模块点√提交文件（输入的是commit的注释）

- U：unstage


- M：modified 


 ![VSCodeGit状态](Git.assets/VSCodeGit状态.png)

3.查看历史信息

可以`git checkout SHA-1`切换版本

 ![VSCode查看信息](Git.assets/VSCode查看信息.png)

4.创建和切换分支

点击左下角的main图标

 ![VSCode创建分支](Git.assets/VSCode创建分支.png)

5.提交文件

在main图标旁边的就是push按钮



## IDEA

1. 查看idea中的git配置

   1. 在`settings-Version Control`中点击`Test`，出现git版本号则表示成功

   ![idea查看git配置](Git.assets/idea查看git配置.png)

2. 配置本地仓库

   1. 在工具栏选择`VCS-Create Git Repository`，选择本地目录
   2. 创建完成后会出现`.git`目录

    ![idea创建本地仓库](Git.assets/idea创建本地仓库.png)

3. 右键想要提交的文件，选择`Git-Add`

   1. 更改或新增的文件颜色会变为红色
   2. `Add`过后的文件颜色会变为绿色

    ![ideaadd文件](Git.assets/ideaadd文件.png)

4. 右键想要提交的文件，选择`Git-Commit Directory`

   1. 填写commit message
   2. 上方可以选择或取消文件
   3. 然后点击右下方的`Commit`

   ![ideacommit文件](Git.assets/ideacommit文件.png)

5. 右键要提交的项目，选择`Git-push`

   1. 第一次提交需要链接远程仓库

      ![idea链接远程仓库](Git.assets/idea链接远程仓库.png)

   2. 提交文件到远程仓库

      ![ideapush文件](Git.assets/ideapush文件.png)

   
   













