#优先级的作用
a=2+7*8
#print a

b=9>7
print(b)

#优先级使用实战

#优先级排行榜第1名——函数调用、寻址、下标

#优先级排行榜第2名——幂运算**
a=4*2**3
#print a

#优先级排行榜第3名——翻转运算~

#优先级排行榜第4名——正负号
#print 2+4*-2   #我们可以看，正负号的使用方法是紧挨着操作数的，否则会出错，这就说明正负号优先于加减乘除运算

#优先级排行榜第5名——*、/、%
#print 2+4*2/4

#优先级排行榜第6名——+、-
#print 3<<2+1

#优先级排行榜第7名——<<、>>

#优先级排行榜第8名——按位&、^、|，其实这三个中也是有优先级顺序的，但是他们处于同一级别，故而不细分

#优先级排行榜第9名——比较运算符
a=2*3+5<=5+1*2
#print a


#优先级排行榜第10名——逻辑的not、and、or


#优先级排行榜第11名——lambda表达式
