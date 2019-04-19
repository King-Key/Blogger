### 关于图像数据制作的准备
#### [以下所有程序的文件路径和参数都需要按照自己的需求进行设定]

[1] [make_train_val.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/make_train_val.py):图像数据的分割,根据设定的数目随机将图像数据划分为训练集和测试集,生成用于训练和测试的数据文件

[2] [add_data.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/add_data.py):为图像数据增加椒盐噪声,并将标签文件进行相应的复制与修改,进行数据扩充

[3] [data_make.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/data_make.py):生成带坐标的数据文件

[4] [data_prepare.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/data_prepare.py):对图片数据进行随机分割,生成测试和验证集的数据文件

[5] [data_TFrecord.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/data_TFrecord.py):生成.tfrecord数据

[6] [resize.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/resize.py):批量修改图片大小

[7] [train_test_dir.py](https://github.com/King-Key/Blogger/blob/master/Forimgdata/train_test_dir.py):根据图像数据集生成相应的训练测试集（适用于图像分类的数据集制作）