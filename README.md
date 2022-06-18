# 三维超声重建图像恢复

3D-Ultrasound-Reconstructed-Image-Restoration

## 项目介绍

### 项目背景及意义

三维超声重建图像在医学上应用十分广泛，主要用于人体各器官与部位的无创检查等。目前三维超声重建图像的噪声较大，且不同角度的超声切片提供的信息有限。本项目着重于超声重建图像的增强，在不影响正常诊断的情况下得到更为清晰、鲜活的胎儿图像。

本项目通过深度学习的方法，在不影响正常诊断、保留原始图片信息的情况下，对胎儿三维超声重建图像进行增强。同时，提出使用 CycleGAN 与 VAE 进行迁移训练、使用拉普拉斯金字塔的传统方法图像增强以及基于渐进式深度神经网络PSFRGAN的深度学习方法提升人脸图像清晰度的方法，解决了针对胎儿人像图片优化的数据集不足的问题，能够有效提升超声重建图像人脸清晰度。

### 项目结构

本项目由三部分组成：

- **[Data Transfer](https://github.com/x418-22n/style-transfer-in-ultrasound-reconstruction)**

  基于CycleGAN实现大批量生成三维超声重建风格图像，用以扩充数据集。

- **[Traditional Preprocessing](https://github.com/Meowemeow/llf-for-3D-Ultrasound-Reconstructed-Images)**

  基于传统方法实现的三维超声重建图像恢复与优化算法，用来对数据进行预处理。

- **[PSFRGAN](https://github.com/Rhinophant/PSFRGAN-for-3D-Ultrasound-Reconstructed-Images)**

  基于[PSFRGAN](https://github.com/chaofengc/PSFRGAN)实现的三维超声重建图像恢复与优化算法。

本项目结构如下图所示：

![Project Structure](https://github.com/Rhinophant/3D-Ultrasound-Reconstructed-Image-Restoration/blob/main/pics/project_structure.png)

1. 数据迁移可以将自然图像中的婴幼儿图片转化为三维超声重建图像的风格。将这些由风格迁移生成的图像与原始三位超声重建图像结合，可以得到扩充后的数据集。
2. 使用传统方法对数据进行处理，得到的结果可以作为预处理输入到深度学习方法中。
3. 深度学习方法可以直接对原始图像进行处理，也可以以传统方法的输出作为输入，进行处理。

## 环境要求

- Python 3.8 +

- **Data Transfer**

  - 使用以下命令来安装依赖：

    ```
    pip install paddlepaddle
    pip install --upgrade ppgan
    pip install -r Data_Transfer/requirements.txt
    ```

  - 下载数据集、模型以及运行结果：

    -  [BaiduNetDisk](https://pan.baidu.com/s/1Ic2PRXgGoMoULS8ketlhFA)，提取码`1234`。
    - 数据集放置在路径 `data/ourdata` 下。
    - 模型文件放在`output_dir/model.pdparams`下。
    - 运行结果位于`output_dir/out`。

- **Traditional Preprocessing**

  使用以下命令来安装依赖：

  ```
  pip install opencv-python
  ```

- **PSFRGAN**

  - CUDA 10.1

  - 使用以下 命令安装依赖：

    ```
    pip install -r PSFRGAN/requirements.txt
    ```

  - 下载预训练模型：

    - [BaiduNetDisk](https://pan.baidu.com/s/1R2NCCvpTUPouiFfuIw88kA)，提取码：`y7in`。
    - 将所有预训练模型放置在路径 `./PSFRGAN/pretrain_models` 下。

## 测试运行

可以使用以下命令来测试运行：

```
python run.py
```

项目各部分测试运行方式参见本项目子模块中的说明。

## 结果展示

<center><b>超声重建图像处理前后对比</b></center>

<center>
	<img src='https://github.com/Rhinophant/PSFRGAN-for-3D-Ultrasound-Reconstructed-Images/blob/master/test_dir/147.png' width=300><img src='https://github.com/Rhinophant/PSFRGAN-for-3D-Ultrasound-Reconstructed-Images/blob/master/test_result/HQ/000.jpg' width=300>
</center>
