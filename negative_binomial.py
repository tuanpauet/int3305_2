import math
def factorial (n):
    if (n <= 1): return 1
    return n * factorial (n - 1)
def C(k, n):
    return factorial(n) / factorial(k) / factorial (n - k)
 
def prob(k, r, p):
    return C(k, k + r - 1) * (p**r) * ((1 - p) ** k)
 
def infoMeasure(k, r, p):
    try:
        return -math.log(prob(k, r, p), 2.0)
    except ValueError:
        print (prob(k, r, p))
    return 0.0
 
def sumProb(k, r, p):
    sumProb = 0
    for i in range (1, k + 1, 1):
        sumProb += prob(i, r, p)
    return sumProb
 
##Sự xuất hiện của biến cố với một symbol nhất định không ảnh hưởng đến sự xuất hiện của các
##biến cố ứng với những symbol khác. Do vậy ta hoàn toàn có thể dùng hàm sumProb để kiếm chứng
##tổng xác suất của phân bố ngẫu nhiên geometric bằng 1
 
def approxEntropy(k, r, p):
    sumInfo = 0
    for i in range (1, k + 1, 1):
        sumInfo += infoMeasure (i, r, p)
    return float(sumInfo) / float(k)
 
##Entropy được tính là tổng lượng tin của tất cả các symbol vì vậy cũng là tổng của p(x) * log(p(x))
##Kiểm chứng bằng hàm approxEntropy ta được kết quả như sau
 
print (sumProb(1000, 3, 0.3)) # được kết quả 0.9729999999999991 xấp xỉ 1 khi n lớn = 1000
print (approxEntropy (1000, 3, 0.3)) #được kết quả 246.66707065607218 khi n lớn = 1000
