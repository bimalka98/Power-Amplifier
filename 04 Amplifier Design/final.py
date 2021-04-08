Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> vcc = 24
>>> rl = 16
>>> ie2 = vcc/(2*rl)
>>> ie2
0.75
>>> beta2 = 400
>>> alpa2 = beta2/(beta2+1)
>>> alpa2
0.9975062344139651
>>> ic2 = alpha2*ie2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ic2 = alpha2*ie2
NameError: name 'alpha2' is not defined
>>> ic2 = alpa2*ie2
>>> ic2
0.7481296758104738
>>> ic2/(20*10**(-3))
37.406483790523694
>>> gm2 = ic2/(20*10**(-3))
>>> gm2
37.406483790523694
>>> re2 = alpa2/gm2
>>> re2
0.026666666666666665
>>> av2 = rl/(rl+re2)
>>> av2
0.9983361064891847
>>> ib2 = ic2/beta2
>>> ib2
0.0018703241895261847
>>> rb4 = 12.5/(ib2/9)
>>> rb4
60149.99999999999
>>> rb3 = (24-12.5)/(10/9*ib2)
>>> rb3
5533.8
>>> def pl(r1,r2):
	return (r1*r2)/(r1+r2)

>>> pl(pl(rb3,rb4),((beta2+1)*(re2+rl)))
2833.3927987241354
>>> ic1= ic2/500
>>> ic1
0.0014962593516209476
>>> gm1 = ic1/(20*10**(-3))
>>> gm1
0.07481296758104738
>>> av = 120
>>> av1 = av/av2
>>> av1
120.2
>>> av1/gm1
1606.6733333333334
>>> rin2 = pl(pl(rb3,rb4),((beta2+1)*(re2+rl)))
>>> rin2
2833.3927987241354
>>> rc1 = 3712.7730 # Calculated manually
>>> pl(rc1,rin2)
1607.0085306344868
>>> 1607.0085306344868-1606.6733333333334
0.33519730115335733
>>> beta1 = 100
>>> re1 = (beta1/(beta1+1))*((12-ic1*rc1)/(ic1))
>>> re1
4264.581188118812
>>> ib1 = ic1/beta1
>>> ib1
1.4962593516209477e-05
>>> ie1 = ib1+ic1
>>> ie1
0.0015112219451371572
>>> rb2 = (0.6+ie1*re1)/(ib1/9)
>>> rb2
4237404.3
>>> rb1 = (24-(0.6+ie1*re1))/(10*ib1/9)
>>> rb1
1019859.5700000002
>>> import math
>>> vp = sqrt(4*2*16)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    vp = sqrt(4*2*16)
NameError: name 'sqrt' is not defined
>>> vp = math.sqrt(4*2*16)
>>> vp
11.313708498984761
>>> vin = vp/120
>>> vin
0.09428090415820635
>>> vp2 = 85*10**(-3)*120
>>> vp2
10.200000000000001
>>> vp2**2/vcc**2
0.18062500000000004
>>> 