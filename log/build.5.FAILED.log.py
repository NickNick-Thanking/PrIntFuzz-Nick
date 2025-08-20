[+]Analyze statically finished.
[+]Analyze llvm bitcode files finished.
[*]Start to generate the configurations for syzkaller...
[*]Generate the configurations for syzkaller finished.
[*]Start to build syzkaller...

[CMD]: git checkout 3cd800e43
M       .gitignore
M       executor/common_linux.h
M       executor/executor.cc
M       pkg/csource/generated.go
M       pkg/host/syscalls_linux.go
M       prog/generation.go
M       prog/minimization.go
M       prog/mutation.go
M       prog/prog.go
M       prog/rand.go
M       sys/linux/dev_fb.txt
M       sys/linux/filesystem.txt
M       sys/linux/socket.txt
M       sys/linux/test/80211_ibss
M       sys/linux/test/80211_scan
M       sys/linux/test/80211_setup_ap
M       sys/linux/test/80211_setup_mesh
M       sys/linux/test/80211_setup_station
M       sys/linux/test/binder
M       sys/linux/test/binfmt
M       sys/linux/test/bpf_cgroup
M       sys/linux/test/btf_id
M       sys/linux/test/can
M       sys/linux/test/caps
M       sys/linux/test/cgroup
M       sys/linux/test/dev_bifrost
M       sys/linux/test/exit0
M       sys/linux/test/exit1
M       sys/linux/test/fd_assignment
M       sys/linux/test/file
M       sys/linux/test/file_immutable
M       sys/linux/test/fscrypt_ext4
M       sys/linux/test/fscrypt_f2fs
M       sys/linux/test/fuse_deadlock
M       sys/linux/test/fuse_getdents64
M       sys/linux/test/gup_fast
M       sys/linux/test/io_uring
M       sys/linux/test/ipc
M       sys/linux/test/landlock_fs_accesses
M       sys/linux/test/landlock_fs_forbidden
M       sys/linux/test/landlock_layers
M       sys/linux/test/landlock_ptrace
M       sys/linux/test/landlock_sb_delete
M       sys/linux/test/mmap
M       sys/linux/test/netrom
M       sys/linux/test/pipe
M       sys/linux/test/rfkill
M       sys/linux/test/syz_clone
M       sys/linux/test/syz_clone3
M       sys/linux/test/syz_fuse_handle_req
M       sys/linux/test/syz_genetlink_get_family_id
M       sys/linux/test/syz_kvm_setup_cpu_ppc64le
M       sys/linux/test/syz_mount_image
M       sys/linux/test/syz_mount_image_bfs_0
M       sys/linux/test/syz_mount_image_bfs_1
M       sys/linux/test/syz_mount_image_bfs_2
M       sys/linux/test/syz_mount_image_btrfs_0
M       sys/linux/test/syz_mount_image_btrfs_1
M       sys/linux/test/syz_mount_image_btrfs_10
M       sys/linux/test/syz_mount_image_btrfs_11
M       sys/linux/test/syz_mount_image_btrfs_12
M       sys/linux/test/syz_mount_image_btrfs_13
M       sys/linux/test/syz_mount_image_btrfs_14
M       sys/linux/test/syz_mount_image_btrfs_15
M       sys/linux/test/syz_mount_image_btrfs_16
M       sys/linux/test/syz_mount_image_btrfs_17
M       sys/linux/test/syz_mount_image_btrfs_18
M       sys/linux/test/syz_mount_image_btrfs_19
M       sys/linux/test/syz_mount_image_btrfs_2
M       sys/linux/test/syz_mount_image_btrfs_20
M       sys/linux/test/syz_mount_image_btrfs_21
M       sys/linux/test/syz_mount_image_btrfs_22
M       sys/linux/test/syz_mount_image_btrfs_23
M       sys/linux/test/syz_mount_image_btrfs_24
M       sys/linux/test/syz_mount_image_btrfs_25
M       sys/linux/test/syz_mount_image_btrfs_26
M       sys/linux/test/syz_mount_image_btrfs_27
M       sys/linux/test/syz_mount_image_btrfs_28
M       sys/linux/test/syz_mount_image_btrfs_29
M       sys/linux/test/syz_mount_image_btrfs_3
M       sys/linux/test/syz_mount_image_btrfs_30
M       sys/linux/test/syz_mount_image_btrfs_31
M       sys/linux/test/syz_mount_image_btrfs_32
M       sys/linux/test/syz_mount_image_btrfs_33
M       sys/linux/test/syz_mount_image_btrfs_34
M       sys/linux/test/syz_mount_image_btrfs_35
M       sys/linux/test/syz_mount_image_btrfs_36
M       sys/linux/test/syz_mount_image_btrfs_37
M       sys/linux/test/syz_mount_image_btrfs_38
M       sys/linux/test/syz_mount_image_btrfs_39
M       sys/linux/test/syz_mount_image_btrfs_4
M       sys/linux/test/syz_mount_image_btrfs_40
M       sys/linux/test/syz_mount_image_btrfs_41
M       sys/linux/test/syz_mount_image_btrfs_42
M       sys/linux/test/syz_mount_image_btrfs_43
M       sys/linux/test/syz_mount_image_btrfs_44
M       sys/linux/test/syz_mount_image_btrfs_45
M       sys/linux/test/syz_mount_image_btrfs_46
M       sys/linux/test/syz_mount_image_btrfs_47
M       sys/linux/test/syz_mount_image_btrfs_48
M       sys/linux/test/syz_mount_image_btrfs_49
M       sys/linux/test/syz_mount_image_btrfs_5
M       sys/linux/test/syz_mount_image_btrfs_50
M       sys/linux/test/syz_mount_image_btrfs_51
M       sys/linux/test/syz_mount_image_btrfs_52
M       sys/linux/test/syz_mount_image_btrfs_53
M       sys/linux/test/syz_mount_image_btrfs_54
M       sys/linux/test/syz_mount_image_btrfs_55
M       sys/linux/test/syz_mount_image_btrfs_56
M       sys/linux/test/syz_mount_image_btrfs_57
M       sys/linux/test/syz_mount_image_btrfs_58
M       sys/linux/test/syz_mount_image_btrfs_59
M       sys/linux/test/syz_mount_image_btrfs_6
M       sys/linux/test/syz_mount_image_btrfs_60
M       sys/linux/test/syz_mount_image_btrfs_61
M       sys/linux/test/syz_mount_image_btrfs_62
M       sys/linux/test/syz_mount_image_btrfs_63
M       sys/linux/test/syz_mount_image_btrfs_64
M       sys/linux/test/syz_mount_image_btrfs_65
M       sys/linux/test/syz_mount_image_btrfs_66
M       sys/linux/test/syz_mount_image_btrfs_67
M       sys/linux/test/syz_mount_image_btrfs_68
M       sys/linux/test/syz_mount_image_btrfs_69
M       sys/linux/test/syz_mount_image_btrfs_7
M       sys/linux/test/syz_mount_image_btrfs_70
M       sys/linux/test/syz_mount_image_btrfs_71
M       sys/linux/test/syz_mount_image_btrfs_72
M       sys/linux/test/syz_mount_image_btrfs_73
M       sys/linux/test/syz_mount_image_btrfs_74
M       sys/linux/test/syz_mount_image_btrfs_75
M       sys/linux/test/syz_mount_image_btrfs_76
M       sys/linux/test/syz_mount_image_btrfs_77
M       sys/linux/test/syz_mount_image_btrfs_78
M       sys/linux/test/syz_mount_image_btrfs_79
M       sys/linux/test/syz_mount_image_btrfs_8
M       sys/linux/test/syz_mount_image_btrfs_9
M       sys/linux/test/syz_mount_image_cramfs_0
M       sys/linux/test/syz_mount_image_cramfs_1
M       sys/linux/test/syz_mount_image_cramfs_2
M       sys/linux/test/syz_mount_image_cramfs_3
M       sys/linux/test/syz_mount_image_efs_0
M       sys/linux/test/syz_mount_image_efs_1
M       sys/linux/test/syz_mount_image_efs_10
M       sys/linux/test/syz_mount_image_efs_11
M       sys/linux/test/syz_mount_image_efs_12
M       sys/linux/test/syz_mount_image_efs_13
M       sys/linux/test/syz_mount_image_efs_2
M       sys/linux/test/syz_mount_image_efs_3
M       sys/linux/test/syz_mount_image_efs_4
M       sys/linux/test/syz_mount_image_efs_5
M       sys/linux/test/syz_mount_image_efs_6
M       sys/linux/test/syz_mount_image_efs_7
M       sys/linux/test/syz_mount_image_efs_8
M       sys/linux/test/syz_mount_image_efs_9
M       sys/linux/test/syz_mount_image_erofs_0
M       sys/linux/test/syz_mount_image_erofs_1
M       sys/linux/test/syz_mount_image_erofs_10
M       sys/linux/test/syz_mount_image_erofs_11
M       sys/linux/test/syz_mount_image_erofs_12
M       sys/linux/test/syz_mount_image_erofs_13
M       sys/linux/test/syz_mount_image_erofs_14
M       sys/linux/test/syz_mount_image_erofs_15
M       sys/linux/test/syz_mount_image_erofs_2
M       sys/linux/test/syz_mount_image_erofs_3
M       sys/linux/test/syz_mount_image_erofs_4
M       sys/linux/test/syz_mount_image_erofs_5
M       sys/linux/test/syz_mount_image_erofs_6
M       sys/linux/test/syz_mount_image_erofs_7
M       sys/linux/test/syz_mount_image_erofs_8
M       sys/linux/test/syz_mount_image_erofs_9
M       sys/linux/test/syz_mount_image_exfat_0
M       sys/linux/test/syz_mount_image_exfat_1
M       sys/linux/test/syz_mount_image_ext4_0
M       sys/linux/test/syz_mount_image_ext4_1
M       sys/linux/test/syz_mount_image_ext4_10
M       sys/linux/test/syz_mount_image_ext4_11
M       sys/linux/test/syz_mount_image_ext4_12
M       sys/linux/test/syz_mount_image_ext4_13
M       sys/linux/test/syz_mount_image_ext4_14
M       sys/linux/test/syz_mount_image_ext4_15
M       sys/linux/test/syz_mount_image_ext4_16
M       sys/linux/test/syz_mount_image_ext4_17
M       sys/linux/test/syz_mount_image_ext4_18
M       sys/linux/test/syz_mount_image_ext4_19
M       sys/linux/test/syz_mount_image_ext4_2
M       sys/linux/test/syz_mount_image_ext4_20
M       sys/linux/test/syz_mount_image_ext4_21
M       sys/linux/test/syz_mount_image_ext4_22
M       sys/linux/test/syz_mount_image_ext4_23
M       sys/linux/test/syz_mount_image_ext4_24
M       sys/linux/test/syz_mount_image_ext4_25
M       sys/linux/test/syz_mount_image_ext4_26
M       sys/linux/test/syz_mount_image_ext4_27
M       sys/linux/test/syz_mount_image_ext4_28
M       sys/linux/test/syz_mount_image_ext4_29
M       sys/linux/test/syz_mount_image_ext4_3
M       sys/linux/test/syz_mount_image_ext4_30
M       sys/linux/test/syz_mount_image_ext4_31
M       sys/linux/test/syz_mount_image_ext4_32
M       sys/linux/test/syz_mount_image_ext4_33
M       sys/linux/test/syz_mount_image_ext4_34
M       sys/linux/test/syz_mount_image_ext4_35
M       sys/linux/test/syz_mount_image_ext4_36
M       sys/linux/test/syz_mount_image_ext4_37
M       sys/linux/test/syz_mount_image_ext4_38
M       sys/linux/test/syz_mount_image_ext4_39
M       sys/linux/test/syz_mount_image_ext4_4
M       sys/linux/test/syz_mount_image_ext4_40
M       sys/linux/test/syz_mount_image_ext4_41
M       sys/linux/test/syz_mount_image_ext4_42
M       sys/linux/test/syz_mount_image_ext4_43
M       sys/linux/test/syz_mount_image_ext4_44
M       sys/linux/test/syz_mount_image_ext4_45
M       sys/linux/test/syz_mount_image_ext4_46
M       sys/linux/test/syz_mount_image_ext4_47
M       sys/linux/test/syz_mount_image_ext4_48
M       sys/linux/test/syz_mount_image_ext4_49
M       sys/linux/test/syz_mount_image_ext4_5
M       sys/linux/test/syz_mount_image_ext4_50
M       sys/linux/test/syz_mount_image_ext4_51
M       sys/linux/test/syz_mount_image_ext4_52
M       sys/linux/test/syz_mount_image_ext4_53
M       sys/linux/test/syz_mount_image_ext4_54
M       sys/linux/test/syz_mount_image_ext4_55
M       sys/linux/test/syz_mount_image_ext4_56
M       sys/linux/test/syz_mount_image_ext4_57
M       sys/linux/test/syz_mount_image_ext4_58
M       sys/linux/test/syz_mount_image_ext4_59
M       sys/linux/test/syz_mount_image_ext4_6
M       sys/linux/test/syz_mount_image_ext4_60
M       sys/linux/test/syz_mount_image_ext4_61
M       sys/linux/test/syz_mount_image_ext4_62
M       sys/linux/test/syz_mount_image_ext4_7
M       sys/linux/test/syz_mount_image_ext4_8
M       sys/linux/test/syz_mount_image_ext4_9
M       sys/linux/test/syz_mount_image_f2fs_0
M       sys/linux/test/syz_mount_image_f2fs_1
M       sys/linux/test/syz_mount_image_f2fs_10
M       sys/linux/test/syz_mount_image_f2fs_11
M       sys/linux/test/syz_mount_image_f2fs_12
M       sys/linux/test/syz_mount_image_f2fs_13
M       sys/linux/test/syz_mount_image_f2fs_14
M       sys/linux/test/syz_mount_image_f2fs_15
M       sys/linux/test/syz_mount_image_f2fs_16
M       sys/linux/test/syz_mount_image_f2fs_17
M       sys/linux/test/syz_mount_image_f2fs_18
M       sys/linux/test/syz_mount_image_f2fs_19
M       sys/linux/test/syz_mount_image_f2fs_2
M       sys/linux/test/syz_mount_image_f2fs_20
M       sys/linux/test/syz_mount_image_f2fs_21
M       sys/linux/test/syz_mount_image_f2fs_22
M       sys/linux/test/syz_mount_image_f2fs_23
M       sys/linux/test/syz_mount_image_f2fs_24
M       sys/linux/test/syz_mount_image_f2fs_25
M       sys/linux/test/syz_mount_image_f2fs_26
M       sys/linux/test/syz_mount_image_f2fs_27
M       sys/linux/test/syz_mount_image_f2fs_28
M       sys/linux/test/syz_mount_image_f2fs_29
M       sys/linux/test/syz_mount_image_f2fs_3
M       sys/linux/test/syz_mount_image_f2fs_30
M       sys/linux/test/syz_mount_image_f2fs_31
M       sys/linux/test/syz_mount_image_f2fs_4
M       sys/linux/test/syz_mount_image_f2fs_5
M       sys/linux/test/syz_mount_image_f2fs_6
M       sys/linux/test/syz_mount_image_f2fs_7
M       sys/linux/test/syz_mount_image_f2fs_8
M       sys/linux/test/syz_mount_image_f2fs_9
M       sys/linux/test/syz_mount_image_fuse
M       sys/linux/test/syz_mount_image_gfs2_0
M       sys/linux/test/syz_mount_image_gfs2_1
M       sys/linux/test/syz_mount_image_gfs2_10
M       sys/linux/test/syz_mount_image_gfs2_11
M       sys/linux/test/syz_mount_image_gfs2_12
M       sys/linux/test/syz_mount_image_gfs2_13
M       sys/linux/test/syz_mount_image_gfs2_14
M       sys/linux/test/syz_mount_image_gfs2_15
M       sys/linux/test/syz_mount_image_gfs2_16
M       sys/linux/test/syz_mount_image_gfs2_17
M       sys/linux/test/syz_mount_image_gfs2_18
M       sys/linux/test/syz_mount_image_gfs2_19
M       sys/linux/test/syz_mount_image_gfs2_2
M       sys/linux/test/syz_mount_image_gfs2_20
M       sys/linux/test/syz_mount_image_gfs2_21
M       sys/linux/test/syz_mount_image_gfs2_22
M       sys/linux/test/syz_mount_image_gfs2_23
M       sys/linux/test/syz_mount_image_gfs2_24
M       sys/linux/test/syz_mount_image_gfs2_25
M       sys/linux/test/syz_mount_image_gfs2_26
M       sys/linux/test/syz_mount_image_gfs2_27
M       sys/linux/test/syz_mount_image_gfs2_28
M       sys/linux/test/syz_mount_image_gfs2_29
M       sys/linux/test/syz_mount_image_gfs2_3
M       sys/linux/test/syz_mount_image_gfs2_30
M       sys/linux/test/syz_mount_image_gfs2_31
M       sys/linux/test/syz_mount_image_gfs2_4
M       sys/linux/test/syz_mount_image_gfs2_5
M       sys/linux/test/syz_mount_image_gfs2_6
M       sys/linux/test/syz_mount_image_gfs2_7
M       sys/linux/test/syz_mount_image_gfs2_8
M       sys/linux/test/syz_mount_image_gfs2_9
M       sys/linux/test/syz_mount_image_iso9660_0
M       sys/linux/test/syz_mount_image_iso9660_1
M       sys/linux/test/syz_mount_image_iso9660_10
M       sys/linux/test/syz_mount_image_iso9660_11
M       sys/linux/test/syz_mount_image_iso9660_12
M       sys/linux/test/syz_mount_image_iso9660_13
M       sys/linux/test/syz_mount_image_iso9660_14
M       sys/linux/test/syz_mount_image_iso9660_15
M       sys/linux/test/syz_mount_image_iso9660_16
M       sys/linux/test/syz_mount_image_iso9660_17
M       sys/linux/test/syz_mount_image_iso9660_2
M       sys/linux/test/syz_mount_image_iso9660_3
M       sys/linux/test/syz_mount_image_iso9660_4
M       sys/linux/test/syz_mount_image_iso9660_5
M       sys/linux/test/syz_mount_image_iso9660_6
M       sys/linux/test/syz_mount_image_iso9660_7
M       sys/linux/test/syz_mount_image_iso9660_8
M       sys/linux/test/syz_mount_image_iso9660_9
M       sys/linux/test/syz_mount_image_jffs2_0
M       sys/linux/test/syz_mount_image_jffs2_1
M       sys/linux/test/syz_mount_image_jffs2_2
M       sys/linux/test/syz_mount_image_jffs2_3
M       sys/linux/test/syz_mount_image_jffs2_4
M       sys/linux/test/syz_mount_image_jffs2_5
M       sys/linux/test/syz_mount_image_jffs2_6
M       sys/linux/test/syz_mount_image_jffs2_7
M       sys/linux/test/syz_mount_image_jfs_0
M       sys/linux/test/syz_mount_image_jfs_1
M       sys/linux/test/syz_mount_image_jfs_2
M       sys/linux/test/syz_mount_image_jfs_3
M       sys/linux/test/syz_mount_image_minix_0
M       sys/linux/test/syz_mount_image_minix_1
M       sys/linux/test/syz_mount_image_minix_10
M       sys/linux/test/syz_mount_image_minix_11
M       sys/linux/test/syz_mount_image_minix_12
M       sys/linux/test/syz_mount_image_minix_13
M       sys/linux/test/syz_mount_image_minix_14
M       sys/linux/test/syz_mount_image_minix_2
M       sys/linux/test/syz_mount_image_minix_3
M       sys/linux/test/syz_mount_image_minix_4
M       sys/linux/test/syz_mount_image_minix_5
M       sys/linux/test/syz_mount_image_minix_6
M       sys/linux/test/syz_mount_image_minix_7
M       sys/linux/test/syz_mount_image_minix_8
M       sys/linux/test/syz_mount_image_minix_9
M       sys/linux/test/syz_mount_image_nilfs2_0
M       sys/linux/test/syz_mount_image_nilfs2_1
M       sys/linux/test/syz_mount_image_nilfs2_10
M       sys/linux/test/syz_mount_image_nilfs2_11
M       sys/linux/test/syz_mount_image_nilfs2_12
M       sys/linux/test/syz_mount_image_nilfs2_13
M       sys/linux/test/syz_mount_image_nilfs2_14
M       sys/linux/test/syz_mount_image_nilfs2_15
M       sys/linux/test/syz_mount_image_nilfs2_16
M       sys/linux/test/syz_mount_image_nilfs2_17
M       sys/linux/test/syz_mount_image_nilfs2_2
M       sys/linux/test/syz_mount_image_nilfs2_3
M       sys/linux/test/syz_mount_image_nilfs2_4
M       sys/linux/test/syz_mount_image_nilfs2_5
M       sys/linux/test/syz_mount_image_nilfs2_6
M       sys/linux/test/syz_mount_image_nilfs2_7
M       sys/linux/test/syz_mount_image_nilfs2_8
M       sys/linux/test/syz_mount_image_nilfs2_9
M       sys/linux/test/syz_mount_image_ntfs_10
M       sys/linux/test/syz_mount_image_ntfs_11
M       sys/linux/test/syz_mount_image_ntfs_12
M       sys/linux/test/syz_mount_image_ntfs_13
M       sys/linux/test/syz_mount_image_ntfs_14
M       sys/linux/test/syz_mount_image_ntfs_15
M       sys/linux/test/syz_mount_image_ntfs_16
M       sys/linux/test/syz_mount_image_ntfs_17
M       sys/linux/test/syz_mount_image_ntfs_18
M       sys/linux/test/syz_mount_image_ntfs_19
M       sys/linux/test/syz_mount_image_ntfs_2
M       sys/linux/test/syz_mount_image_ntfs_3
M       sys/linux/test/syz_mount_image_ntfs_4
M       sys/linux/test/syz_mount_image_ntfs_5
M       sys/linux/test/syz_mount_image_ntfs_6
M       sys/linux/test/syz_mount_image_ntfs_7
M       sys/linux/test/syz_mount_image_ntfs_8
M       sys/linux/test/syz_mount_image_ntfs_9
M       sys/linux/test/syz_mount_image_ocfs2_0
M       sys/linux/test/syz_mount_image_ocfs2_1
M       sys/linux/test/syz_mount_image_ocfs2_10
M       sys/linux/test/syz_mount_image_ocfs2_11
M       sys/linux/test/syz_mount_image_ocfs2_12
M       sys/linux/test/syz_mount_image_ocfs2_13
M       sys/linux/test/syz_mount_image_ocfs2_14
M       sys/linux/test/syz_mount_image_ocfs2_15
M       sys/linux/test/syz_mount_image_ocfs2_16
M       sys/linux/test/syz_mount_image_ocfs2_17
M       sys/linux/test/syz_mount_image_ocfs2_18
M       sys/linux/test/syz_mount_image_ocfs2_19
M       sys/linux/test/syz_mount_image_ocfs2_2
M       sys/linux/test/syz_mount_image_ocfs2_20
M       sys/linux/test/syz_mount_image_ocfs2_21
M       sys/linux/test/syz_mount_image_ocfs2_22
M       sys/linux/test/syz_mount_image_ocfs2_23
M       sys/linux/test/syz_mount_image_ocfs2_24
M       sys/linux/test/syz_mount_image_ocfs2_25
M       sys/linux/test/syz_mount_image_ocfs2_26
M       sys/linux/test/syz_mount_image_ocfs2_27
M       sys/linux/test/syz_mount_image_ocfs2_28
M       sys/linux/test/syz_mount_image_ocfs2_29
M       sys/linux/test/syz_mount_image_ocfs2_3
M       sys/linux/test/syz_mount_image_ocfs2_30
M       sys/linux/test/syz_mount_image_ocfs2_31
M       sys/linux/test/syz_mount_image_ocfs2_32
M       sys/linux/test/syz_mount_image_ocfs2_33
M       sys/linux/test/syz_mount_image_ocfs2_34
M       sys/linux/test/syz_mount_image_ocfs2_35
M       sys/linux/test/syz_mount_image_ocfs2_36
M       sys/linux/test/syz_mount_image_ocfs2_37
M       sys/linux/test/syz_mount_image_ocfs2_38
M       sys/linux/test/syz_mount_image_ocfs2_39
M       sys/linux/test/syz_mount_image_ocfs2_4
M       sys/linux/test/syz_mount_image_ocfs2_40
M       sys/linux/test/syz_mount_image_ocfs2_41
M       sys/linux/test/syz_mount_image_ocfs2_42
M       sys/linux/test/syz_mount_image_ocfs2_43
M       sys/linux/test/syz_mount_image_ocfs2_44
M       sys/linux/test/syz_mount_image_ocfs2_45
M       sys/linux/test/syz_mount_image_ocfs2_46
M       sys/linux/test/syz_mount_image_ocfs2_47
M       sys/linux/test/syz_mount_image_ocfs2_48
M       sys/linux/test/syz_mount_image_ocfs2_49
M       sys/linux/test/syz_mount_image_ocfs2_5
M       sys/linux/test/syz_mount_image_ocfs2_50
M       sys/linux/test/syz_mount_image_ocfs2_51
M       sys/linux/test/syz_mount_image_ocfs2_52
M       sys/linux/test/syz_mount_image_ocfs2_53
M       sys/linux/test/syz_mount_image_ocfs2_54
M       sys/linux/test/syz_mount_image_ocfs2_55
M       sys/linux/test/syz_mount_image_ocfs2_56
M       sys/linux/test/syz_mount_image_ocfs2_57
M       sys/linux/test/syz_mount_image_ocfs2_58
M       sys/linux/test/syz_mount_image_ocfs2_59
M       sys/linux/test/syz_mount_image_ocfs2_6
M       sys/linux/test/syz_mount_image_ocfs2_60
M       sys/linux/test/syz_mount_image_ocfs2_61
M       sys/linux/test/syz_mount_image_ocfs2_62
M       sys/linux/test/syz_mount_image_ocfs2_63
M       sys/linux/test/syz_mount_image_ocfs2_64
M       sys/linux/test/syz_mount_image_ocfs2_65
M       sys/linux/test/syz_mount_image_ocfs2_66
M       sys/linux/test/syz_mount_image_ocfs2_67
M       sys/linux/test/syz_mount_image_ocfs2_68
M       sys/linux/test/syz_mount_image_ocfs2_69
M       sys/linux/test/syz_mount_image_ocfs2_7
M       sys/linux/test/syz_mount_image_ocfs2_70
M       sys/linux/test/syz_mount_image_ocfs2_71
M       sys/linux/test/syz_mount_image_ocfs2_8
M       sys/linux/test/syz_mount_image_ocfs2_9
M       sys/linux/test/syz_mount_image_reiserfs_0
M       sys/linux/test/syz_mount_image_reiserfs_1
M       sys/linux/test/syz_mount_image_reiserfs_10
M       sys/linux/test/syz_mount_image_reiserfs_11
M       sys/linux/test/syz_mount_image_reiserfs_12
M       sys/linux/test/syz_mount_image_reiserfs_13
M       sys/linux/test/syz_mount_image_reiserfs_14
M       sys/linux/test/syz_mount_image_reiserfs_15
M       sys/linux/test/syz_mount_image_reiserfs_16
M       sys/linux/test/syz_mount_image_reiserfs_17
M       sys/linux/test/syz_mount_image_reiserfs_18
M       sys/linux/test/syz_mount_image_reiserfs_19
M       sys/linux/test/syz_mount_image_reiserfs_2
M       sys/linux/test/syz_mount_image_reiserfs_20
M       sys/linux/test/syz_mount_image_reiserfs_21
M       sys/linux/test/syz_mount_image_reiserfs_22
M       sys/linux/test/syz_mount_image_reiserfs_23
M       sys/linux/test/syz_mount_image_reiserfs_24
M       sys/linux/test/syz_mount_image_reiserfs_25
M       sys/linux/test/syz_mount_image_reiserfs_26
M       sys/linux/test/syz_mount_image_reiserfs_27
M       sys/linux/test/syz_mount_image_reiserfs_28
M       sys/linux/test/syz_mount_image_reiserfs_29
M       sys/linux/test/syz_mount_image_reiserfs_3
M       sys/linux/test/syz_mount_image_reiserfs_30
M       sys/linux/test/syz_mount_image_reiserfs_31
M       sys/linux/test/syz_mount_image_reiserfs_32
M       sys/linux/test/syz_mount_image_reiserfs_33
M       sys/linux/test/syz_mount_image_reiserfs_34
M       sys/linux/test/syz_mount_image_reiserfs_35
M       sys/linux/test/syz_mount_image_reiserfs_36
M       sys/linux/test/syz_mount_image_reiserfs_37
M       sys/linux/test/syz_mount_image_reiserfs_38
M       sys/linux/test/syz_mount_image_reiserfs_39
M       sys/linux/test/syz_mount_image_reiserfs_4
M       sys/linux/test/syz_mount_image_reiserfs_40
M       sys/linux/test/syz_mount_image_reiserfs_41
M       sys/linux/test/syz_mount_image_reiserfs_42
M       sys/linux/test/syz_mount_image_reiserfs_43
M       sys/linux/test/syz_mount_image_reiserfs_44
M       sys/linux/test/syz_mount_image_reiserfs_45
M       sys/linux/test/syz_mount_image_reiserfs_46
M       sys/linux/test/syz_mount_image_reiserfs_47
M       sys/linux/test/syz_mount_image_reiserfs_48
M       sys/linux/test/syz_mount_image_reiserfs_49
M       sys/linux/test/syz_mount_image_reiserfs_5
M       sys/linux/test/syz_mount_image_reiserfs_50
M       sys/linux/test/syz_mount_image_reiserfs_51
M       sys/linux/test/syz_mount_image_reiserfs_52
M       sys/linux/test/syz_mount_image_reiserfs_53
M       sys/linux/test/syz_mount_image_reiserfs_54
M       sys/linux/test/syz_mount_image_reiserfs_55
M       sys/linux/test/syz_mount_image_reiserfs_56
M       sys/linux/test/syz_mount_image_reiserfs_57
M       sys/linux/test/syz_mount_image_reiserfs_58
M       sys/linux/test/syz_mount_image_reiserfs_59
M       sys/linux/test/syz_mount_image_reiserfs_6
M       sys/linux/test/syz_mount_image_reiserfs_7
M       sys/linux/test/syz_mount_image_reiserfs_8
M       sys/linux/test/syz_mount_image_reiserfs_9
M       sys/linux/test/syz_mount_image_romfs_0
M       sys/linux/test/syz_mount_image_romfs_1
M       sys/linux/test/syz_mount_image_squashfs_0
M       sys/linux/test/syz_mount_image_squashfs_1
M       sys/linux/test/syz_mount_image_squashfs_10
M       sys/linux/test/syz_mount_image_squashfs_11
M       sys/linux/test/syz_mount_image_squashfs_12
M       sys/linux/test/syz_mount_image_squashfs_13
M       sys/linux/test/syz_mount_image_squashfs_14
M       sys/linux/test/syz_mount_image_squashfs_15
M       sys/linux/test/syz_mount_image_squashfs_16
M       sys/linux/test/syz_mount_image_squashfs_17
M       sys/linux/test/syz_mount_image_squashfs_2
M       sys/linux/test/syz_mount_image_squashfs_3
M       sys/linux/test/syz_mount_image_squashfs_4
M       sys/linux/test/syz_mount_image_squashfs_5
M       sys/linux/test/syz_mount_image_squashfs_6
M       sys/linux/test/syz_mount_image_squashfs_7
M       sys/linux/test/syz_mount_image_squashfs_8
M       sys/linux/test/syz_mount_image_squashfs_9
M       sys/linux/test/syz_mount_image_udf_0
M       sys/linux/test/syz_mount_image_udf_1
M       sys/linux/test/syz_mount_image_udf_10
M       sys/linux/test/syz_mount_image_udf_11
M       sys/linux/test/syz_mount_image_udf_12
M       sys/linux/test/syz_mount_image_udf_13
M       sys/linux/test/syz_mount_image_udf_14
M       sys/linux/test/syz_mount_image_udf_15
M       sys/linux/test/syz_mount_image_udf_16
M       sys/linux/test/syz_mount_image_udf_17
M       sys/linux/test/syz_mount_image_udf_18
M       sys/linux/test/syz_mount_image_udf_19
M       sys/linux/test/syz_mount_image_udf_2
M       sys/linux/test/syz_mount_image_udf_20
M       sys/linux/test/syz_mount_image_udf_21
M       sys/linux/test/syz_mount_image_udf_22
M       sys/linux/test/syz_mount_image_udf_23
M       sys/linux/test/syz_mount_image_udf_24
M       sys/linux/test/syz_mount_image_udf_25
M       sys/linux/test/syz_mount_image_udf_26
M       sys/linux/test/syz_mount_image_udf_27
M       sys/linux/test/syz_mount_image_udf_28
M       sys/linux/test/syz_mount_image_udf_29
M       sys/linux/test/syz_mount_image_udf_3
M       sys/linux/test/syz_mount_image_udf_30
M       sys/linux/test/syz_mount_image_udf_31
M       sys/linux/test/syz_mount_image_udf_32
M       sys/linux/test/syz_mount_image_udf_33
M       sys/linux/test/syz_mount_image_udf_34
M       sys/linux/test/syz_mount_image_udf_35
M       sys/linux/test/syz_mount_image_udf_36
M       sys/linux/test/syz_mount_image_udf_37
M       sys/linux/test/syz_mount_image_udf_38
M       sys/linux/test/syz_mount_image_udf_39
M       sys/linux/test/syz_mount_image_udf_4
M       sys/linux/test/syz_mount_image_udf_40
M       sys/linux/test/syz_mount_image_udf_41
M       sys/linux/test/syz_mount_image_udf_42
M       sys/linux/test/syz_mount_image_udf_43
M       sys/linux/test/syz_mount_image_udf_44
M       sys/linux/test/syz_mount_image_udf_45
M       sys/linux/test/syz_mount_image_udf_46
M       sys/linux/test/syz_mount_image_udf_47
M       sys/linux/test/syz_mount_image_udf_48
M       sys/linux/test/syz_mount_image_udf_49
M       sys/linux/test/syz_mount_image_udf_5
M       sys/linux/test/syz_mount_image_udf_50
M       sys/linux/test/syz_mount_image_udf_51
M       sys/linux/test/syz_mount_image_udf_52
M       sys/linux/test/syz_mount_image_udf_53
M       sys/linux/test/syz_mount_image_udf_54
M       sys/linux/test/syz_mount_image_udf_55
M       sys/linux/test/syz_mount_image_udf_56
M       sys/linux/test/syz_mount_image_udf_6
M       sys/linux/test/syz_mount_image_udf_7
M       sys/linux/test/syz_mount_image_udf_8
M       sys/linux/test/syz_mount_image_udf_9
M       sys/linux/test/syz_mount_image_vfat_0
M       sys/linux/test/syz_mount_image_vfat_1
M       sys/linux/test/syz_mount_image_vfat_10
M       sys/linux/test/syz_mount_image_vfat_11
M       sys/linux/test/syz_mount_image_vfat_12
M       sys/linux/test/syz_mount_image_vfat_13
M       sys/linux/test/syz_mount_image_vfat_14
M       sys/linux/test/syz_mount_image_vfat_15
M       sys/linux/test/syz_mount_image_vfat_16
M       sys/linux/test/syz_mount_image_vfat_17
M       sys/linux/test/syz_mount_image_vfat_18
M       sys/linux/test/syz_mount_image_vfat_19
M       sys/linux/test/syz_mount_image_vfat_2
M       sys/linux/test/syz_mount_image_vfat_20
M       sys/linux/test/syz_mount_image_vfat_21
M       sys/linux/test/syz_mount_image_vfat_22
M       sys/linux/test/syz_mount_image_vfat_23
M       sys/linux/test/syz_mount_image_vfat_24
M       sys/linux/test/syz_mount_image_vfat_25
M       sys/linux/test/syz_mount_image_vfat_26
M       sys/linux/test/syz_mount_image_vfat_27
M       sys/linux/test/syz_mount_image_vfat_28
M       sys/linux/test/syz_mount_image_vfat_29
M       sys/linux/test/syz_mount_image_vfat_3
M       sys/linux/test/syz_mount_image_vfat_30
M       sys/linux/test/syz_mount_image_vfat_31
M       sys/linux/test/syz_mount_image_vfat_32
M       sys/linux/test/syz_mount_image_vfat_33
M       sys/linux/test/syz_mount_image_vfat_34
M       sys/linux/test/syz_mount_image_vfat_35
M       sys/linux/test/syz_mount_image_vfat_36
M       sys/linux/test/syz_mount_image_vfat_37
M       sys/linux/test/syz_mount_image_vfat_38
M       sys/linux/test/syz_mount_image_vfat_39
M       sys/linux/test/syz_mount_image_vfat_4
M       sys/linux/test/syz_mount_image_vfat_40
M       sys/linux/test/syz_mount_image_vfat_41
M       sys/linux/test/syz_mount_image_vfat_42
M       sys/linux/test/syz_mount_image_vfat_43
M       sys/linux/test/syz_mount_image_vfat_44
M       sys/linux/test/syz_mount_image_vfat_45
M       sys/linux/test/syz_mount_image_vfat_46
M       sys/linux/test/syz_mount_image_vfat_47
M       sys/linux/test/syz_mount_image_vfat_48
M       sys/linux/test/syz_mount_image_vfat_49
M       sys/linux/test/syz_mount_image_vfat_5
M       sys/linux/test/syz_mount_image_vfat_50
M       sys/linux/test/syz_mount_image_vfat_51
M       sys/linux/test/syz_mount_image_vfat_52
M       sys/linux/test/syz_mount_image_vfat_53
M       sys/linux/test/syz_mount_image_vfat_54
M       sys/linux/test/syz_mount_image_vfat_55
M       sys/linux/test/syz_mount_image_vfat_56
M       sys/linux/test/syz_mount_image_vfat_57
M       sys/linux/test/syz_mount_image_vfat_58
M       sys/linux/test/syz_mount_image_vfat_59
M       sys/linux/test/syz_mount_image_vfat_6
M       sys/linux/test/syz_mount_image_vfat_7
M       sys/linux/test/syz_mount_image_vfat_8
M       sys/linux/test/syz_mount_image_vfat_9
M       sys/linux/test/syz_mount_image_xfs_0
M       sys/linux/test/syz_mount_image_xfs_1
M       sys/linux/test/syz_mount_image_xfs_10
M       sys/linux/test/syz_mount_image_xfs_11
M       sys/linux/test/syz_mount_image_xfs_12
M       sys/linux/test/syz_mount_image_xfs_13
M       sys/linux/test/syz_mount_image_xfs_14
M       sys/linux/test/syz_mount_image_xfs_15
M       sys/linux/test/syz_mount_image_xfs_16
M       sys/linux/test/syz_mount_image_xfs_17
M       sys/linux/test/syz_mount_image_xfs_18
M       sys/linux/test/syz_mount_image_xfs_19
M       sys/linux/test/syz_mount_image_xfs_2
M       sys/linux/test/syz_mount_image_xfs_20
M       sys/linux/test/syz_mount_image_xfs_21
M       sys/linux/test/syz_mount_image_xfs_22
M       sys/linux/test/syz_mount_image_xfs_23
M       sys/linux/test/syz_mount_image_xfs_24
M       sys/linux/test/syz_mount_image_xfs_25
M       sys/linux/test/syz_mount_image_xfs_26
M       sys/linux/test/syz_mount_image_xfs_27
M       sys/linux/test/syz_mount_image_xfs_28
M       sys/linux/test/syz_mount_image_xfs_29
M       sys/linux/test/syz_mount_image_xfs_3
M       sys/linux/test/syz_mount_image_xfs_30
M       sys/linux/test/syz_mount_image_xfs_31
M       sys/linux/test/syz_mount_image_xfs_32
M       sys/linux/test/syz_mount_image_xfs_33
M       sys/linux/test/syz_mount_image_xfs_34
M       sys/linux/test/syz_mount_image_xfs_35
M       sys/linux/test/syz_mount_image_xfs_4
M       sys/linux/test/syz_mount_image_xfs_5
M       sys/linux/test/syz_mount_image_xfs_6
M       sys/linux/test/syz_mount_image_xfs_7
M       sys/linux/test/syz_mount_image_xfs_8
M       sys/linux/test/syz_mount_image_xfs_9
M       sys/linux/test/tipc
M       sys/linux/test/udp
M       sys/linux/test/udp2
M       sys/linux/test/vhci
M       sys/linux/test/vnet_tun
M       sys/linux/test/vusb
M       sys/linux/test/vusb_ath9k
M       sys/linux/test/vusb_cdc_ecm
M       sys/linux/test/vusb_cdc_ncm
M       sys/linux/test/vusb_hid
M       sys/linux/test/vusb_hid_hiddev
M       sys/linux/test/vusb_printer
M       sys/linux/test/wireguard
M       syz-fuzzer/testing.go
M       vm/qemu/qemu.go
HEAD is now at 3cd800e43 tools: update buildroot version

[CMD]: tar -xzvf /home/nick/PrIntFuzz/patch/syzkaller.patch.tar.gz -C /home/nick/PrIntFuzz/patch
syzkaller.patch

[CMD]: git apply /home/nick/PrIntFuzz/patch/syzkaller.patch
error: patch failed: .gitignore:18
error: .gitignore: patch does not apply
error: patch failed: executor/common_linux.h:1384
error: executor/common_linux.h: patch does not apply
error: patch failed: executor/executor.cc:860
error: executor/executor.cc: patch does not apply
error: patch failed: pkg/host/syscalls_linux.go:318
error: pkg/host/syscalls_linux.go: patch does not apply
error: patch failed: prog/generation.go:16
error: prog/generation.go: patch does not apply
error: patch failed: prog/minimization.go:63
error: prog/minimization.go: patch does not apply
error: patch failed: prog/mutation.go:77
error: prog/mutation.go: patch does not apply
error: patch failed: prog/prog.go:416
error: prog/prog.go: patch does not apply
error: patch failed: prog/rand.go:385
error: prog/rand.go: patch does not apply
error: patch failed: sys/linux/dev_fb.txt:8
error: sys/linux/dev_fb.txt: patch does not apply
error: sys/linux/fake_drivers_counter_counter.txt: already exists in working directory
error: sys/linux/fake_drivers_firewire_nosy.txt: already exists in working directory
error: sys/linux/fake_drivers_misc_pci_endpoint_test.txt: already exists in working directory
error: sys/linux/fake_drivers_misc_phantom.txt: already exists in working directory
error: sys/linux/fake_drivers_pci_switch_switchtec.txt: already exists in working directory
error: sys/linux/fake_drivers_tty_mxser.txt: already exists in working directory
error: sys/linux/fake_drivers_tty_nozomi.txt: already exists in working directory
error: sys/linux/fake_drivers_tty_synclink_gt.txt: already exists in working directory
error: sys/linux/fake_drivers_watchdog.txt: already exists in working directory
error: patch failed: sys/linux/filesystem.txt:5
error: sys/linux/filesystem.txt: patch does not apply
error: sys/linux/print_fuzz.txt: already exists in working directory
error: patch failed: sys/linux/socket.txt:383
error: sys/linux/socket.txt: patch does not apply
error: patch failed: sys/linux/test/80211_ibss:2
error: sys/linux/test/80211_ibss: patch does not apply
error: patch failed: sys/linux/test/80211_scan:1
error: sys/linux/test/80211_scan: patch does not apply
error: patch failed: sys/linux/test/80211_setup_ap:1
error: sys/linux/test/80211_setup_ap: patch does not apply
error: patch failed: sys/linux/test/80211_setup_mesh:1
error: sys/linux/test/80211_setup_mesh: patch does not apply
error: patch failed: sys/linux/test/80211_setup_station:1
error: sys/linux/test/80211_setup_station: patch does not apply
error: patch failed: sys/linux/test/binder:1
error: sys/linux/test/binder: patch does not apply
error: patch failed: sys/linux/test/binfmt:1
error: sys/linux/test/binfmt: patch does not apply
error: patch failed: sys/linux/test/bpf_cgroup:1
error: sys/linux/test/bpf_cgroup: patch does not apply
error: patch failed: sys/linux/test/btf_id:1
error: sys/linux/test/btf_id: patch does not apply
error: patch failed: sys/linux/test/can:1
error: sys/linux/test/can: patch does not apply
error: patch failed: sys/linux/test/caps:2
error: sys/linux/test/caps: patch does not apply
error: patch failed: sys/linux/test/cgroup:3
error: sys/linux/test/cgroup: patch does not apply
error: patch failed: sys/linux/test/dev_bifrost:1
error: sys/linux/test/dev_bifrost: patch does not apply
error: patch failed: sys/linux/test/exit0:1
error: sys/linux/test/exit0: patch does not apply
error: patch failed: sys/linux/test/exit1:1
error: sys/linux/test/exit1: patch does not apply
error: patch failed: sys/linux/test/fd_assignment:1
error: sys/linux/test/fd_assignment: patch does not apply
error: patch failed: sys/linux/test/file:1
error: sys/linux/test/file: patch does not apply
error: patch failed: sys/linux/test/file_immutable:3
error: sys/linux/test/file_immutable: patch does not apply
error: patch failed: sys/linux/test/fscrypt_ext4:2
error: sys/linux/test/fscrypt_ext4: patch does not apply
error: patch failed: sys/linux/test/fscrypt_f2fs:2
error: sys/linux/test/fscrypt_f2fs: patch does not apply
error: patch failed: sys/linux/test/fuse_deadlock:1
error: sys/linux/test/fuse_deadlock: patch does not apply
error: patch failed: sys/linux/test/fuse_getdents64:1
error: sys/linux/test/fuse_getdents64: patch does not apply
error: patch failed: sys/linux/test/gup_fast:1
error: sys/linux/test/gup_fast: patch does not apply
error: patch failed: sys/linux/test/io_uring:1
error: sys/linux/test/io_uring: patch does not apply
error: patch failed: sys/linux/test/ipc:2
error: sys/linux/test/ipc: patch does not apply
error: patch failed: sys/linux/test/landlock_fs_accesses:5
error: sys/linux/test/landlock_fs_accesses: patch does not apply
error: patch failed: sys/linux/test/landlock_fs_forbidden:5
error: sys/linux/test/landlock_fs_forbidden: patch does not apply
error: patch failed: sys/linux/test/landlock_layers:1
error: sys/linux/test/landlock_layers: patch does not apply
error: patch failed: sys/linux/test/landlock_ptrace:1
error: sys/linux/test/landlock_ptrace: patch does not apply
error: patch failed: sys/linux/test/landlock_sb_delete:3
error: sys/linux/test/landlock_sb_delete: patch does not apply
error: patch failed: sys/linux/test/mmap:1
error: sys/linux/test/mmap: patch does not apply
error: patch failed: sys/linux/test/netrom:1
error: sys/linux/test/netrom: patch does not apply
error: patch failed: sys/linux/test/pipe:1
error: sys/linux/test/pipe: patch does not apply
error: sys/linux/test/print_fuzz: already exists in working directory
error: patch failed: sys/linux/test/rfkill:1
error: sys/linux/test/rfkill: patch does not apply
error: patch failed: sys/linux/test/syz_clone:1
error: sys/linux/test/syz_clone: patch does not apply
error: patch failed: sys/linux/test/syz_clone3:1
error: sys/linux/test/syz_clone3: patch does not apply
error: patch failed: sys/linux/test/syz_fuse_handle_req:1
error: sys/linux/test/syz_fuse_handle_req: patch does not apply
error: patch failed: sys/linux/test/syz_genetlink_get_family_id:1
error: sys/linux/test/syz_genetlink_get_family_id: patch does not apply
error: patch failed: sys/linux/test/syz_kvm_setup_cpu_ppc64le:1
error: sys/linux/test/syz_kvm_setup_cpu_ppc64le: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image:1
error: sys/linux/test/syz_mount_image: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_bfs_0:1
error: sys/linux/test/syz_mount_image_bfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_bfs_1:1
error: sys/linux/test/syz_mount_image_bfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_bfs_2:1
error: sys/linux/test/syz_mount_image_bfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_0:1
error: sys/linux/test/syz_mount_image_btrfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_1:1
error: sys/linux/test/syz_mount_image_btrfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_10:1
error: sys/linux/test/syz_mount_image_btrfs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_11:1
error: sys/linux/test/syz_mount_image_btrfs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_12:1
error: sys/linux/test/syz_mount_image_btrfs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_13:1
error: sys/linux/test/syz_mount_image_btrfs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_14:1
error: sys/linux/test/syz_mount_image_btrfs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_15:1
error: sys/linux/test/syz_mount_image_btrfs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_16:1
error: sys/linux/test/syz_mount_image_btrfs_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_17:1
error: sys/linux/test/syz_mount_image_btrfs_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_18:1
error: sys/linux/test/syz_mount_image_btrfs_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_19:1
error: sys/linux/test/syz_mount_image_btrfs_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_2:1
error: sys/linux/test/syz_mount_image_btrfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_20:1
error: sys/linux/test/syz_mount_image_btrfs_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_21:1
error: sys/linux/test/syz_mount_image_btrfs_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_22:1
error: sys/linux/test/syz_mount_image_btrfs_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_23:1
error: sys/linux/test/syz_mount_image_btrfs_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_24:1
error: sys/linux/test/syz_mount_image_btrfs_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_25:1
error: sys/linux/test/syz_mount_image_btrfs_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_26:1
error: sys/linux/test/syz_mount_image_btrfs_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_27:1
error: sys/linux/test/syz_mount_image_btrfs_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_28:1
error: sys/linux/test/syz_mount_image_btrfs_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_29:1
error: sys/linux/test/syz_mount_image_btrfs_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_3:1
error: sys/linux/test/syz_mount_image_btrfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_30:1
error: sys/linux/test/syz_mount_image_btrfs_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_31:1
error: sys/linux/test/syz_mount_image_btrfs_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_32:1
error: sys/linux/test/syz_mount_image_btrfs_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_33:1
error: sys/linux/test/syz_mount_image_btrfs_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_34:1
error: sys/linux/test/syz_mount_image_btrfs_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_35:1
error: sys/linux/test/syz_mount_image_btrfs_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_36:1
error: sys/linux/test/syz_mount_image_btrfs_36: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_37:1
error: sys/linux/test/syz_mount_image_btrfs_37: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_38:1
error: sys/linux/test/syz_mount_image_btrfs_38: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_39:1
error: sys/linux/test/syz_mount_image_btrfs_39: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_4:1
error: sys/linux/test/syz_mount_image_btrfs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_40:1
error: sys/linux/test/syz_mount_image_btrfs_40: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_41:1
error: sys/linux/test/syz_mount_image_btrfs_41: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_42:1
error: sys/linux/test/syz_mount_image_btrfs_42: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_43:1
error: sys/linux/test/syz_mount_image_btrfs_43: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_44:1
error: sys/linux/test/syz_mount_image_btrfs_44: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_45:1
error: sys/linux/test/syz_mount_image_btrfs_45: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_46:1
error: sys/linux/test/syz_mount_image_btrfs_46: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_47:1
error: sys/linux/test/syz_mount_image_btrfs_47: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_48:1
error: sys/linux/test/syz_mount_image_btrfs_48: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_49:1
error: sys/linux/test/syz_mount_image_btrfs_49: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_5:1
error: sys/linux/test/syz_mount_image_btrfs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_50:1
error: sys/linux/test/syz_mount_image_btrfs_50: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_51:1
error: sys/linux/test/syz_mount_image_btrfs_51: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_52:1
error: sys/linux/test/syz_mount_image_btrfs_52: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_53:1
error: sys/linux/test/syz_mount_image_btrfs_53: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_54:1
error: sys/linux/test/syz_mount_image_btrfs_54: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_55:1
error: sys/linux/test/syz_mount_image_btrfs_55: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_56:1
error: sys/linux/test/syz_mount_image_btrfs_56: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_57:1
error: sys/linux/test/syz_mount_image_btrfs_57: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_58:1
error: sys/linux/test/syz_mount_image_btrfs_58: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_59:1
error: sys/linux/test/syz_mount_image_btrfs_59: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_6:1
error: sys/linux/test/syz_mount_image_btrfs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_60:1
error: sys/linux/test/syz_mount_image_btrfs_60: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_61:1
error: sys/linux/test/syz_mount_image_btrfs_61: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_62:1
error: sys/linux/test/syz_mount_image_btrfs_62: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_63:1
error: sys/linux/test/syz_mount_image_btrfs_63: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_64:1
error: sys/linux/test/syz_mount_image_btrfs_64: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_65:1
error: sys/linux/test/syz_mount_image_btrfs_65: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_66:1
error: sys/linux/test/syz_mount_image_btrfs_66: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_67:1
error: sys/linux/test/syz_mount_image_btrfs_67: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_68:1
error: sys/linux/test/syz_mount_image_btrfs_68: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_69:1
error: sys/linux/test/syz_mount_image_btrfs_69: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_7:1
error: sys/linux/test/syz_mount_image_btrfs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_70:1
error: sys/linux/test/syz_mount_image_btrfs_70: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_71:1
error: sys/linux/test/syz_mount_image_btrfs_71: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_72:1
error: sys/linux/test/syz_mount_image_btrfs_72: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_73:1
error: sys/linux/test/syz_mount_image_btrfs_73: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_74:1
error: sys/linux/test/syz_mount_image_btrfs_74: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_75:1
error: sys/linux/test/syz_mount_image_btrfs_75: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_76:1
error: sys/linux/test/syz_mount_image_btrfs_76: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_77:1
error: sys/linux/test/syz_mount_image_btrfs_77: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_78:1
error: sys/linux/test/syz_mount_image_btrfs_78: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_79:1
error: sys/linux/test/syz_mount_image_btrfs_79: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_8:1
error: sys/linux/test/syz_mount_image_btrfs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_btrfs_9:1
error: sys/linux/test/syz_mount_image_btrfs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_cramfs_0:1
error: sys/linux/test/syz_mount_image_cramfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_cramfs_1:1
error: sys/linux/test/syz_mount_image_cramfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_cramfs_2:1
error: sys/linux/test/syz_mount_image_cramfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_cramfs_3:1
error: sys/linux/test/syz_mount_image_cramfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_0:1
error: sys/linux/test/syz_mount_image_efs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_1:1
error: sys/linux/test/syz_mount_image_efs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_10:1
error: sys/linux/test/syz_mount_image_efs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_11:1
error: sys/linux/test/syz_mount_image_efs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_12:1
error: sys/linux/test/syz_mount_image_efs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_13:1
error: sys/linux/test/syz_mount_image_efs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_2:1
error: sys/linux/test/syz_mount_image_efs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_3:1
error: sys/linux/test/syz_mount_image_efs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_4:1
error: sys/linux/test/syz_mount_image_efs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_5:1
error: sys/linux/test/syz_mount_image_efs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_6:1
error: sys/linux/test/syz_mount_image_efs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_7:1
error: sys/linux/test/syz_mount_image_efs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_8:1
error: sys/linux/test/syz_mount_image_efs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_efs_9:1
error: sys/linux/test/syz_mount_image_efs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_0:1
error: sys/linux/test/syz_mount_image_erofs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_1:1
error: sys/linux/test/syz_mount_image_erofs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_10:1
error: sys/linux/test/syz_mount_image_erofs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_11:1
error: sys/linux/test/syz_mount_image_erofs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_12:1
error: sys/linux/test/syz_mount_image_erofs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_13:1
error: sys/linux/test/syz_mount_image_erofs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_14:1
error: sys/linux/test/syz_mount_image_erofs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_15:1
error: sys/linux/test/syz_mount_image_erofs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_2:1
error: sys/linux/test/syz_mount_image_erofs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_3:1
error: sys/linux/test/syz_mount_image_erofs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_4:1
error: sys/linux/test/syz_mount_image_erofs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_5:1
error: sys/linux/test/syz_mount_image_erofs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_6:1
error: sys/linux/test/syz_mount_image_erofs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_7:1
error: sys/linux/test/syz_mount_image_erofs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_8:1
error: sys/linux/test/syz_mount_image_erofs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_erofs_9:1
error: sys/linux/test/syz_mount_image_erofs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_exfat_0:1
error: sys/linux/test/syz_mount_image_exfat_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_exfat_1:1
error: sys/linux/test/syz_mount_image_exfat_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_0:1
error: sys/linux/test/syz_mount_image_ext4_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_1:1
error: sys/linux/test/syz_mount_image_ext4_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_10:1
error: sys/linux/test/syz_mount_image_ext4_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_11:1
error: sys/linux/test/syz_mount_image_ext4_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_12:1
error: sys/linux/test/syz_mount_image_ext4_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_13:1
error: sys/linux/test/syz_mount_image_ext4_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_14:1
error: sys/linux/test/syz_mount_image_ext4_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_15:1
error: sys/linux/test/syz_mount_image_ext4_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_16:1
error: sys/linux/test/syz_mount_image_ext4_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_17:1
error: sys/linux/test/syz_mount_image_ext4_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_18:1
error: sys/linux/test/syz_mount_image_ext4_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_19:1
error: sys/linux/test/syz_mount_image_ext4_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_2:1
error: sys/linux/test/syz_mount_image_ext4_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_20:1
error: sys/linux/test/syz_mount_image_ext4_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_21:1
error: sys/linux/test/syz_mount_image_ext4_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_22:1
error: sys/linux/test/syz_mount_image_ext4_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_23:1
error: sys/linux/test/syz_mount_image_ext4_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_24:1
error: sys/linux/test/syz_mount_image_ext4_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_25:1
error: sys/linux/test/syz_mount_image_ext4_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_26:1
error: sys/linux/test/syz_mount_image_ext4_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_27:1
error: sys/linux/test/syz_mount_image_ext4_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_28:1
error: sys/linux/test/syz_mount_image_ext4_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_29:1
error: sys/linux/test/syz_mount_image_ext4_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_3:1
error: sys/linux/test/syz_mount_image_ext4_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_30:1
error: sys/linux/test/syz_mount_image_ext4_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_31:1
error: sys/linux/test/syz_mount_image_ext4_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_32:1
error: sys/linux/test/syz_mount_image_ext4_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_33:1
error: sys/linux/test/syz_mount_image_ext4_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_34:1
error: sys/linux/test/syz_mount_image_ext4_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_35:1
error: sys/linux/test/syz_mount_image_ext4_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_36:1
error: sys/linux/test/syz_mount_image_ext4_36: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_37:1
error: sys/linux/test/syz_mount_image_ext4_37: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_38:1
error: sys/linux/test/syz_mount_image_ext4_38: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_39:1
error: sys/linux/test/syz_mount_image_ext4_39: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_4:1
error: sys/linux/test/syz_mount_image_ext4_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_40:1
error: sys/linux/test/syz_mount_image_ext4_40: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_41:1
error: sys/linux/test/syz_mount_image_ext4_41: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_42:1
error: sys/linux/test/syz_mount_image_ext4_42: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_43:1
error: sys/linux/test/syz_mount_image_ext4_43: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_44:1
error: sys/linux/test/syz_mount_image_ext4_44: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_45:1
error: sys/linux/test/syz_mount_image_ext4_45: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_46:1
error: sys/linux/test/syz_mount_image_ext4_46: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_47:1
error: sys/linux/test/syz_mount_image_ext4_47: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_48:1
error: sys/linux/test/syz_mount_image_ext4_48: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_49:1
error: sys/linux/test/syz_mount_image_ext4_49: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_5:1
error: sys/linux/test/syz_mount_image_ext4_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_50:1
error: sys/linux/test/syz_mount_image_ext4_50: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_51:1
error: sys/linux/test/syz_mount_image_ext4_51: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_52:1
error: sys/linux/test/syz_mount_image_ext4_52: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_53:1
error: sys/linux/test/syz_mount_image_ext4_53: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_54:1
error: sys/linux/test/syz_mount_image_ext4_54: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_55:1
error: sys/linux/test/syz_mount_image_ext4_55: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_56:1
error: sys/linux/test/syz_mount_image_ext4_56: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_57:1
error: sys/linux/test/syz_mount_image_ext4_57: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_58:1
error: sys/linux/test/syz_mount_image_ext4_58: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_59:1
error: sys/linux/test/syz_mount_image_ext4_59: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_6:1
error: sys/linux/test/syz_mount_image_ext4_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_60:1
error: sys/linux/test/syz_mount_image_ext4_60: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_61:1
error: sys/linux/test/syz_mount_image_ext4_61: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_62:1
error: sys/linux/test/syz_mount_image_ext4_62: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_7:1
error: sys/linux/test/syz_mount_image_ext4_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_8:1
error: sys/linux/test/syz_mount_image_ext4_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ext4_9:1
error: sys/linux/test/syz_mount_image_ext4_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_0:1
error: sys/linux/test/syz_mount_image_f2fs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_1:1
error: sys/linux/test/syz_mount_image_f2fs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_10:1
error: sys/linux/test/syz_mount_image_f2fs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_11:1
error: sys/linux/test/syz_mount_image_f2fs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_12:1
error: sys/linux/test/syz_mount_image_f2fs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_13:1
error: sys/linux/test/syz_mount_image_f2fs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_14:1
error: sys/linux/test/syz_mount_image_f2fs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_15:1
error: sys/linux/test/syz_mount_image_f2fs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_16:1
error: sys/linux/test/syz_mount_image_f2fs_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_17:1
error: sys/linux/test/syz_mount_image_f2fs_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_18:1
error: sys/linux/test/syz_mount_image_f2fs_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_19:1
error: sys/linux/test/syz_mount_image_f2fs_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_2:1
error: sys/linux/test/syz_mount_image_f2fs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_20:1
error: sys/linux/test/syz_mount_image_f2fs_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_21:1
error: sys/linux/test/syz_mount_image_f2fs_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_22:1
error: sys/linux/test/syz_mount_image_f2fs_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_23:1
error: sys/linux/test/syz_mount_image_f2fs_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_24:1
error: sys/linux/test/syz_mount_image_f2fs_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_25:1
error: sys/linux/test/syz_mount_image_f2fs_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_26:1
error: sys/linux/test/syz_mount_image_f2fs_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_27:1
error: sys/linux/test/syz_mount_image_f2fs_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_28:1
error: sys/linux/test/syz_mount_image_f2fs_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_29:1
error: sys/linux/test/syz_mount_image_f2fs_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_3:1
error: sys/linux/test/syz_mount_image_f2fs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_30:1
error: sys/linux/test/syz_mount_image_f2fs_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_31:1
error: sys/linux/test/syz_mount_image_f2fs_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_4:1
error: sys/linux/test/syz_mount_image_f2fs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_5:1
error: sys/linux/test/syz_mount_image_f2fs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_6:1
error: sys/linux/test/syz_mount_image_f2fs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_7:1
error: sys/linux/test/syz_mount_image_f2fs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_8:1
error: sys/linux/test/syz_mount_image_f2fs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_f2fs_9:1
error: sys/linux/test/syz_mount_image_f2fs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_fuse:1
error: sys/linux/test/syz_mount_image_fuse: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_0:1
error: sys/linux/test/syz_mount_image_gfs2_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_1:1
error: sys/linux/test/syz_mount_image_gfs2_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_10:1
error: sys/linux/test/syz_mount_image_gfs2_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_11:1
error: sys/linux/test/syz_mount_image_gfs2_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_12:1
error: sys/linux/test/syz_mount_image_gfs2_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_13:1
error: sys/linux/test/syz_mount_image_gfs2_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_14:1
error: sys/linux/test/syz_mount_image_gfs2_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_15:1
error: sys/linux/test/syz_mount_image_gfs2_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_16:1
error: sys/linux/test/syz_mount_image_gfs2_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_17:1
error: sys/linux/test/syz_mount_image_gfs2_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_18:1
error: sys/linux/test/syz_mount_image_gfs2_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_19:1
error: sys/linux/test/syz_mount_image_gfs2_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_2:1
error: sys/linux/test/syz_mount_image_gfs2_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_20:1
error: sys/linux/test/syz_mount_image_gfs2_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_21:1
error: sys/linux/test/syz_mount_image_gfs2_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_22:1
error: sys/linux/test/syz_mount_image_gfs2_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_23:1
error: sys/linux/test/syz_mount_image_gfs2_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_24:1
error: sys/linux/test/syz_mount_image_gfs2_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_25:1
error: sys/linux/test/syz_mount_image_gfs2_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_26:1
error: sys/linux/test/syz_mount_image_gfs2_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_27:1
error: sys/linux/test/syz_mount_image_gfs2_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_28:1
error: sys/linux/test/syz_mount_image_gfs2_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_29:1
error: sys/linux/test/syz_mount_image_gfs2_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_3:1
error: sys/linux/test/syz_mount_image_gfs2_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_30:1
error: sys/linux/test/syz_mount_image_gfs2_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_31:1
error: sys/linux/test/syz_mount_image_gfs2_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_4:1
error: sys/linux/test/syz_mount_image_gfs2_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_5:1
error: sys/linux/test/syz_mount_image_gfs2_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_6:1
error: sys/linux/test/syz_mount_image_gfs2_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_7:1
error: sys/linux/test/syz_mount_image_gfs2_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_8:1
error: sys/linux/test/syz_mount_image_gfs2_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_gfs2_9:1
error: sys/linux/test/syz_mount_image_gfs2_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_0:1
error: sys/linux/test/syz_mount_image_iso9660_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_1:1
error: sys/linux/test/syz_mount_image_iso9660_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_10:1
error: sys/linux/test/syz_mount_image_iso9660_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_11:1
error: sys/linux/test/syz_mount_image_iso9660_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_12:1
error: sys/linux/test/syz_mount_image_iso9660_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_13:1
error: sys/linux/test/syz_mount_image_iso9660_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_14:1
error: sys/linux/test/syz_mount_image_iso9660_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_15:1
error: sys/linux/test/syz_mount_image_iso9660_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_16:1
error: sys/linux/test/syz_mount_image_iso9660_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_17:1
error: sys/linux/test/syz_mount_image_iso9660_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_2:1
error: sys/linux/test/syz_mount_image_iso9660_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_3:1
error: sys/linux/test/syz_mount_image_iso9660_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_4:1
error: sys/linux/test/syz_mount_image_iso9660_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_5:1
error: sys/linux/test/syz_mount_image_iso9660_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_6:1
error: sys/linux/test/syz_mount_image_iso9660_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_7:1
error: sys/linux/test/syz_mount_image_iso9660_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_8:1
error: sys/linux/test/syz_mount_image_iso9660_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_iso9660_9:1
error: sys/linux/test/syz_mount_image_iso9660_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_0:1
error: sys/linux/test/syz_mount_image_jffs2_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_1:1
error: sys/linux/test/syz_mount_image_jffs2_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_2:1
error: sys/linux/test/syz_mount_image_jffs2_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_3:1
error: sys/linux/test/syz_mount_image_jffs2_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_4:1
error: sys/linux/test/syz_mount_image_jffs2_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_5:1
error: sys/linux/test/syz_mount_image_jffs2_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_6:1
error: sys/linux/test/syz_mount_image_jffs2_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jffs2_7:1
error: sys/linux/test/syz_mount_image_jffs2_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jfs_0:1
error: sys/linux/test/syz_mount_image_jfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jfs_1:1
error: sys/linux/test/syz_mount_image_jfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jfs_2:1
error: sys/linux/test/syz_mount_image_jfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_jfs_3:1
error: sys/linux/test/syz_mount_image_jfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_0:1
error: sys/linux/test/syz_mount_image_minix_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_1:1
error: sys/linux/test/syz_mount_image_minix_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_10:1
error: sys/linux/test/syz_mount_image_minix_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_11:1
error: sys/linux/test/syz_mount_image_minix_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_12:1
error: sys/linux/test/syz_mount_image_minix_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_13:1
error: sys/linux/test/syz_mount_image_minix_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_14:1
error: sys/linux/test/syz_mount_image_minix_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_2:1
error: sys/linux/test/syz_mount_image_minix_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_3:1
error: sys/linux/test/syz_mount_image_minix_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_4:1
error: sys/linux/test/syz_mount_image_minix_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_5:1
error: sys/linux/test/syz_mount_image_minix_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_6:1
error: sys/linux/test/syz_mount_image_minix_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_7:1
error: sys/linux/test/syz_mount_image_minix_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_8:1
error: sys/linux/test/syz_mount_image_minix_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_minix_9:1
error: sys/linux/test/syz_mount_image_minix_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_0:1
error: sys/linux/test/syz_mount_image_nilfs2_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_1:1
error: sys/linux/test/syz_mount_image_nilfs2_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_10:1
error: sys/linux/test/syz_mount_image_nilfs2_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_11:1
error: sys/linux/test/syz_mount_image_nilfs2_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_12:1
error: sys/linux/test/syz_mount_image_nilfs2_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_13:1
error: sys/linux/test/syz_mount_image_nilfs2_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_14:1
error: sys/linux/test/syz_mount_image_nilfs2_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_15:1
error: sys/linux/test/syz_mount_image_nilfs2_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_16:1
error: sys/linux/test/syz_mount_image_nilfs2_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_17:1
error: sys/linux/test/syz_mount_image_nilfs2_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_2:1
error: sys/linux/test/syz_mount_image_nilfs2_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_3:1
error: sys/linux/test/syz_mount_image_nilfs2_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_4:1
error: sys/linux/test/syz_mount_image_nilfs2_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_5:1
error: sys/linux/test/syz_mount_image_nilfs2_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_6:1
error: sys/linux/test/syz_mount_image_nilfs2_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_7:1
error: sys/linux/test/syz_mount_image_nilfs2_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_8:1
error: sys/linux/test/syz_mount_image_nilfs2_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_nilfs2_9:1
error: sys/linux/test/syz_mount_image_nilfs2_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_10:1
error: sys/linux/test/syz_mount_image_ntfs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_11:1
error: sys/linux/test/syz_mount_image_ntfs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_12:1
error: sys/linux/test/syz_mount_image_ntfs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_13:1
error: sys/linux/test/syz_mount_image_ntfs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_14:1
error: sys/linux/test/syz_mount_image_ntfs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_15:1
error: sys/linux/test/syz_mount_image_ntfs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_16:1
error: sys/linux/test/syz_mount_image_ntfs_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_17:1
error: sys/linux/test/syz_mount_image_ntfs_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_18:1
error: sys/linux/test/syz_mount_image_ntfs_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_19:1
error: sys/linux/test/syz_mount_image_ntfs_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_2:1
error: sys/linux/test/syz_mount_image_ntfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_3:1
error: sys/linux/test/syz_mount_image_ntfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_4:1
error: sys/linux/test/syz_mount_image_ntfs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_5:1
error: sys/linux/test/syz_mount_image_ntfs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_6:1
error: sys/linux/test/syz_mount_image_ntfs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_7:1
error: sys/linux/test/syz_mount_image_ntfs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_8:1
error: sys/linux/test/syz_mount_image_ntfs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ntfs_9:1
error: sys/linux/test/syz_mount_image_ntfs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_0:1
error: sys/linux/test/syz_mount_image_ocfs2_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_1:1
error: sys/linux/test/syz_mount_image_ocfs2_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_10:1
error: sys/linux/test/syz_mount_image_ocfs2_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_11:1
error: sys/linux/test/syz_mount_image_ocfs2_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_12:1
error: sys/linux/test/syz_mount_image_ocfs2_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_13:1
error: sys/linux/test/syz_mount_image_ocfs2_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_14:1
error: sys/linux/test/syz_mount_image_ocfs2_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_15:1
error: sys/linux/test/syz_mount_image_ocfs2_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_16:1
error: sys/linux/test/syz_mount_image_ocfs2_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_17:1
error: sys/linux/test/syz_mount_image_ocfs2_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_18:1
error: sys/linux/test/syz_mount_image_ocfs2_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_19:1
error: sys/linux/test/syz_mount_image_ocfs2_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_2:1
error: sys/linux/test/syz_mount_image_ocfs2_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_20:1
error: sys/linux/test/syz_mount_image_ocfs2_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_21:1
error: sys/linux/test/syz_mount_image_ocfs2_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_22:1
error: sys/linux/test/syz_mount_image_ocfs2_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_23:1
error: sys/linux/test/syz_mount_image_ocfs2_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_24:1
error: sys/linux/test/syz_mount_image_ocfs2_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_25:1
error: sys/linux/test/syz_mount_image_ocfs2_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_26:1
error: sys/linux/test/syz_mount_image_ocfs2_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_27:1
error: sys/linux/test/syz_mount_image_ocfs2_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_28:1
error: sys/linux/test/syz_mount_image_ocfs2_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_29:1
error: sys/linux/test/syz_mount_image_ocfs2_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_3:1
error: sys/linux/test/syz_mount_image_ocfs2_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_30:1
error: sys/linux/test/syz_mount_image_ocfs2_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_31:1
error: sys/linux/test/syz_mount_image_ocfs2_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_32:1
error: sys/linux/test/syz_mount_image_ocfs2_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_33:1
error: sys/linux/test/syz_mount_image_ocfs2_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_34:1
error: sys/linux/test/syz_mount_image_ocfs2_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_35:1
error: sys/linux/test/syz_mount_image_ocfs2_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_36:1
error: sys/linux/test/syz_mount_image_ocfs2_36: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_37:1
error: sys/linux/test/syz_mount_image_ocfs2_37: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_38:1
error: sys/linux/test/syz_mount_image_ocfs2_38: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_39:1
error: sys/linux/test/syz_mount_image_ocfs2_39: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_4:1
error: sys/linux/test/syz_mount_image_ocfs2_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_40:1
error: sys/linux/test/syz_mount_image_ocfs2_40: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_41:1
error: sys/linux/test/syz_mount_image_ocfs2_41: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_42:1
error: sys/linux/test/syz_mount_image_ocfs2_42: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_43:1
error: sys/linux/test/syz_mount_image_ocfs2_43: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_44:1
error: sys/linux/test/syz_mount_image_ocfs2_44: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_45:1
error: sys/linux/test/syz_mount_image_ocfs2_45: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_46:1
error: sys/linux/test/syz_mount_image_ocfs2_46: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_47:1
error: sys/linux/test/syz_mount_image_ocfs2_47: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_48:1
error: sys/linux/test/syz_mount_image_ocfs2_48: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_49:1
error: sys/linux/test/syz_mount_image_ocfs2_49: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_5:1
error: sys/linux/test/syz_mount_image_ocfs2_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_50:1
error: sys/linux/test/syz_mount_image_ocfs2_50: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_51:1
error: sys/linux/test/syz_mount_image_ocfs2_51: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_52:1
error: sys/linux/test/syz_mount_image_ocfs2_52: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_53:1
error: sys/linux/test/syz_mount_image_ocfs2_53: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_54:1
error: sys/linux/test/syz_mount_image_ocfs2_54: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_55:1
error: sys/linux/test/syz_mount_image_ocfs2_55: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_56:1
error: sys/linux/test/syz_mount_image_ocfs2_56: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_57:1
error: sys/linux/test/syz_mount_image_ocfs2_57: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_58:1
error: sys/linux/test/syz_mount_image_ocfs2_58: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_59:1
error: sys/linux/test/syz_mount_image_ocfs2_59: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_6:1
error: sys/linux/test/syz_mount_image_ocfs2_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_60:1
error: sys/linux/test/syz_mount_image_ocfs2_60: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_61:1
error: sys/linux/test/syz_mount_image_ocfs2_61: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_62:1
error: sys/linux/test/syz_mount_image_ocfs2_62: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_63:1
error: sys/linux/test/syz_mount_image_ocfs2_63: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_64:1
error: sys/linux/test/syz_mount_image_ocfs2_64: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_65:1
error: sys/linux/test/syz_mount_image_ocfs2_65: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_66:1
error: sys/linux/test/syz_mount_image_ocfs2_66: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_67:1
error: sys/linux/test/syz_mount_image_ocfs2_67: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_68:1
error: sys/linux/test/syz_mount_image_ocfs2_68: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_69:1
error: sys/linux/test/syz_mount_image_ocfs2_69: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_7:1
error: sys/linux/test/syz_mount_image_ocfs2_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_70:1
error: sys/linux/test/syz_mount_image_ocfs2_70: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_71:1
error: sys/linux/test/syz_mount_image_ocfs2_71: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_8:1
error: sys/linux/test/syz_mount_image_ocfs2_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_ocfs2_9:1
error: sys/linux/test/syz_mount_image_ocfs2_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_0:1
error: sys/linux/test/syz_mount_image_reiserfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_1:1
error: sys/linux/test/syz_mount_image_reiserfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_10:1
error: sys/linux/test/syz_mount_image_reiserfs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_11:1
error: sys/linux/test/syz_mount_image_reiserfs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_12:1
error: sys/linux/test/syz_mount_image_reiserfs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_13:1
error: sys/linux/test/syz_mount_image_reiserfs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_14:1
error: sys/linux/test/syz_mount_image_reiserfs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_15:1
error: sys/linux/test/syz_mount_image_reiserfs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_16:1
error: sys/linux/test/syz_mount_image_reiserfs_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_17:1
error: sys/linux/test/syz_mount_image_reiserfs_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_18:1
error: sys/linux/test/syz_mount_image_reiserfs_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_19:1
error: sys/linux/test/syz_mount_image_reiserfs_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_2:1
error: sys/linux/test/syz_mount_image_reiserfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_20:1
error: sys/linux/test/syz_mount_image_reiserfs_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_21:1
error: sys/linux/test/syz_mount_image_reiserfs_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_22:1
error: sys/linux/test/syz_mount_image_reiserfs_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_23:1
error: sys/linux/test/syz_mount_image_reiserfs_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_24:1
error: sys/linux/test/syz_mount_image_reiserfs_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_25:1
error: sys/linux/test/syz_mount_image_reiserfs_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_26:1
error: sys/linux/test/syz_mount_image_reiserfs_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_27:1
error: sys/linux/test/syz_mount_image_reiserfs_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_28:1
error: sys/linux/test/syz_mount_image_reiserfs_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_29:1
error: sys/linux/test/syz_mount_image_reiserfs_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_3:1
error: sys/linux/test/syz_mount_image_reiserfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_30:1
error: sys/linux/test/syz_mount_image_reiserfs_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_31:1
error: sys/linux/test/syz_mount_image_reiserfs_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_32:1
error: sys/linux/test/syz_mount_image_reiserfs_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_33:1
error: sys/linux/test/syz_mount_image_reiserfs_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_34:1
error: sys/linux/test/syz_mount_image_reiserfs_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_35:1
error: sys/linux/test/syz_mount_image_reiserfs_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_36:1
error: sys/linux/test/syz_mount_image_reiserfs_36: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_37:1
error: sys/linux/test/syz_mount_image_reiserfs_37: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_38:1
error: sys/linux/test/syz_mount_image_reiserfs_38: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_39:1
error: sys/linux/test/syz_mount_image_reiserfs_39: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_4:1
error: sys/linux/test/syz_mount_image_reiserfs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_40:1
error: sys/linux/test/syz_mount_image_reiserfs_40: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_41:1
error: sys/linux/test/syz_mount_image_reiserfs_41: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_42:1
error: sys/linux/test/syz_mount_image_reiserfs_42: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_43:1
error: sys/linux/test/syz_mount_image_reiserfs_43: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_44:1
error: sys/linux/test/syz_mount_image_reiserfs_44: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_45:1
error: sys/linux/test/syz_mount_image_reiserfs_45: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_46:1
error: sys/linux/test/syz_mount_image_reiserfs_46: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_47:1
error: sys/linux/test/syz_mount_image_reiserfs_47: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_48:1
error: sys/linux/test/syz_mount_image_reiserfs_48: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_49:1
error: sys/linux/test/syz_mount_image_reiserfs_49: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_5:1
error: sys/linux/test/syz_mount_image_reiserfs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_50:1
error: sys/linux/test/syz_mount_image_reiserfs_50: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_51:1
error: sys/linux/test/syz_mount_image_reiserfs_51: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_52:1
error: sys/linux/test/syz_mount_image_reiserfs_52: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_53:1
error: sys/linux/test/syz_mount_image_reiserfs_53: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_54:1
error: sys/linux/test/syz_mount_image_reiserfs_54: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_55:1
error: sys/linux/test/syz_mount_image_reiserfs_55: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_56:1
error: sys/linux/test/syz_mount_image_reiserfs_56: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_57:1
error: sys/linux/test/syz_mount_image_reiserfs_57: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_58:1
error: sys/linux/test/syz_mount_image_reiserfs_58: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_59:1
error: sys/linux/test/syz_mount_image_reiserfs_59: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_6:1
error: sys/linux/test/syz_mount_image_reiserfs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_7:1
error: sys/linux/test/syz_mount_image_reiserfs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_8:1
error: sys/linux/test/syz_mount_image_reiserfs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_reiserfs_9:1
error: sys/linux/test/syz_mount_image_reiserfs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_romfs_0:1
error: sys/linux/test/syz_mount_image_romfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_romfs_1:1
error: sys/linux/test/syz_mount_image_romfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_0:1
error: sys/linux/test/syz_mount_image_squashfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_1:1
error: sys/linux/test/syz_mount_image_squashfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_10:1
error: sys/linux/test/syz_mount_image_squashfs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_11:1
error: sys/linux/test/syz_mount_image_squashfs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_12:1
error: sys/linux/test/syz_mount_image_squashfs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_13:1
error: sys/linux/test/syz_mount_image_squashfs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_14:1
error: sys/linux/test/syz_mount_image_squashfs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_15:1
error: sys/linux/test/syz_mount_image_squashfs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_16:1
error: sys/linux/test/syz_mount_image_squashfs_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_17:1
error: sys/linux/test/syz_mount_image_squashfs_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_2:1
error: sys/linux/test/syz_mount_image_squashfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_3:1
error: sys/linux/test/syz_mount_image_squashfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_4:1
error: sys/linux/test/syz_mount_image_squashfs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_5:1
error: sys/linux/test/syz_mount_image_squashfs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_6:1
error: sys/linux/test/syz_mount_image_squashfs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_7:1
error: sys/linux/test/syz_mount_image_squashfs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_8:1
error: sys/linux/test/syz_mount_image_squashfs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_squashfs_9:1
error: sys/linux/test/syz_mount_image_squashfs_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_0:1
error: sys/linux/test/syz_mount_image_udf_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_1:1
error: sys/linux/test/syz_mount_image_udf_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_10:1
error: sys/linux/test/syz_mount_image_udf_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_11:1
error: sys/linux/test/syz_mount_image_udf_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_12:1
error: sys/linux/test/syz_mount_image_udf_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_13:1
error: sys/linux/test/syz_mount_image_udf_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_14:1
error: sys/linux/test/syz_mount_image_udf_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_15:1
error: sys/linux/test/syz_mount_image_udf_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_16:1
error: sys/linux/test/syz_mount_image_udf_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_17:1
error: sys/linux/test/syz_mount_image_udf_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_18:1
error: sys/linux/test/syz_mount_image_udf_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_19:1
error: sys/linux/test/syz_mount_image_udf_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_2:1
error: sys/linux/test/syz_mount_image_udf_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_20:1
error: sys/linux/test/syz_mount_image_udf_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_21:1
error: sys/linux/test/syz_mount_image_udf_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_22:1
error: sys/linux/test/syz_mount_image_udf_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_23:1
error: sys/linux/test/syz_mount_image_udf_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_24:1
error: sys/linux/test/syz_mount_image_udf_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_25:1
error: sys/linux/test/syz_mount_image_udf_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_26:1
error: sys/linux/test/syz_mount_image_udf_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_27:1
error: sys/linux/test/syz_mount_image_udf_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_28:1
error: sys/linux/test/syz_mount_image_udf_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_29:1
error: sys/linux/test/syz_mount_image_udf_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_3:1
error: sys/linux/test/syz_mount_image_udf_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_30:1
error: sys/linux/test/syz_mount_image_udf_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_31:1
error: sys/linux/test/syz_mount_image_udf_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_32:1
error: sys/linux/test/syz_mount_image_udf_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_33:1
error: sys/linux/test/syz_mount_image_udf_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_34:1
error: sys/linux/test/syz_mount_image_udf_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_35:1
error: sys/linux/test/syz_mount_image_udf_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_36:1
error: sys/linux/test/syz_mount_image_udf_36: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_37:1
error: sys/linux/test/syz_mount_image_udf_37: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_38:1
error: sys/linux/test/syz_mount_image_udf_38: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_39:1
error: sys/linux/test/syz_mount_image_udf_39: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_4:1
error: sys/linux/test/syz_mount_image_udf_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_40:1
error: sys/linux/test/syz_mount_image_udf_40: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_41:1
error: sys/linux/test/syz_mount_image_udf_41: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_42:1
error: sys/linux/test/syz_mount_image_udf_42: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_43:1
error: sys/linux/test/syz_mount_image_udf_43: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_44:1
error: sys/linux/test/syz_mount_image_udf_44: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_45:1
error: sys/linux/test/syz_mount_image_udf_45: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_46:1
error: sys/linux/test/syz_mount_image_udf_46: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_47:1
error: sys/linux/test/syz_mount_image_udf_47: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_48:1
error: sys/linux/test/syz_mount_image_udf_48: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_49:1
error: sys/linux/test/syz_mount_image_udf_49: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_5:1
error: sys/linux/test/syz_mount_image_udf_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_50:1
error: sys/linux/test/syz_mount_image_udf_50: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_51:1
error: sys/linux/test/syz_mount_image_udf_51: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_52:1
error: sys/linux/test/syz_mount_image_udf_52: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_53:1
error: sys/linux/test/syz_mount_image_udf_53: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_54:1
error: sys/linux/test/syz_mount_image_udf_54: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_55:1
error: sys/linux/test/syz_mount_image_udf_55: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_56:1
error: sys/linux/test/syz_mount_image_udf_56: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_6:1
error: sys/linux/test/syz_mount_image_udf_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_7:1
error: sys/linux/test/syz_mount_image_udf_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_8:1
error: sys/linux/test/syz_mount_image_udf_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_udf_9:1
error: sys/linux/test/syz_mount_image_udf_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_0:1
error: sys/linux/test/syz_mount_image_vfat_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_1:1
error: sys/linux/test/syz_mount_image_vfat_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_10:1
error: sys/linux/test/syz_mount_image_vfat_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_11:1
error: sys/linux/test/syz_mount_image_vfat_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_12:1
error: sys/linux/test/syz_mount_image_vfat_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_13:1
error: sys/linux/test/syz_mount_image_vfat_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_14:1
error: sys/linux/test/syz_mount_image_vfat_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_15:1
error: sys/linux/test/syz_mount_image_vfat_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_16:1
error: sys/linux/test/syz_mount_image_vfat_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_17:1
error: sys/linux/test/syz_mount_image_vfat_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_18:1
error: sys/linux/test/syz_mount_image_vfat_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_19:1
error: sys/linux/test/syz_mount_image_vfat_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_2:1
error: sys/linux/test/syz_mount_image_vfat_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_20:1
error: sys/linux/test/syz_mount_image_vfat_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_21:1
error: sys/linux/test/syz_mount_image_vfat_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_22:1
error: sys/linux/test/syz_mount_image_vfat_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_23:1
error: sys/linux/test/syz_mount_image_vfat_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_24:1
error: sys/linux/test/syz_mount_image_vfat_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_25:1
error: sys/linux/test/syz_mount_image_vfat_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_26:1
error: sys/linux/test/syz_mount_image_vfat_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_27:1
error: sys/linux/test/syz_mount_image_vfat_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_28:1
error: sys/linux/test/syz_mount_image_vfat_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_29:1
error: sys/linux/test/syz_mount_image_vfat_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_3:1
error: sys/linux/test/syz_mount_image_vfat_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_30:1
error: sys/linux/test/syz_mount_image_vfat_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_31:1
error: sys/linux/test/syz_mount_image_vfat_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_32:1
error: sys/linux/test/syz_mount_image_vfat_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_33:1
error: sys/linux/test/syz_mount_image_vfat_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_34:1
error: sys/linux/test/syz_mount_image_vfat_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_35:1
error: sys/linux/test/syz_mount_image_vfat_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_36:1
error: sys/linux/test/syz_mount_image_vfat_36: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_37:1
error: sys/linux/test/syz_mount_image_vfat_37: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_38:1
error: sys/linux/test/syz_mount_image_vfat_38: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_39:1
error: sys/linux/test/syz_mount_image_vfat_39: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_4:1
error: sys/linux/test/syz_mount_image_vfat_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_40:1
error: sys/linux/test/syz_mount_image_vfat_40: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_41:1
error: sys/linux/test/syz_mount_image_vfat_41: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_42:1
error: sys/linux/test/syz_mount_image_vfat_42: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_43:1
error: sys/linux/test/syz_mount_image_vfat_43: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_44:1
error: sys/linux/test/syz_mount_image_vfat_44: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_45:1
error: sys/linux/test/syz_mount_image_vfat_45: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_46:1
error: sys/linux/test/syz_mount_image_vfat_46: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_47:1
error: sys/linux/test/syz_mount_image_vfat_47: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_48:1
error: sys/linux/test/syz_mount_image_vfat_48: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_49:1
error: sys/linux/test/syz_mount_image_vfat_49: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_5:1
error: sys/linux/test/syz_mount_image_vfat_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_50:1
error: sys/linux/test/syz_mount_image_vfat_50: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_51:1
error: sys/linux/test/syz_mount_image_vfat_51: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_52:1
error: sys/linux/test/syz_mount_image_vfat_52: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_53:1
error: sys/linux/test/syz_mount_image_vfat_53: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_54:1
error: sys/linux/test/syz_mount_image_vfat_54: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_55:1
error: sys/linux/test/syz_mount_image_vfat_55: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_56:1
error: sys/linux/test/syz_mount_image_vfat_56: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_57:1
error: sys/linux/test/syz_mount_image_vfat_57: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_58:1
error: sys/linux/test/syz_mount_image_vfat_58: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_59:1
error: sys/linux/test/syz_mount_image_vfat_59: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_6:1
error: sys/linux/test/syz_mount_image_vfat_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_7:1
error: sys/linux/test/syz_mount_image_vfat_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_8:1
error: sys/linux/test/syz_mount_image_vfat_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_vfat_9:1
error: sys/linux/test/syz_mount_image_vfat_9: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_0:1
error: sys/linux/test/syz_mount_image_xfs_0: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_1:1
error: sys/linux/test/syz_mount_image_xfs_1: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_10:1
error: sys/linux/test/syz_mount_image_xfs_10: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_11:1
error: sys/linux/test/syz_mount_image_xfs_11: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_12:1
error: sys/linux/test/syz_mount_image_xfs_12: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_13:1
error: sys/linux/test/syz_mount_image_xfs_13: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_14:1
error: sys/linux/test/syz_mount_image_xfs_14: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_15:1
error: sys/linux/test/syz_mount_image_xfs_15: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_16:1
error: sys/linux/test/syz_mount_image_xfs_16: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_17:1
error: sys/linux/test/syz_mount_image_xfs_17: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_18:1
error: sys/linux/test/syz_mount_image_xfs_18: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_19:1
error: sys/linux/test/syz_mount_image_xfs_19: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_2:1
error: sys/linux/test/syz_mount_image_xfs_2: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_20:1
error: sys/linux/test/syz_mount_image_xfs_20: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_21:1
error: sys/linux/test/syz_mount_image_xfs_21: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_22:1
error: sys/linux/test/syz_mount_image_xfs_22: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_23:1
error: sys/linux/test/syz_mount_image_xfs_23: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_24:1
error: sys/linux/test/syz_mount_image_xfs_24: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_25:1
error: sys/linux/test/syz_mount_image_xfs_25: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_26:1
error: sys/linux/test/syz_mount_image_xfs_26: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_27:1
error: sys/linux/test/syz_mount_image_xfs_27: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_28:1
error: sys/linux/test/syz_mount_image_xfs_28: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_29:1
error: sys/linux/test/syz_mount_image_xfs_29: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_3:1
error: sys/linux/test/syz_mount_image_xfs_3: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_30:1
error: sys/linux/test/syz_mount_image_xfs_30: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_31:1
error: sys/linux/test/syz_mount_image_xfs_31: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_32:1
error: sys/linux/test/syz_mount_image_xfs_32: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_33:1
error: sys/linux/test/syz_mount_image_xfs_33: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_34:1
error: sys/linux/test/syz_mount_image_xfs_34: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_35:1
error: sys/linux/test/syz_mount_image_xfs_35: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_4:1
error: sys/linux/test/syz_mount_image_xfs_4: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_5:1
error: sys/linux/test/syz_mount_image_xfs_5: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_6:1
error: sys/linux/test/syz_mount_image_xfs_6: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_7:1
error: sys/linux/test/syz_mount_image_xfs_7: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_8:1
error: sys/linux/test/syz_mount_image_xfs_8: patch does not apply
error: patch failed: sys/linux/test/syz_mount_image_xfs_9:1
error: sys/linux/test/syz_mount_image_xfs_9: patch does not apply
error: patch failed: sys/linux/test/tipc:1
error: sys/linux/test/tipc: patch does not apply
error: patch failed: sys/linux/test/udp:1
error: sys/linux/test/udp: patch does not apply
error: patch failed: sys/linux/test/udp2:1
error: sys/linux/test/udp2: patch does not apply
error: patch failed: sys/linux/test/vhci:1
error: sys/linux/test/vhci: patch does not apply
error: patch failed: sys/linux/test/vnet_tun:1
error: sys/linux/test/vnet_tun: patch does not apply
error: patch failed: sys/linux/test/vusb:1
error: sys/linux/test/vusb: patch does not apply
error: patch failed: sys/linux/test/vusb_ath9k:1
error: sys/linux/test/vusb_ath9k: patch does not apply
error: patch failed: sys/linux/test/vusb_cdc_ecm:1
error: sys/linux/test/vusb_cdc_ecm: patch does not apply
error: patch failed: sys/linux/test/vusb_cdc_ncm:1
error: sys/linux/test/vusb_cdc_ncm: patch does not apply
error: patch failed: sys/linux/test/vusb_hid:1
error: sys/linux/test/vusb_hid: patch does not apply
error: patch failed: sys/linux/test/vusb_hid_hiddev:1
error: sys/linux/test/vusb_hid_hiddev: patch does not apply
error: patch failed: sys/linux/test/vusb_printer:1
error: sys/linux/test/vusb_printer: patch does not apply
error: patch failed: sys/linux/test/wireguard:1
error: sys/linux/test/wireguard: patch does not apply
error: patch failed: syz-fuzzer/testing.go:269
error: syz-fuzzer/testing.go: patch does not apply
error: patch failed: vm/qemu/qemu.go:415
error: vm/qemu/qemu.go: patch does not apply
Traceback (most recent call last):
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 580, in <module>
    setup.process()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 573, in process
    component()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 433, in __build_syzkaller
    self._run_cmd(f'git apply {self.env.syzkaller_patch}')
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 144, in _run_cmd
    subprocess.run(cmd, shell=True, check=True)
  File "/usr/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'git apply /home/nick/PrIntFuzz/patch/syzkaller.patch' returned non-zero exit status 1.