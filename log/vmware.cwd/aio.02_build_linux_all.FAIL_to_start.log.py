[+]Build LLVM finished.


[CMD]: git restore .

[CMD]: git checkout v5.18-rc1
HEAD is now at 3123109284176 Linux 5.18-rc1

[CMD]: git apply /home/nick/data-me/github-me/PrIntFuzz-Nick/patch/build_linux_all.patch
/home/nick/data-me/github-me/PrIntFuzz-Nick/patch/build_linux_all.patch:164: trailing whitespace.
//
warning: 1 line adds whitespace errors.
[*]Start to enable driver configurations...
[INFO] output_dir = [/home/nick/data-me/github-me/PrIntFuzz-Nick/build/linux/linux_allmodconfig]
[INFO] config_bak_path = [/home/nick/data-me/github-me/PrIntFuzz-Nick/out/linux_config/linux_x86_64_allmod.config]
./scripts/python/setup.py, 290: config_bak_path.exists() else...
./scripts/python/setup.py, 295: allmod...

[CMD]: make O=/home/nick/data-me/github-me/PrIntFuzz-Nick/build/linux/linux_allmodconfig CC=clang allmodconfig
make[1]: Entering directory '/home/nick/data-me/github-me/PrIntFuzz-Nick/build/linux/linux_allmodconfig'
  GEN     Makefile
#
# No change to .config
#
make[1]: Leaving directory '/home/nick/data-me/github-me/PrIntFuzz-Nick/build/linux/linux_allmodconfig'
[INFO] args = [namespace(config_file=PosixPath('/home/nick/data-me/github-me/PrIntFuzz-Nick/build/linux/linux_allmodconfig/.config'), config_type='allmod')]
Traceback (most recent call last):
  File "./scripts/python/setup.py", line 592, in <module>
    setup.process()
  File "./scripts/python/setup.py", line 585, in process
    component()
  File "./scripts/python/setup.py", line 128, in _build_linux_all
    self.__enable_config('allmod')
  File "./scripts/python/setup.py", line 308, in __enable_config
    enable_config = utils.EnableConfig(args)
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/scripts/python/utils/enable_config.py", line 10, in __init__
    self.__check()
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/scripts/python/utils/enable_config.py", line 19, in __check
    raise Exception(f"The json file {self.env.config_json} doesn't "
Exception: The json file /home/nick/data-me/github-me/PrIntFuzz-Nick/third_party/linux/config/linux/enable_config.json doesn't exist.
