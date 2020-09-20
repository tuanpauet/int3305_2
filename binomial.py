import math
def factorial (n):
    if (n <= 1): return 1
    return n * factorial (n - 1)
def C(k, n):
    return factorial(n) / factorial(k) / factorial (n - k)
 
def prob(k, n, p):
    return C(k, n) * (p**k) * ((1-p) ** (n - k))
 
def infoMeasure(k, n, p):
    try:
        return -math.log(prob(k, n, p), 2.0)
    except ValueError:
        return 0.0
 
def sumProb(k, n, p):
    sumProb = 0
    for i in range (1, k + 1, 1):
        sumProb += prob(i, n, p)
    return sumProb
 
##Sự xuất hiện của biến cố với một symbol nhất định không ảnh hưởng đến sự xuất hiện của các
##biến cố ứng với những symbol khác. Do vậy ta hoàn toàn có thể dùng hàm sumProb để kiếm chứng
##tổng xác suất của phân bố ngẫu nhiên geometric bằng 1
 
def approxEntropy(k, n, p):
    sumInfo = 0
    for i in range (1, k + 1, 1):
        sumInfo += infoMeasure (i, n, p)
    return float(sumInfo) / float(k)
 
##Entropy được tính là tổng lượng tin của tất cả các symbol vì vậy cũng là tổng của p(x) * log(p(x))
##Kiểm chứng bằng hàm approxEntropy ta được kết quả như sau
 
print (sumProb(1000, 20, 0.3)) # được kết quả 0.9992020773377486 xấp xỉ 1 khi n lớn = 1000
print (approxEntropy (1000, 20, 0.3)) #được kết quả 64.73289991978544 khi n lớn = 1000
