# 最基础的机器学习与数据挖掘库
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import  StandardScaler
from sklearn.externals import joblib

# 1: 获取数据源
df = pd.read_csv("./data/train.csv")
df.info()
print(df.head())
# 2: 数据清理

# 特征值与目标值,并且区分测试集和训练集
y = df['place_id']
# 删除不必要的特征值,可以提高准确率
X = df.drop(['place_id','row_id','time'],axis=1)

# 3：特征工程 (one-hot、归一、标准化)
std = StandardScaler()
# 理解：此处y为什么可以不用进行标准化
X = std.fit_transform(X)

#  4: 划分测试集和训练集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# 7: 模型的保存与使用
try:
    knn = joblib.load("./data/knn.pkl")
    print('已加载模型,直接测试')
except FileNotFoundError:
    print('还没有模型,应该新建模型')
    knn = KNeighborsClassifier(n_neighbors=10)
    # 传入训练集特征值,和目标值训练模型
    knn.fit(X_train, y_train)
    # 把训练成功的模型进行保存
    joblib.dump(knn, "./data/knn.pkl")

# 根据模型测试数据, 返回测试集的预测值
y_predict = knn.predict(X_test)
print('推荐酒店地址:' , y_predict)
# 通过预测值与真实值比较,可以获取正确率
print('测试得分', knn.score(X_test, y_test))
