Template for compiling and calling C code from python.

seems to work.

Currently only tested with WSL.
`sudo apt install cmake gcc python3-pip` and `python3 -m pip install -r requirements.txt` should do the trick. Then build with the cmake extension in vs code. 

Also currently needs the full path to `module/lib` to be added to `$LD_LIBRARY_PATH`. I'll hopefully find a fix or workaround. `LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/your/project/directory/module/lib`

Put declarations of the stuff you want exposed in `module/declarations.h`, and their implementations in `module/definitions.h`.
Remember to update the cmakelists file if more sourcefiles are added.
