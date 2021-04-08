Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def parallel(r1,r2):
	return (r1*r2)/(r1+r2)

>>> parallel(10,10)
5.0
>>> rb3 = 5.5338
>>> rb4 = 60.15
>>> parallel(rb3,rb4)
5.067582417582417
>>> b = (400+1)*(16+0.0267)
>>> parallel(parallel(rb3,rb4),b)
5.063589679275479
>>> parallel(parallel(rb3,rb4)*1000,b)
2833.3953968550504
>>> b
6426.706700000001
>>> rb3 = 5.53
>>> rb4 = 60.15
>>> parallel(parallel(rb3,rb4)*1000,b)
2832.398852576494
>>> 120/0.9983
120.20434739056397
>>> parallel(2833.3954,3712.7730)
1607.0093674101324
>>> 120.2043/0.0748
1607.00935828877
>>> 