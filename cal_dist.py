from numpy import *

#两点间欧氏距离
def twopt_dist(a, b):
    d = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return d


# print('a,b 二维欧式距离：', twopt_dist((1, 1), (1, 2)))

#多维欧氏距离
def euc_dist(a, b):
    dissum = 0
    for i in range(len(a)):
        dissum += (a[i]-b[i])**2
    dissum = sqrt(dissum)
    return  dissum


# print('a,b 多维距离： ', euc_dist((1,1,1,1), (2,2,2,2)))

#多维标准欧氏距离，标准差si
def std_euc_dist(a, b):
    dissum = 0;
    for i in range(len(a)):
        # avg均指  si标准差
        avg = (a[i]-b[i])/2
        si = sqrt((a[i]-avg)**2+(b[i]-avg)**2)
        dissum += ((a[i]-b[i])/si)**2
    dissum = sqrt(dissum)
    return dissum


#print("a, b 多维距离： ",std_euc_dist((1,1,1,1), (2,2,2,2)))

#多维街区距离,曼哈顿距离
def block_dist(a, b):
    dissum = 0
    for i in range(len(a)):
        dissum += abs(a[i]-b[i])
    return  dissum


# print("多维曼哈顿距离： ", block_dist((1,1,1),(2,2,2)))

#多维切比雪夫距离
def cheb_dist(a, b):
    maxdis = 0
    for i in range(len(a)):
        if abs(a[i]-b[i]) > maxdis:
            maxdis = abs(a[i]-b[i])
    return maxdis


# print("多维切比雪夫距离：", cheb_dist((1,2,3), (10,10,10)))

#多维向量的夹角余弦相似度
def cos_sim(a, b):
    sumdot = 0.0
    norm_a, norm_b = 0, 0
    for i in range(len(a)):
        sumdot += a[i]*b[i]
        norm_a += a[i]**2
        norm_b += b[i]**2
    return sumdot/(sqrt(norm_b*norm_b))


#print("多维向量的夹角余弦相似度: ", cos_sim((1,1), (-1,-1)))

# 汉明距离
def ham_dist(a, b):
    dissum = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dissum += 1
    return dissum


print("汉明距离: ", ham_dist((1,1,1,1),(1,2,3,1)))