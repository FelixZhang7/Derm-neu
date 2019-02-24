# 皮肤病检测分类程序Derm-neu
使用数据集[Dermne](http://www.dermnet.com/dermatology-pictures-skin-disease-pictures)，默认参数时测试准确率61.5%
---
数据集可从DropBox下载[train](https://www.dropbox.com/s/h5yora9j0onglw6/train.zip?dl=0)  [test](https://www.dropbox.com/s/c94io61nmldcgv8/test.zip?dl=0)
## 运行代码前，需要将图片放在data目录下，目录树如下：

	|--data
		|--train
		   |--AcneandRosaceaPhotos
		   ...
		   ...
		|--test
	|--gen_label_csv.py
	|--model_v4.py
	|--main_inception_v4.py

---
## 运行方式：
	python gen_label_csv.py
	python main_inception_v4.py

---
## 程序说明：
框架：Pytorch 0.4

使用的模型为ImageNet预训练的inception v4，整体思路：数据增强之后直接将网络全部层一起训练，做简单分类。

输入尺寸为384×384


