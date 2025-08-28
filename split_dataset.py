import os
import shutil
from sklearn.model_selection import train_test_split

# 数据集文件夹路径
data_dir = r"C:\Users\Admin\Desktop\SFCoT-main\dataset\FGSCR_42"

# 假设数据集包含子文件夹，每个子文件夹代表一个类别
categories = os.listdir(data_dir)

# 创建训练集和测试集的目标文件夹
train_dir = r"C:\Users\Admin\Desktop\SFCoT-main\dataset\FGSCR_42\train"
test_dir = r"C:\Users\Admin\Desktop\SFCoT-main\dataset\FGSCR_42\test"
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for category in categories:
    category_path = os.path.join(data_dir, category)
    
    # 检查当前路径是否是文件夹
    if os.path.isdir(category_path):
        # 获取类别下所有图片文件
        images = os.listdir(category_path)
        
        # 按照 4:1 的比例划分数据
        train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
        
        # 创建类别子文件夹
        os.makedirs(os.path.join(train_dir, category), exist_ok=True)
        os.makedirs(os.path.join(test_dir, category), exist_ok=True)
        
        # 移动文件到相应的训练集和测试集文件夹
        for image in train_images:
            shutil.move(os.path.join(category_path, image), os.path.join(train_dir, category, image))
        
        for image in test_images:
            shutil.move(os.path.join(category_path, image), os.path.join(test_dir, category, image))

print("数据集划分完成！")
