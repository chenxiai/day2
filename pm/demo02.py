# 最基础的机器学习与数据挖掘库
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1: 数据的获取(数据库、爬虫、CSV)
# pandas加载csv格式的数据
data = pd.read_csv("./data/movie_test.csv")
# info方法查询数据的相关信息
data.info()
print(data.head(n=3))

# 2: 数据清理 (异常值，缺省值，日期格式化)
# 3: 特征工程 (把大数据映射到0~1过程)
# 4: 把数据划分成训练集与测试集，前提是先划分特征值，和目标值
y = data['type']  # 获取了目标值
# 删除目标值,默认axis=0 代表的是行,axis=1则代表删除列
X = data.drop(["type", 'name'], axis=1)
# 需要传入特征值,目标值,并且对他们进行拆分(默认是0.25)
# X_train: 训练特征值   y_train: 训练的目标值
# X_test: 测试特征值   y_test: 测试的目标值
# random_state 固定测试集与训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
print(X_test)
print(y_test)
# 5：根据需求选择合适的机器学习算法(分类问题才有正确率, 回归问题没有正确率只误差率)
# 采用K近邻完成训练  模型算法是 超参数,超参数会影响到测试正确率和误差
knn = KNeighborsClassifier(n_neighbors=3)
# 传入训练集特征值,和目标值训练模型
knn.fit(X_train, y_train)
# 根据模型测试数据, 返回测试集的预测值
y_predict = knn.predict(X_test)
print('电影类型的预测值:' , y_predict)
# 通过预测值与真实值比较,可以获取正确率
print('测试得分', knn.score(X_test, y_test))
