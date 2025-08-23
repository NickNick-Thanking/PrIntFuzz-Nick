[+]Build LLVM finished.


[CMD]: git restore .

[CMD]: git checkout v5.18-rc1
HEAD is now at 3123109284176 Linux 5.18-rc1

[CMD]: git apply /home/nick/PrIntFuzz/patch/build_linux_all.patch
/home/nick/PrIntFuzz/patch/build_linux_all.patch:164: trailing whitespace.
//
warning: 1 line adds whitespace errors.
[*]Start to enable driver configurations...
[INFO] output_dir = [/home/nick/PrIntFuzz/build/linux/linux_allmodconfig]
[INFO] config_bak_path = [/home/nick/PrIntFuzz/out/linux_config/linux_x86_64_allmod.config]
./scripts/python/setup.py, 287: entering config_bak_path.exists()...

[CMD]: cp /home/nick/PrIntFuzz/out/linux_config/linux_x86_64_allmod.config /home/nick/PrIntFuzz/build/linux/linux_allmodconfig/.config
[+]Enable driver configuations finished.
[*]Start to build linux allmod...

[CMD]: make ARCH=x86_64  O=/home/nick/PrIntFuzz/build/linux/linux_allmodconfig CROSS_COMPILE= CC=/home/nick/PrIntFuzz/scripts/shell/clang.sh AR=/home/nick/PrIntFuzz/scripts/shell/ar.sh LD=/home/nick/PrIntFuzz/scripts/shell/ld.sh OBJCOPY=/home/nick/PrIntFuzz/scripts/shell/objcopy.sh olddefconfig
make[1]: Entering directory '/home/nick/data-me/github-me/PrIntFuzz-Nick-2/build/linux/linux_allmodconfig'
  GEN     Makefile
#
# configuration written to .config
#
make[1]: Leaving directory '/home/nick/data-me/github-me/PrIntFuzz-Nick-2/build/linux/linux_allmodconfig'

[CMD]: make ARCH=x86_64  O=/home/nick/PrIntFuzz/build/linux/linux_allmodconfig CROSS_COMPILE= CC=/home/nick/PrIntFuzz/scripts/shell/clang.sh AR=/home/nick/PrIntFuzz/scripts/shell/ar.sh LD=/home/nick/PrIntFuzz/scripts/shell/ld.sh OBJCOPY=/home/nick/PrIntFuzz/scripts/shell/objcopy.sh -j10
make[1]: Entering directory '/home/nick/data-me/github-me/PrIntFuzz-Nick-2/build/linux/linux_allmodconfig'
  SYNC    include/config/auto.conf.cmd
  GEN     Makefile
  GEN     Makefile
  DESCEND objtool
  CALL    /home/nick/data-me/github-me/PrIntFuzz-Nick-2/third_party/linux/scripts/atomic/check-atomics.sh
  CALL    /home/nick/data-me/github-me/PrIntFuzz-Nick-2/third_party/linux/scripts/checksyscalls.sh
  CHK     include/generated/compile.h
