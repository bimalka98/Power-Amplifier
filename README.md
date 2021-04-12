# Power-Amplifier
All the project files related to the development of a power amplifier, based on a set of given specifications for UOM's EN2110 - Electronics - III Module 🔉 ---->🔊

## Reports

1. [DC Analysis](https://nbviewer.jupyter.org/github/bimalka98/Power-Amplifier/blob/main/01%20DC%20Analysis/Report/A01_180631J.pdf)
2. [AC Analysis](https://nbviewer.jupyter.org/github/bimalka98/Power-Amplifier/blob/main/02%20AC%20Analysis/Report/A02_180631J.pdf)
3. [Power Analysis](https://nbviewer.jupyter.org/github/bimalka98/Power-Amplifier/blob/main/03%20Power%20Analysis/Report/A03_180631J.pdf)
4. [Amplifier Design](https://nbviewer.jupyter.org/github/bimalka98/Power-Amplifier/blob/main/04%20Amplifier%20Design/LaTeX%20Report/A04_180631J.pdf)
5. [DC-DC Converter Analysis](https://nbviewer.jupyter.org/github/bimalka98/Power-Amplifier/blob/main/05%20DC-DC%20Converter%20Analysis/LaTeX%20Report/A05_180631J.pdf)

## AC Analysis

<div class="circuitikz">

(-1,0) to\[sV, l=*v*<sub>*i**n*</sub>\] (-1,6) to\[short, -\*\] (1,6)
to\[R=$R\_{B\_1}\\parallelsum R\_{B\_2}$, v= *v*<sub>*i**n*</sub> \]
(1,0) – (-1,0);

(1,6) to\[short, i&gt;=*i*<sub>*b*<sub>1</sub></sub>\] (4.5,6)
to\[R=*r*<sub>*π*</sub>, v=*v*<sub>*π*</sub>\] (4.5,0) to\[short, -\*\]
(1,0);

(4.5,0) – (7,0);

(7,0) to\[I, l=*g*<sub>*m*</sub>*v*<sub>*π*</sub>, invert\] (7,6)
to\[short, -\*\] (9,6) to\[R=*R*<sub>*C*<sub>1</sub></sub>,
v=*v*<sub>*o*<sub>1</sub></sub>\] (9,0) to\[short,
i&lt;=*i*<sub>*o*<sub>1</sub></sub>\] (7,0);

(6,0) node\[ground\];

(9,6) to\[short, -\*\] (11,6) to \[R=$R\_{B\_3}\\parallelsum R\_{B\_4}$,
v=*v*<sub>*i**n*<sub>2</sub></sub>\] (11,0) to\[short, -\*\] (9,0);

(11,6) to\[short, -\*, i&gt;=*i*<sub>*b*<sub>2</sub></sub>\] (13.5,6)
to\[R=*r*<sub>*e*</sub>, i=*i*<sub>*e*</sub>\] (13.5,3)
to\[R=*R*<sub>*L*</sub>, v=*v*<sub>*O*</sub>\] (13.5,0) to\[short,
-\*\](11,0);

(13.5,6) to\[I, l=*α**i*<sub>*e*</sub>, invert\] (13.5,9)
–(15.5,9)–(15.5,0)–(13.5,0);

(10,8) – (10,-2);

</div>
