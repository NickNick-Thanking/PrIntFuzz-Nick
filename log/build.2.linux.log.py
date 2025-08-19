####


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


### 
sudo apt install debootstrap

zkaller/prog.gitRevisionDate=20220217-141201'" "-tags=syz_target syz_os_linux syz_arch_amd64 " -o ./bin/linux_amd64/syz-stress github.com/google/syzkaller/tools/syz-stress
mkdir -p ./bin/linux_amd64
gcc -o ./bin/linux_amd64/syz-executor executor/executor.cc \
        -m64 -O2 -pthread -Wall -Werror -Wparentheses -Wunused-const-variable -Wframe-larger-than=16384 -Wno-stringop-overflow -Wno-array-bounds -Wno-format-overflow -static-pie  -DGOOS_linux=1 -DGOARCH_amd64=1 \
        -DHOSTGOOS_linux=1 -DGIT_REVISION=\"3cd800e43d452c348a66ba475143831d94969a24+\"
[+]Build syzkaller finished.
[*]Start to create image...

[CMD]: bash make_ubuntu.sh
+ mkdir -p /home/nick/github-nick/PrIntFuzz-Nick/out/build
+ pushd /home/nick/github-nick/PrIntFuzz-Nick/out/build
+ DIR=debian
+ PREINSTALL_PKGS=gdb,net-tools,openssh-server,curl,tar,gcc,libc6-dev,time,strace,sudo,cmake,make,git,vim,tmux,usbutils,tcpdump,pciutils,tree,i2c-tools,lsscsi
+ RELEASE=stretch
+ sudo rm -rf debian
[sudo] password for nick:
+ sudo mkdir -p debian
+ sudo chmod 0755 debian
+ sudo debootstrap --include=gdb,net-tools,openssh-server,curl,tar,gcc,libc6-dev,time,strace,sudo,cmake,make,git,vim,tmux,usbutils,tcpdump,pciutils,tree,i2c-tools,lsscsi --components=main stretch debian https://mirrors.tuna.tsinghua.edu.cn/debian-elts
sudo: debootstrap: command not found
Traceback (most recent call last):
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 580, in <module>
    setup.process()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 573, in process
    component()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 496, in __create_image
    self._create_x86_image()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 468, in _create_x86_image
    self._run_cmd('bash make_ubuntu.sh')
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 144, in _run_cmd
    subprocess.run(cmd, shell=True, check=True)
  File "/usr/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'bash make_ubuntu.sh' returned non-zero exit status 1.