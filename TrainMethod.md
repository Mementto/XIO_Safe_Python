# 训练方式

## 第一步：存入数据集
**以下是数据集的路径**
````
YOLOX-main
├── datasets
│   ├── VOCdevkit
│   │   ├── annotations_cache
│   │   ├── results
│   │   ├── VOC2007
│   │   │   ├── Annotations
│   │   │   ├── ImageSets
│   │   │   │   ├── Main
│   │   │   │   │   ├── test.txt
│   │   │   │   │   ├── train.txt
│   │   │   │   │   ├── trainval.txt
│   │   │   │   │   ├── val.txt
│   │   │   ├── JPEGImages
│   │   │   ├──make_trin_val_test_set.py
│   ├── README.md
````
[1]在训练前删除`annotations_cache`和`results`文件夹。

[2]将要训练的图片放入`JPEGImages`中，将标签xml文件放入`Annotations`中。

[3]打开`make_trin_val_test_set.py`文件，修改其中的`train_percent`变量，该变量是用来设置训练集和验证集的比例，（例如`train_percent = 0.7`表示将百分之70的数据集用作训练，剩下的用作验证），以括号中的比例为基准如果图片过多可以降低`train_percent`的值，反之增大`train_percent`的值

[4]执行`make_trin_val_test_set.py`文件
***
## 第二步：修改输出分类
**以下是网络输出分类的路径**
````
YOLOX-main
├── yolox
│   ├── core
│   ├── data
│   │   ├── datasets
│   │   │   ├── coco_classes.py
│   │   │   ├── voc_classes.py
│   ├── evaluators
│   ├── exp
│   ├── layers
│   ├── models
│   ├── utils
````
[1] 将你数据集中的所有标签类型输入到`coco_classes.py`和`voc_classes.py`中（例如你的标签类型只有person，那么只需在那两个文件中填入"person"，如果有person和dog，那么需要填入"person"以及"dog"）

**以下是网络参数文件路径**
````
YOLOX-main
├── exps
│   ├── default
│   ├── example
│   │   ├── custom
│   │   ├── yolox_voc
│   │   │   ├── yolox_voc_s.py
````
[2] 将你数据集中的标签数量输入到`yolox_voc_s.py`中（例如你的标签类型只有person，那么只需将文件中的变量`self.num_classes`修改为1，如果有person和dog，那么修改为2）
***

## 第三步：纠错
**标签中可能会出现类型错误（例如将person误写成了dog），训练时会报KeyError错误**

[1]选中pycharm的顶部菜单栏Edit-->Find-->Find in Files，弹出框中输入dog，下面就会显示全部含有dog字符的文件（包括xml文件）

[2]将xml中的dog全部改成person
***

## 第四步：训练
````
YOLOX-main
├── tools
│   ├── YOLOX_outputs
│   ├── demo.py
│   ├── eval.py
│   ├── train.py
│   ├── trt.py
````
[1]删除`YOLOX_outputs`文件夹

[2]执行`train.py`文件