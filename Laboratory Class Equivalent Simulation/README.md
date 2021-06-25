# ※ *Used features of LTspice* ※

## ❄ *Importing Third-Party Intrinsic Models* 

[Reference](https://www.ieee.li/pdf/viewgraphs/ltspice_importing_third_party_models.pdf)

***To import a third-party intrinsic spice model***

1. Download the spice model file from the manufacturer’s website.  Make sure to note the file location on the hard-drive.(save it in a .txt file)
2. Add the following spice directive to the LTspice simulation file 

```
// Edit pull-down menu ---> SPICE Directive):

.include [path(optional)] spicemodel_filename.abc

// if the model is in a .txt file 
.include [path(optional)] spicemodel_filename.txt
```
> ***Important: The file name in the .include statement must match the spice model file name identically! The file name syntax can be anything, just make sure that all of the characters match.***

### Note: An absolute path name <path> can be omitted in the .include directive only if the file is located in:
* <LTspiceIV> \lib\sub 
* The directory that contains the simulation file

---

## ❄ *LTspice: Parametric Plots (Changing independant variable from time to some other variable)*

[Reference](https://www.analog.com/en/technical-articles/ltspice-parametric-plots.html)

***To change the default settings(time variable) of the X-axis:***

1. Click on a node/component to plot its voltage/current in the waveform viewer.
2. Move the cursor to the horizontal axis of the waveform viewer (the cursor will turn into a ruler) and left-click.
3. In the Horizontal Axis dialog, enter an expression for the “Quantity Plotted.
4. Click OK.

---

## ❄ *Measuring values using .meas : output is saved to the *`.log`*  file*

[Reference](https://electronics.stackexchange.com/questions/562475/find-min-and-max-of-magnitude-ltspice)

```
.meas vmax max v(vout)    // find maximum value within the tran time
.meas vmin min v(vout)    // find minimum value within the tran time


.meas vmax find abs(v(vout)) at t1    // if the period of the waveform is known
.meas vmin find abs(v(vout)) at t2    
```
