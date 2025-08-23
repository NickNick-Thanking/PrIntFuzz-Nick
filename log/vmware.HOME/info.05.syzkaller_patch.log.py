补丁 syzkaller_patch 的前面几行内容如下：
##########################################
diff --git a/.gitignore b/.gitignore
index 4c9e47088dfd..e6a355e9f8a2 100644
--- a/.gitignore
+++ b/.gitignore
@@ -18,9 +18,12 @@ dashboard/app/config_prod.go
 sys/*/gen/*.go
 executor/defs.h
 executor/syscalls.h
+sys/*/*.txt.const
 
 # produced by gcloud command
 dashboard/app/.gcloudignore
 
 # jetbrains goland
 .idea
+
+sys/linux/new_*.txt
diff --git a/executor/common_linux.h b/executor/common_linux.h
index 88c129f8581f..e588aa6be052 100644
--- a/executor/common_linux.h
+++ b/executor/common_linux.h
@@ -1384,6 +1384,8 @@ static void initialize_netdevices(void)
 		int macsize;
 		bool noipv6;
 	} devices[] = {
+        {"enp0s4", ETH_ALEN},
+        {"enp0s5", ETH_ALEN},
 	    {"lo", ETH_ALEN},
 	    {"sit0", 0},
 	    {"bridge0", ETH_ALEN},
@@ -3654,14 +3656,14 @@ static void sandbox_common()
 	prctl(PR_SET_PDEATHSIG, SIGKILL, 0, 0, 0);
 	setsid();
 
-#if SYZ_EXECUTOR || __NR_syz_init_net_socket || SYZ_DEVLINK_PCI
-	int netns = open("/proc/self/ns/net", O_RDONLY);
-	if (netns == -1)
-		fail("open(/proc/self/ns/net) failed");
-	if (dup2(netns, kInitNetNsFd) < 0)
-		fail("dup2(netns, kInitNetNsFd) failed");
-	close(netns);
-#endif
+// #if SYZ_EXECUTOR || __NR_syz_init_net_socket || SYZ_DEVLINK_PCI
+// 	int netns = open("/proc/self/ns/net", O_RDONLY);
+// 	if (netns == -1)
+// 		fail("open(/proc/self/ns/net) failed");
+// 	if (dup2(netns, kInitNetNsFd) < 0)
+// 		fail("dup2(netns, kInitNetNsFd) failed");
+// 	close(netns);
+// #endif
 
 	struct rlimit rlim;
 #if SYZ_EXECUTOR
@@ -5284,3 +5286,60 @@ static long syz_clone3(volatile long a0, volatile long a1)
 }
 
 #endif
+
+#if SYZ_EXECUTOR || __NR_syz_interrupt
+
+#define INTERRUPT _IO(0x68, 0)
+
+static long syz_interrupt(volatile long a0)
+{
+	char* data = (char*)a0;
+	int fd, ret;
+
+	fd = open("/dev/print_fuzz", O_RDONLY);
+	if (fd < 0)
+		fail("Open print_fuzz failed.");
+	ret = ioctl(fd, INTERRUPT, data);
+	if (ret < 0) {
+		debug("Ioctl interrupt for print_fuzz failed.");
+		return -1;
+	}
+
+	return 0;
+}
+
+#endif
+
+#if SYZ_EXECUTOR || __NR_syz_prepare_data
+
+#define PREPARE_DATA _IO(0x68, 1)
+
+#define BUF_LEN 0x400
+#define DMA_BUF_LEN 0x10000
+
+typedef struct fuzz_input {
+	char register_data[BUF_LEN];
+	char dma_data[DMA_BUF_LEN];
+} fuzz_input;
+
+static long syz_prepare_data(volatile long a0)
+{
+	fuzz_input* data = (fuzz_input*)a0;
+	int fd, ret, index;
+
+	for (index = BUF_LEN; index < DMA_BUF_LEN; index += BUF_LEN)
+		memcpy(data->dma_data+index, data->dma_data, BUF_LEN);
+
+	fd = open("/dev/print_fuzz", O_RDONLY);
+	if (fd < 0)
+		fail("Open print_fuzz failed.");
+	ret = ioctl(fd, PREPARE_DATA, data);
+	if (ret < 0) {
+		debug("Ioctl prepare_data for print_fuzz failed.");
+		return -1;
+	}
+
+	return 0;
+}
+
+#endif
diff --git a/executor/executor.cc b/executor/executor.cc
index 28ab72206b26..d4fde29a31c8 100644
--- a/executor/executor.cc
+++ b/executor/executor.cc
@@ -860,6 +860,8 @@ void execute_one()
 			prog_extra_cover_timeout = std::max(prog_extra_cover_timeout, 500 * slowdown_scale);
 		if (strncmp(syscalls[call_num].name, "syz_80211_inject_frame", strlen("syz_80211_inject_frame")) == 0)
 			prog_extra_cover_timeout = std::max(prog_extra_cover_timeout, 300 * slowdown_scale);
+		if (strncmp(syscalls[call_num].name, "interrupt", strlen("interrupt")) == 0)
+			prog_extra_cover_timeout = std::max(prog_extra_cover_timeout, 500 * slowdown_scale);
 		uint64 copyout_index = read_input(&input_pos);
 		uint64 num_args = read_input(&input_pos);
 		if (num_args > kMaxArgs)
diff --git a/pkg/csource/generated.go b/pkg/csource/generated.go
index 04f6b6108b91..886ba29bc52d 100644
--- a/pkg/csource/generated.go
+++ b/pkg/csource/generated.go
@@ -10240,6 +10240,60 @@ static long syz_clone3(volatile long a0, volatile long a1)
 
 #endif
 
+#if SYZ_EXECUTOR || __NR_syz_interrupt
+
+#define INTERRUPT _IO(0x68, 0)
+
+static long syz_interrupt(volatile long a0)
+{
+	char* data = (char*)a0;
+	int fd, ret;
+
+	fd = open("/dev/print_fuzz", O_RDONLY);
+	if (fd < 0)
+		fail("Open print_fuzz failed.");
+	ret = ioctl(fd, INTERRUPT, data);
+	if (ret < 0) {
+		debug("Ioctl interrupt for print_fuzz failed.");
+		return -1;
+	}
+
+	return 0;
+}
+
+#endif
+
+#if SYZ_EXECUTOR || __NR_syz_prepare_data
+
+#define PREPARE_DATA _IO(0x68, 1)
+
+#define BUF_LEN 0x400
+#define DMA_BUF_LEN 0x10000
+
+typedef struct fuzz_input {
+	char register_data[BUF_LEN];
+	char dma_data[DMA_BUF_LEN];
+} fuzz_input;
+
+static long syz_prepare_data(volatile long a0)
+{
+	fuzz_input* data = (fuzz_input*)a0;
+	int fd, ret;
+
+	fd = open("/dev/print_fuzz", O_RDONLY);
+	if (fd < 0)
+		fail("Open print_fuzz failed.");
+	ret = ioctl(fd, PREPARE_DATA, data);
+	if (ret < 0) {
+		debug("Ioctl prepare_data for print_fuzz failed.");
+		return -1;
+	}
+
+	return 0;
+}
+
+#endif
+
 #elif GOOS_test
 
 #include <stdlib.h>
diff --git a/pkg/host/syscalls_linux.go b/pkg/host/syscalls_linux.go