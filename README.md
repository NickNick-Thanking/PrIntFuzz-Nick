# PrIntFuzz: Fuzzing Linux Drivers via Automated Virtual Device Simulation

## 0. Introduction

PrIntFuzz is an efficient and universal fuzzing framework that can test the Linux driver code, include the PRobing code and INTerrupt handlers.

The following instructions guide you to set up the fuzzing environment and perform multi-dimension fuzzing on various device drivers. 

Tested on Ubuntu 20.04.1.

## 1. Setup

### Init submodules
```bash
git submodule update --init --progress
```

### 设置工作区
Init Env
```bash
chmod u+x ./setHostEnv.sh
./setHostEnv.sh
```

Init workdir
- ~~默认工作目录是 `~/PrintFuzz`，所以必须创建连接： `ln -s ${HOME_PrIntFuzz}/ ~/PrIntFuzz`~~
- 已经修改代码可以使用 `Path.cwd()` 作为 `env.project_dir`，不需要在创建连接

`flag_use_cwd = True`
```bash
cd ${WORKDIR_PrIntFuzz}
cd ~/data-me/github-me/PrIntFuzz-Nick
```

`flag_use_cwd = False`
- 给目录创建软连接时，不要在目录后面添加 `/`
```
rm ~/PrIntFuzz
ln -s ~/data-me/github-me/PrIntFuzz-Nick-2 ~/PrIntFuzz
cd ~/PrIntFuzz
```

python3 venv
```bash
# 后续激活
cd ${WORKDIR_PrIntFuzz}
source venv/bin/activate
```
```bash
# 第一次/重建
cd ${WORKDIR_PrIntFuzz}
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```
```bash
# 退出
deactivate
```
```bash
# 安装 python3 和 pip3
sudo apt-get install -y python3-venv python3-pip
```

## 1.1 Prerequisite
```bash
cd ${WORKDIR_PrIntFuzz}
```

### Python3 dependencies
Please install the following python package:

```python
pip3 install kconfiglib==14.1.0 GitPython requests 
```

### Build dependencies
Linux dependencies
- build-essential: 包括 gcc, g++, make, 标准头文件等必要开发工具

```bash
sudo apt install -y git gcc make cmake
sudo apt install -y ninja-build build-essential
sudo apt install -y bc flex bison fakeroot debootstrap dwarves ncurses-dev binutils-dev xz-utils libssl-dev libelf-dev libdw-dev libunwind-dev libslang2-dev

#5.13之后支持zstd压缩
sudo apt install -y zstd 

sudo apt install -y qemu-utils qemu-system-x86 virtinst libvirt-clients libvirt-daemon-system
```

## 1.2 Build

Re-build 需要删除 build 和 out
```
rm -rf build out
```

### 1.2.1 Use one click script

```bash
python3 ./scripts/python/setup.py
```

### 1.2.2 Step by step

1. Build the LLVM
    
    ```bash
    python3 ./scripts/python/setup.py --build_llvm
    ```
    
2. Build the Linux kernel with `allmodconfig`
    
    ```bash
    python3 ./scripts/python/setup.py --build_linux_all
    ```
    
3. Build the static analyzer
    
    ```bash
    python3 ./scripts/python/setup.py --build_analyzer
    ```
    
4. Perform static analysis
    
    ```bash
    python3 ./scripts/python/setup.py --analyze
    ```
    
5. Build the syzkaller
    
    ```bash
    python3 ./scripts/python/setup.py --build_syz
    ```
    
6. Build the Linux kernel for fuzzing
    
    ```bash
    python3 ./scripts/python/setup.py --build_linux_fuzz
    ```
    
7. Build the disk image for fuzzing
    
    ```bash
    python3 ./scripts/python/setup.py --create_image # --build_image
    ```
    
8. Build the Linux kernel for fault injection
    
    ```bash
    python3 ./scripts/python/setup.py --build_linux_fault
    ```
    
9. Build the qemu with fake devices
    
    ```bash
    python3 ./scripts/python/setup.py --build_qemu
    ```
    
10. Build the docker image for fuzzing
    
    ```bash
    python3 ./scripts/python/setup.py --create_docker
    ```
    

## 2. Patch the host’s KVM module

1. Get the source code of the current kernel
    
    ```bash
    sudo apt-get source linux-image-unsigned-$(uname -r)
    ```
    
2. Patch the kernel’s KVM module
    
    ```bash
    sudo patch -p1 < ./patch/linux_host.patch (for Linux 5.13)
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
    python3 ./scripts/python/qemu.py -m fuzz -e drivers_atm_he
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
python3 ./scripts/python/evaluation/probe.py -t PCI
```

Drivers that match successfully are in the `./out/probe/success/pci`, drivers that fail to match are in the `./out/probe/fail/pci` directory, and drivers that cause system crashes are in the `./out/probe/crash` directory.

Each driver has a separate folder where the relevant logs are stored, and we can check the logs to determine if the driver is crashing the kernel.

## 5. Perform fuzzing on drivers

```bash
python3 ./scripts/python/evaluation/fuzz.py
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
