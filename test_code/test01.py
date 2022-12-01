from sklearn.tree
import export_graphviz
import graphviz
import os
# 以下这两行是手动进行环境变量配置，防止在本机环境的变量部署失败
os.environ['PATH'] = os.pathsep + r'C:\Program Files (x86)\Graphviz2.38\bin'
# 生成dot_data
dot_data = export_graphviz(model, out_file=None, feature_names=X_train.columns, class_names=['不流失', '流失'], rounded=True, filled=True)
# rounded和字体有关，filled设置颜色填充
# 将生成的dot_data内容导入到txt文件中
f = open('dot_data.txt', 'w') f.write(dot_data)
f.close()
# 修改字体设置，避免中文乱码！
import re
f_old = open('dot_data.txt', 'r')
f_new = open('dot_data_new.txt', 'w', encoding='utf-8')
for line in f_old:
    if 'fontname' in line:
         font_re = 'fontname=(.*?)]'
         old_font = re.findall(font_re, line)[0]
         line = line.replace(old_font, 'SimHei')
     f_new.write(line)
f_old.close()
f_new.close()
# 以PNG的图片形式存储生成的可视化文件
os.system('dot -Tpng dot_data_new.txt -o 决策树模型.png')
print('决策树模型.png已经保存在代码所在文件夹！')
# 以PDF的形式存储生成的可视化文件
os.system('dot -Tpdf dot_data_new.txt -o 决策树模型.pdf')
print('决策树模型.pdf已经保存在代码所在文件夹！')