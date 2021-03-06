# 中文

- 快捷键`Ctrl + Shift + P`打开搜索栏，输入`configure language`在语言配置文件中将en-us修改成zh-cn，保存重启
- 安装中文插件`Chinese`

# 设置

文件-首选项-设置

VSCode支持选择配置也支持编辑setting.json文件修改配置

VSCode设置默认为UI的设置，可以通过文件-首选项-设置-搜索`workbench.settings.editor`选中json修改

# 快捷键

**编程**

- `Ctrl + 鼠标左键`：文件、函数等跳转
- `Alt + ←` ：跳转后返回原处
- `Ctrl + Shift + O`：列出函数名
- `Alt + Shift + F`（或者用右键菜单）：格式化代码
- `Ctrl + Shift + B`：单纯编译，按F5为编译加调试
- `ctrl + /`：添加/关闭行注释
- `Shift + Alt +A`：块区域注释
- `ctrl + Shift + [`：折叠区域代码
- `ctrl + Shift + ]`：展开区域代码

**行**操作：

- 光标不在行尾，重开一行：
  - `ctrl + enter` ：向下重开一行
  - `ctrl + shift + enter` ：向上重开一行
- 光标没有选择内容时删除一行：
  - `ctrl+ x`：剪切一行
  - `ctrl + shift + k`：直接删除一行
- 移动一行：
  - `alt + ↑`： 向上移动一行
  - `alt + ↓` ：向下移动一行
- 复制一行：
  - `shift + alt + ↓`： 向下复制一行
  - `shift + alt + ↑` ：向上复制一行

**词**操作：

- 选中一个词：`ctrl+ d`

**搜索/替换**：

- `ctrl + f` ：搜索

- `ctrl+ alt + f`： 替换
- `ctrl + shift + f`：在项目内搜索

**全局操作**：

- **Ctrl + `**：打开或关闭终端

- `ctrl + p`：列出近期打开的文件名
- `ctrl + Tab`：列出最近打开的文件，可用于文件间切换
- `ctrl + Shift + n`：打开新的编辑器窗口
- `ctrl + Shift + w`：关闭编辑器

- `Home`：标跳转到行头
- `End`：光标跳转到行尾
- `ctrl + Home`：跳转到页头
- `ctrl + End`：跳转到页尾

# 插件

- Bracket Pair Colorizer 2：彩虹花括号
- One Dark Pro：VSCode主题

# 同步

在不同的设备间同步VSCode设置需要用到Token和Gist id

- Token：把插件上传到github上时保存的一段字符

  > Tokens you have generated that can be used to access the GitHub API

- Gist id：在上传设置的电脑上保存

**上传配置步骤**

1. 在扩展商店中安装`Settings Sync`

2. 创建GitHub token：
   1. 打开Github-`Settings`-`Developer settings`-`Personal access tokens`-`generate new token`
   
   2. 在Note中输入token名，勾选`gist`提交
   
   3. 显示tokens
   
      ```bash
      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
      ```
   
3. 在VSCode中按`Ctrl+Shift+P`打开命令框，输入sync-高级选项-编辑本地扩展设置：编辑token

4. 在VSCode中按`Ctrl+Shift+P`打开命令框，输入sync-高级选项-打开设置：可以查看Gist ID

5. 在VSCode中按`Ctrl+Shift+P`打开命令框，输入sync-高级选项-打开设置，用tokens生成Gist ID：将tokens输入到获取令牌中

6. 在VSCode中按`Ctrl+Shift+P`打开命令框，输入sync-`update/upload settings`，上传成功后会返回Gist ID，保存Gist ID

   > 可根据步骤4中查看

   ```bash
   827945d088cc7c81e0105d490213060f
   ```

7. 打开Github-`Your gists`：可以查看同步设置



**下载配置步骤**

1. 在VSCode扩展商店中搜索`Settings Sync`并安装，重启
2. 在VSCode中按`Ctrl+Shift+P`打开命令框，输入sync-`update/upload settings`
3. 跳转到sync扩展的配置页面，点击`LOGIN WITH GITHUB`跳转至GitHub登录授权页，同意授权
4. 授权后回到VSCode，选择跟之前生成的令牌（token）对应的选项



