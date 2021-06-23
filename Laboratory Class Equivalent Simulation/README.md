*Importing Third-Party SPICE Models Presented by Thomas Mosteller ADI FAE [full pdf](https://www.ieee.li/pdf/viewgraphs/ltspice_importing_third_party_models.pdf)*

## *Importing Third-Party Intrinsic Models*

### To import a third-party intrinsic spice model

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