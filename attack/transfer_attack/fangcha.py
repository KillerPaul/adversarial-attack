import os
import numpy as np
from scipy import stats
from PIL import Image
from torchvision import models, transforms
import torch

# 假设你的数据根目录
data_root = r"C:\Users\Admin\Desktop\SFCoT-main\dataset\FGSCR_42\test"  # 每个子文件夹是一个类别，共42个类别

# 定义图片预处理和特征提取器（以 ResNet18 为例）
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
model = models.resnet18(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])  # 去掉全连接层
model.eval()

# 定义一个函数提取图片特征（返回一维向量）
def extract_feature(image_path):
    image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  # 添加 batch 维度
    with torch.no_grad():
        features = model(input_batch)
    # 将 features 从 (1, C, 1, 1) 转换为 (C,)
    return features.squeeze().numpy()

# 创建字典存储各类别的某个特征维度的数值
features_by_class = {}

# 遍历数据集文件夹
for class_name in os.listdir(data_root):
    class_dir = os.path.join(data_root, class_name)
    if os.path.isdir(class_dir):
        features_list = []
        for filename in os.listdir(class_dir):
            file_path = os.path.join(class_dir, filename)
            try:
                feat = extract_feature(file_path)
                features_list.append(feat)
            except Exception as e:
                print(f"读取 {file_path} 出错: {e}")
        if features_list:
            # 将特征转为 numpy 数组，形状为 (样本数, 特征维度)
            features_array = np.array(features_list)
            features_by_class[class_name] = features_array

# 假设我们对第0个特征维度进行 ANOVA 分析
group_data = []
for class_name, features in features_by_class.items():
    # 提取所有图片的第0个特征
    group_data.append(features[:, 0])

# 进行 ANOVA 检验
F, p = stats.f_oneway(*group_data)
print("F值:", F)
print("p值:", p)
