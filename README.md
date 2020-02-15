# 小玩具：人教电子版教材爬虫

__（这仅仅是个玩具而已）__

## 依赖项安装

```sh
pip3 install scrapy
```

## 玩法

先修改 ./pepbookspider/settings.py 中的 `FILES_STORE` 为想要存储下载的PDF的文件夹路径。

执行示例：（-o指定的文件必须不存在，若存在，新内容会被追加到末尾导致JSON格式不正确）

```sh
scrapy crawl pepbook -o files.json -a "filt=数学.*修"
python3 rearrange_files.py files.json # 将文件重命名为网站上显示的书名
```

`-a filt=XXX` 是可选的，可提供一个正则表达式用于筛选文件。等号后面不用引号，如需引号应加在filt之前，正则表达式之后。