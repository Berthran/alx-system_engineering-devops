## Shebang
- The shebang directive is the first line in any Linux shell script. It starts with a character sequence consisting of a hash followed by an exclamation mark (#!).
- The shebang line has the following syntax:
    * #!/path/to/interpreter arg1
    * #! /path/to/interpreter arg1 arg2
- The presence of a shebang indicates that a file is executable. When the shebang line is missing, #!/bin/bash is the default shell used to execute the file.

## Types of Shebang
1. _#!/bin/bash_
- When we use this line, it tells the system we want to use bash in the /bin directory.

Pros:
* Full path gives more precision to interpreter.
* Increased operability with the use of flags. _#!/bin/bash -v_ _#!_/bin/bash --_
* Suitable for cron jobs due to restricted environment
Cons:
* The _bash_ interpreter fails to run in systems where *bash* is not in the _/bin_ directory. 

2. _#!/usr/bin/env name_
Linux has various distros, and in some of them, the Shell is in different location. Also, users mighy want to use their customized shells in different locations to run scripts.
How the _env_ command works
===========================
* When we run bash with the env command, env searches for */bash in our $PATH environment variable and runs the first instance it finds. 

Pros:
- Script portability: ability for a script to run scripts across UNIX-like systems without breaking.
- Useful when the absolute path of interpreter is unknown.
Cons:
- Inconsistent result: results are based on which shell runs.
- Doesn’t accept passed arguments to the interpreter.
- Unsuitable for cron jobs
