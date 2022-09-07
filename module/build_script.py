import argparse
import os

from cffi import FFI

def main(module_name: str, module_lib: str):
     path = os.path.dirname(os.path.abspath(__file__))
     outdir = "gen"
     
     ffibuilder = FFI()

     with open(os.path.join(path, "declarations.h"), "r") as f:
          ffibuilder.cdef(
               f.read()
               )

     with open(os.path.join(path, "definitions.h"), "r") as f:
          ffibuilder.set_source(
               f"{module_name}_cffi",
               f.read(),
               include_dirs=[os.path.join(path, "inc")],
               library_dirs=[os.path.join(path, "lib")],
               libraries=[f"{module_lib}"]
               )

     ffibuilder.compile(
          tmpdir=outdir,
          target="*",
          verbose=True
          )

     with open("__init__.py", "w") as f:
          f.write(f"from {module_name}.{outdir}.{module_name}_cffi import lib\n")
     
     with open(f"{outdir}/__init__.py", "w") as f:
          pass

if __name__ == "__main__":
     parser = argparse.ArgumentParser()

     parser.add_argument('module_name', action = 'store', type = str)
     parser.add_argument('module_lib', action = 'store', type = str)

     args = parser.parse_args()

     main(args.module_name, args.module_lib)
