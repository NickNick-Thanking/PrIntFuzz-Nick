In file included from /home/nick/github-nick/PrIntFuzz-Nick/third_party/llvm/llvm/lib/Support/Signals.cpp:250:
/home/nick/github-nick/PrIntFuzz-Nick/third_party/llvm/llvm/lib/Support/Unix/Signals.inc:348:44: error: ‘void llvm::sys::CleanupOnSignal(uintptr_t)’ should have been declared inside ‘llvm::sys’
  348 | void sys::CleanupOnSignal(uintptr_t Context) {
      |                                            ^
[160/5094] Building CXX object lib/TableGen/CMakeFiles/LLVMTableGen.dir/Record.cpp.o
ninja: build stopped: subcommand failed.
Traceback (most recent call last):
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 580, in <module>
    setup.process()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 573, in process
    component()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 157, in __build_llvm
    self._run_cmd(f'cmake --build {self.env.llvm_build_dir}')
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 144, in _run_cmd
    subprocess.run(cmd, shell=True, check=True)
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'cmake --build /home/nick/PrIntFuzz/build/llvm' returned non-zero exit status 1.
