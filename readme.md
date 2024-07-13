### Design Pattern项目

姓名：童书未

学号：21307253

时间：2024-6-9

Funny JSON Explorer（**FJE**），是一个JSON文件可视化的命令行界面小工具

```shell
fje -f <json file> -s <style> -i <icon family>

```

```shell
{
    oranges: {
        'mandarin': {                            ├─ oranges
            clementine: null,                    │  └─ mandarin
            tangerine: 'cheap & juicy!'  -=>     │     ├─ clementine
        }                                        │     └─ tangerine: cheap & juicy!
    },                                           └─ apples
    apples: {                                       ├─ gala
        'gala': null,                               └─ pink lady
        'pink lady': null
    }
}
````

```
┌─♢root─────────────────────────────────────┐
│  ├─♢oranges───────────────────────────────┤
│  │  └─♢mandarin───────────────────────────┤
│  │     ├─♤clementine──────────────────────┤
│  │     └─♤tangerine: cheap & juicy!───────┤
│  └─♢apples────────────────────────────────┤
├───────♤gala───────────────────────────────┤
└───────♤pink lady──────────────────────────┘

┌─♢oranges ───────────────────────────────┐
│  ├─♢mandarin ───────────────────────────┤
│  │  ├─♤clementine ──────────────────────┤
│  │  ├─♤tangerine: cheap & juicy! ───────┤
├─♢apples ────────────────────────────────┤
│  ├─♤gala ───────────────────────────────┤
└──┴─♤pink lady ──────────────────────────┘
```

FJE可以快速切换**风格**（style），包括：树形（tree）、矩形（rectangle）；

```shell
├─ oranges                             ┌─ oranges ───────────────────────────────┐
│  └─ mandarin                         │  ├─ mandarin ───────────────────────────┤
│     ├─ clementine                    │  │  ├─ clementine ──────────────────────┤
│     └─ tangerine: cheap & juicy!     │  │  ├─ tangerine: cheap & juicy! ───────┤
└─ apples                              ├─ apples ────────────────────────────────┤
   └─ gala                             └──┴─✩gala ───────────────────────────────┘

        树形（tree）                                   矩形（rectangle）
````

也可以指定**图标族**（icon family），为中间节点或叶节点指定一套icon

```
├─♢oranges                                 
│  └─♢mandarin                             
│     ├─♤clementine                        
│     └─♤tangerine: cheap & juicy!    
└─♢apples                                  
   └─♤gala                                 

poker-face-icon-family: 中间节点icon：♢ 叶节点icon：♤                 
```

接下来基于上述需求描述和领域模型，按照设计模式要求，进行软件设计，并编码实现要运行文件，可以在终端打开src文件夹，输入如下指令：

```py
python main.py -f example.json -s rectangle -i emoji -c icon_config.json
```

![image-20240609182631200](/Users/tongshw/Library/Application Support/typora-user-images/image-20240609182631200.png)

可以将rectangle换成tree或者新增的style：renderer

可以讲新增的图形族emoji换成default或者star或者pokerface等

^ ^