<img width="1017" alt="image" src="https://user-images.githubusercontent.com/637919/182925421-dd5f222a-c8b7-4a79-8530-1ecdfb47b874.png">

pygelt写的card game，截图


主要想模仿stack那个游戏，两张或者多张卡牌可以堆叠后形成新的元素

非常有趣

### 建立环境
conda create --name pygame python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

### 激活之
conda activate pygame

### 安装

https://pyglet.readthedocs.io/en/latest/external_resources.html#third-party-libraries

pip install pyglet

https://glooey.readthedocs.io/en/latest/installation.html

pip install glooey

### 写起来很有趣

https://api.arcade.academy/en/latest/tutorials/card_game/index.html
最有参考价值的文章

### 转到windows的wsl2上来开发了
先去下载一个conda

https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=A

wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2022.05-Linux-x86_64.sh

不行，我意识到了，wsl2不能开发这个东西，因为是个gui的程序

https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent


### windows下增加ssh到github

ssh-keygen -t ed25519 -C "lemonhall2012@qq.com"

start-ssh-agent

(base) E:\development>start-ssh-agent
Removing old ssh-agent sockets
Starting ssh-agent:  done
Identity added: /c/Users/lemon/.ssh/id_ed25519 (lemonhall2012@qq.com)

然后它自动添加好了

clip < C:\Users\lemon/.ssh/id_ed25519.pub

然后就是copy粘贴

最后就是到web界面里add这个key了，这都简单了

conda create --name card_game python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda activate card_game

pip install pyglet

ok，这下子windows也可以了