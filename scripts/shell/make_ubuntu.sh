#!/bin/bash

source ./common.sh

set -eux

mkdir -p "$BUILDDIR"
pushd "$BUILDDIR" > /dev/null

DIR=debian
PREINSTALL_PKGS=gdb,net-tools,openssh-server,curl,tar,gcc,libc6-dev,time,\
strace,sudo,cmake,make,git,vim,tmux,usbutils,tcpdump,pciutils,tree,i2c-tools,\
lsscsi
RELEASE=stretch
MIRROR_tsinghua_debian_elts=https://mirrors.tuna.tsinghua.edu.cn/debian-elts
MIRROR_tsinghua_debian=https://mirrors.tuna.tsinghua.edu.cn/debian
MIRROR_archive_debian=http://archive.debian.org/debian # archive.debian.org 不支持 HTTPS

sudo rm -rf $DIR
sudo mkdir -p $DIR
sudo chmod 0755 $DIR
# sudo debootstrap --include=$PREINSTALL_PKGS --components=main $RELEASE $DIR https://mirrors.tuna.tsinghua.edu.cn/debian-elts
# sudo debootstrap --include=$PREINSTALL_PKGS --components=main $RELEASE $DIR https://mirrors.tuna.tsinghua.edu.cn/debian # 依然失败，见 "vmware.HOME/aio.07.FAILED__2.log.py"
sudo debootstrap --include=$PREINSTALL_PKGS --components=main $RELEASE $DIR $MIRROR_debian



popd > /dev/null
