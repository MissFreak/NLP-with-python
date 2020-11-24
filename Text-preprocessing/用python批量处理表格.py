# 老爸工作中经常使用Excel，今天用python帮他批量合并Excel表格。

```python
import pandas as pd
import os

#文件路径
file_dir = "your path"
#找到文件路径下的所有表格名称，返回列表
file_list = os.listdir(file_dir)

#创建一个空dataframe
df=pd.DataFrame()

for one_file in file_list:
    #重构文件路径
    file_path = os.path.join(file_dir,one_file)
    try:
        #将excel sheet读取到DataFrame，去掉表头和表尾的注释，只留下columns and rows
        dataframe = pd.read_excel(file_path, skiprows=1, skipfooter=1, sheet_name="sheet name")
        #去掉空白的行
        dataframe = dataframe.dropna(how="all")
        #加入到空df中
        df = pd.concat([df, dataframe])
        #有些文件可能损坏，无法读取
    except:
        print("cannot read" + one_file)

#写入到一个新excel表中，去掉index
df.to_excel("new_file.excel",index=False)
```
