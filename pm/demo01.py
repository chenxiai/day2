from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import jieba

print('---------------------------one-hot编码--------------------------------')
vt = CountVectorizer()
# 如果是中文,则先要进行jieba分词处理
arr = jieba.cut("什么是one-hot编码?one-hot编码,又称独热编码、一位有效编码。其方法是使用N位状态寄存器来对N个状态进行编码，每个状态都有它独立的寄存器位，并且在任意时候，其中只有一位有效")
# for temp in arr:
#     print(temp)
data = ' '.join(arr)

# 传入要提取的数据
result = vt.fit_transform([data])
print(vt.get_feature_names())
print(result.toarray())

print('---------------------------演示归一化--------------------------------')
mm = MinMaxScaler()
data = mm.fit_transform([[90, 2, 10, 40],
                         [60, 4, 15, 45],
                         [75, 3, 13, 46]])
print(data)
print(mm.inverse_transform(data))

print('---------------------------演示标准化--------------------------------')

std = StandardScaler()
data = std.fit_transform([[90, 2, 10, 40],
                         [60, 4, 15, 45],
                         [75, 3, 13, 46]])
print(std.mean_)
print(data)
print(std.inverse_transform(data))