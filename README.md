# PrIntFuzz: Fuzzing Linux Drivers via Automated Virtual Device Simulation

## 0. Introduction

PrIntFuzz is an efficient and universal fuzzing framework that can test the Linux driver code, include the PRobing code and INTerrupt handlers.

The following instructions guide you to set up the fuzzing environment and perform multi-dimension fuzzing on various device drivers. 

Tested on Ubuntu 20.04.1.

## 1. Setup
### 设置工作区
Init Env
```
chmod u+x ./setHostEnv.sh
./setHostEnv.sh
```

Init workdir
```
rm ~/PrIntFuzz
ln -s ${HOME_PrIntFuzz}/ ~/PrIntFuzz
# export WORKDIR_PrIntFuzz=~/PrIntFuzz
```

Init submodules
```
git submodule update --init --progress
```

python3 venv
```
cd ${WORKDIR_PrIntFuzz}
source venv/bin/activate
```
```
cd ${WORKDIR_PrIntFuzz}
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```
```
deactivate
```

## 1.1 Prerequisite

### Python3 dependencies
Please install the following python package:

```bash
pip3 install kconfiglib==14.1.0
pip3 install GitPython
```

More python3 dependencies
```
pip3 install requests
```

### Build dependencies
安装 python3 和 pip3
```
sudo apt-get install python3-venv python3-pip
```

Linux dependencies
- build-essential: 包括 gcc, g++, make, 标准头文件等必要开发工具

LLVM Clang 14
```
## 从 LLVM 官方仓库 添加软件源，才能安装 Clang 14
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | sudo apt-key add -
sudo apt-add-repository "deb http://apt.llvm.org/focal/ llvm-toolchain-focal-14 main"

## 安装 Clang-14
sudo apt update
sudo apt install clang-14

## 安装配套工具
sudo apt install clangd-14         # 用于语言服务器（编辑器支持）
sudo apt install clang-tools-14    # 包含 clang-format, clang-tidy 等
sudo apt install lld-14            # LLVM 的链接器

## （可选）设置 clang 命令默认指向 clang-14
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-14 100
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-14 100
clang --version
```

```
sudo apt install ninja-build build-essential cmake

## 编译 Linux 安装缺失的工具（核心是 flex）
sudo apt install flex bison

# 推荐安装完整内核构建依赖
sudo apt install build-essential libssl-dev libncurses-dev libelf-dev bc \
                 libdw-dev libunwind-dev libslang2-dev binutils-dev
```

## 1.2 Build

### 1.2.1 Use one click script

```bash
python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py
```

### 1.2.2 Step by step

1. Build the LLVM
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_llvm
    ```
    
2. Build the Linux kernel with `allmodconfig`
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_linux_all
    ```
    
3. Build the static analyzer
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_analyzer
    ```
    
4. Perform static analysis
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --analyze
    ```
    
5. Build the syzkaller
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_syz
    ```
    
6. Build the Linux kernel for fuzzing
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_linux_fuzz
    ```
    
7. Build the disk image for fuzzing
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_image
    ```
    
8. Build the Linux kernel for fault injection
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_linux_fault
    ```
    
9. Build the qemu with fake devices
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --build_qemu
    ```
    
10. Build the docker image for fuzzing
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/setup.py --create_docker
    ```
    

## 2. Patch the host’s KVM module

1. Get the source code of the current kernel
    
    ```bash
    sudo apt-get source linux-image-unsigned-$(uname -r)
    ```
    
2. Patch the kernel’s KVM module
    
    ```bash
    sudo patch -p1 < ${WORKDIR_PrIntFuzz}/patch/linux_host.patch (for Linux 5.13)
    ```
    
3. Build and install the kernel
    
    ```bash
    make olddefconfig
    make
    make INSTALL_MOD_STRIP=1 modules_install
    make install
    ```
    
4. Change the default kernel to boot, then reboot and ensure that the kernel is new.
    
    [WARNING]: This operation will change your default kernel, please back up your data first!
    

## 3. Test the environment

1. Boot the virtual machine with a virtual device (`-e`)
    
    ```bash
    python3 ${WORKDIR_PrIntFuzz}/scripts/python/qemu.py -m fuzz -e drivers_atm_he
    ```
    
2. Check whether the driver is loaded
    
    ```bash
    lspci -k
    ```
    
    The result shows that
    
    ```bash
    00:05.0 Unassigned class [ffff]: FORE Systems Inc ForeRunnerHE ATM Adapter
            Kernel driver in use: he
    ```
    
    This indicates that the virtual device is matched with the `he` driver successfully.
    

## 4. Perform fault Injection Test

```bash
python3 ${WORKDIR_PrIntFuzz}/scripts/python/evaluation/probe.py -t PCI
```

Drivers that match successfully are in the `${WORKDIR_PrIntFuzz}/out/probe/success/pci`, drivers that fail to match are in the `${WORKDIR_PrIntFuzz}/out/probe/fail/pci` directory, and drivers that cause system crashes are in the `${WORKDIR_PrIntFuzz}/out/probe/crash` directory.

Each driver has a separate folder where the relevant logs are stored, and we can check the logs to determine if the driver is crashing the kernel.

## 5. Perform fuzzing on drivers

```bash
python3 ${WORKDIR_PrIntFuzz}/scripts/python/evaluation/fuzz.py
```

```bash
optional arguments:
  -h, --help       show this help message and exit
  -i, --interrupt  Use this option to enable the interrupt syscall
  -s, --syscall    Use this option to enable other syscalls
  -t, --test       Use this option to add "test" to the output dir
  -d, --debug      Use this option to debug the setting of experiment
  -f, --fake       Use this option to enable fake devices
```

## 6. Cite our work

```
@inproceedings{ma2022printfuzz,
  title={PrIntFuzz: fuzzing Linux drivers via automated virtual device simulation},
  author={Ma, Zheyu and Zhao, Bodong and Ren, Letu and Li, Zheming and Ma, Siqi and Luo, Xiapu and Zhang, Chao},
  booktitle={Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis},
  pages={404--416},
  year={2022}
}
```
