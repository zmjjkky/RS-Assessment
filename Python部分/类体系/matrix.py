import numpy as np

# ==========================================
# 爸爸：Matrix（普通矩阵类）
# ==========================================
class Matrix:
    
    # 1. __init__ 是“出厂设置”（初始化）
    # 每当我们用 Matrix() 造一个矩阵时，自动执行
    def __init__(self, data):
        # 把传进来的二维列表，转换成 NumPy 矩阵，存入自己的属性 self.data
        self.data = np.array(data)
        
    # 2. 打印技能：当你用 print(m1) 时，自动调用 __str__
    def __str__(self):
        result = ""
        for row in self.data: # 遍历每一行
            result += str(row) + "\n" # 每一行打印完换行
        return result
        
    # 3. 加法技能：重写 __add__，当你写 m1 + m2 时，自动调用
    def __add__(self, other):
        # 把当前矩阵的 data 和另一个矩阵的 data 直接相加
        return Matrix(self.data + other.data)
        
    # 4. 转置技能：行变列，列变行
    def transpose(self):
        # 在 NumPy 里，.T 就是直接转置
        return Matrix(self.data.T)


# ==========================================
# 儿子：SquareMatrix（方阵类）
# 只需要写括号 (Matrix)，就代表继承了爸爸所有技能
# ==========================================
class SquareMatrix(Matrix):
    
    # 1. 出厂设置
    def __init__(self, data):
        # 调用父类的初始化
        super().__init__(data)
        
        # 2. 必须检查形状
        rows, cols = self.data.shape # 获取行数和列数
        if rows != cols:
            raise ValueError("这不是方阵！")
            
    # 3. 算迹
    def trace(self):
        # 迹就是主对角线元素之和
        return np.trace(self.data)
        
    # 4. 判断对称
    def is_symmetric(self):
        # 如果矩阵等于它的转置，就是对称矩阵
        return np.array_equal(self.data, self.data.T)


# ==========================================
# 测试环节（造实物）
# ==========================================
# 1. 造一个普通矩阵 m1
m1 = Matrix([[1, 2], [3, 4]])
print("m1 是：")
print(m1) # 会自动按行打印

# 2. 造一个方阵 sm1
sm1 = SquareMatrix([[1, 2], [2, 3]])
print("sm1 的迹（对角线之和）是：", sm1.trace())
print("sm1 是对称矩阵吗？", sm1.is_symmetric())
