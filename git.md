git笔记

git init 可以把一个新的空的目录初始化成git的版本的仓库（里面多了了.git文件夹)

git add 把文件的改变添加到暂存区（stage），相反的是git reset HEAD file，从暂存区撤销。

git checkout -- readme.txt
就是让这个文件回到最近一次git commit或git add时的状态。（一键还原，从提交到的版本库中还原到本地工作区）

git commit 提交到git，-m对本次提交的说明（把暂存区的内容提交到当前分支）（每创建git版本库的时候，git自动创建了唯一一个master分支。

电脑里看到的目录叫做工作区，.git目录是git的版本库，

未添加的文件显示为untracked

github是一个给git的用户免费提供远程仓库的网站。省去了自己搭建git服务器了。Git仓库托管服务的，所以，只要注册一个GitHub账号，就可以免费获得Git远程仓库。

要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；
git remote remove origin取消关联;

关联后，使用命令git push -u origin master第一次推送master分支的所有内容；

此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；

Git鼓励大量使用分支：

查看分支：git branch

创建分支：git branch <name>

切换分支：git checkout <name>

创建+切换分支：git checkout -b <name>

合并某分支到当前分支：git merge <name>

删除分支：git branch -d <name>
