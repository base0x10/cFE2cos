Using systemtap to trace function calls
=======================================

We can use `stap` to figure out what functions are being called by the cFE. To
do this, first copy the `para-callgraph.stp` script into the `build/exe`
directory. Then from the `build/exe` directory run:
```
sudo stap para-callgraph.stp 'process.function("*")' -c `pwd`/core-cpu1
```

However, this command is not very useful on its own, as it logs way too much
output, and mingles it with the cFE's. That means you're going to have to cut
down on the output of the command, and then also parse its output to eliminate
the parts that you don't care about.

To cut down on output, you either have to modify the script that you are
running, or change which function calls are affected by the script. To modify
the affected functions you have to change the argument to `process.function`.
For example to only get `stap` output about information about the function `foo`
you could use this command:
```
sudo stap para-callgraph.stp 'process.function("foo")' -c `pwd`/core-cpu1
```

Or to only output information about functions with names starting with `bar`,
you could use this command:
```
sudo stap para-callgraph.stp 'process.function("bar*")' -c `pwd`/core-cpu1
```

To eliminate output from the cFE itself, and instead just see the information
printed by the base script, `grep` is your friend:
```
sudo stap para-callgraph.stp 'process.function("*")' -c `pwd`/core-cpu1 | grep -e core-cpu1
```
(Of course, this won't necessarily work if you've written your own script to
replace `para-callgraph.stp`)

One example of all these concepts in action is this command, which prints the
name of a `OS_` function the first time it is called:
```
sudo stap para-callgraph.stp 'process.function("OS_*")' -c `pwd`/core-cpu1 | grep -o 'OS_\w*' | awk '!seen[$0]++'
```
