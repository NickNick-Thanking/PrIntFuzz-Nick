[CMD]: ln -sf /home/nick/PrIntFuzz/build/llvm/compile_commands.json compile_commands.json
[+]Build LLVM finished.


[CMD]: git restore .

[CMD]: git checkout v5.18-rc1
HEAD is now at 3123109284176 Linux 5.18-rc1

[CMD]: git apply /home/nick/PrIntFuzz/patch/build_linux_all.patch
/home/nick/PrIntFuzz/patch/build_linux_all.patch:164: trailing whitespace.
//
warning: 1 line adds whitespace errors.
[*]Start to enable driver configurations...

[CMD]: make O=/home/nick/PrIntFuzz/build/linux/linux_allmodconfig CC=clang allmodconfig
make[1]: Entering directory '/home/nick/github-nick/PrIntFuzz-Nick/build/linux/linux_allmodconfig'
  GEN     Makefile
  HOSTCC  scripts/basic/fixdep
  HOSTCC  scripts/kconfig/conf.o
  HOSTCC  scripts/kconfig/confdata.o
  HOSTCC  scripts/kconfig/expr.o
  LEX     scripts/kconfig/lexer.lex.c
/bin/sh: 1: flex: not found
make[2]: *** [/home/nick/github-nick/PrIntFuzz-Nick/third_party/linux/scripts/Makefile.host:9: scripts/kconfig/lexer.lex.c] Error 127
make[1]: *** [/home/nick/github-nick/PrIntFuzz-Nick/third_party/linux/Makefile:628: allmodconfig] Error 2
make[1]: Leaving directory '/home/nick/github-nick/PrIntFuzz-Nick/build/linux/linux_allmodconfig'
make: *** [Makefile:219: __sub-make] Error 2
Traceback (most recent call last):
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 580, in <module>
    setup.process()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 573, in process
    component()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 126, in _build_linux_all
    self.__enable_config('allmod')
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 287, in __enable_config
    self._run_cmd(f'make O={output_dir} CC=clang allmodconfig')
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 144, in _run_cmd
    subprocess.run(cmd, shell=True, check=True)
  File "/usr/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'make O=/home/nick/PrIntFuzz/build/linux/linux_allmodconfig CC=clang allmodconfig' returned non-zero exit status 2.