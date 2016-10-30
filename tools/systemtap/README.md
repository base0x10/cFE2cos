Using systemtap to trace function calls
=======================================

We can use `stap` to figure out what functions are being called by the cFE. To
do this, first copy the `para-callgraph.stp` script into the `build/exe`
directory. Then from the `build/exe` directory run:
```
sudo stap para-callgraph.stp "process.function(\"*\")" -c `pwd`/core-cpu1
```

To eliminate output from the cFE itself, and instead just see function calls,
then you can pipe the output of the command to `grep`:
```
sudo stap para-callgraph.stp "process.function(\"*\")" -c `pwd`/core-cpu1 | grep -e core-cpu1
```
