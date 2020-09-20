import math
def prob(k, p):
    return (1 - p) ** (k - 1) * p #phan bo hinh hoc
 
def infoMeasure(k, p):
    try:
        return -math.log(prob(k, p), 2.0)
    except ValueError:
        print (prob(k, p))
    return 0.0
 
def sumProb(k, p):
    sumProb = 0
    for i in range (1, k + 1, 1):
        sumProb += prob(i, p)
    return sumProb
 
##Sự xuất hiện của biến cố với một symbol nhất định không ảnh hưởng đến sự xuất hiện của các
##biến cố ứng với những symbol khác. Do vậy ta hoàn toàn có thể dùng hàm sumProb để kiếm chứng
##tổng xác suất của phân bố ngẫu nhiên geometric bằng 1
 
def approxEntropy(k, p):
    sumInfo = 0
    for i in range (1, k + 1, 1):
        sumInfo += infoMeasure (i, p)
    return float(sumInfo) / float(k)
 
##Entropy được tính là tổng lượng tin của tất cả các symbol vì vậy cũng là tổng của p(x) * log(p(x))
##Kiểm chứng bằng hàm approxEntropy ta được kết quả như sau
 
print (sumProb(1000, 0.5)) # được kết quả 0.9990234375 xấp xỉ 1 khi n = 10 và bằng chính xác 1.0 khi n lớn = 1000
print (approxEntropy (1000, 0.5)) #được kết quả 5.5 khi n = 10 và 500.5 khi n lớn = 1000
