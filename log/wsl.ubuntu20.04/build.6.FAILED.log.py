make[1]: Leaving directory '/home/nick/github-nick/PrIntFuzz-Nick/build/linux/linux_fuzz'

[CMD]: sudo rm -rf ./share/lib/modules

[CMD]: mkdir -p ./share && sudo mount -o loop /home/nick/PrIntFuzz/out/build/stretch_without_module.img ./share && sudo cp -a /home/nick/PrIntFuzz/out/build/rootfs/lib/modules/ ./share/lib/ && sudo umount ./share
mount: ./share: failed to setup loop device for /home/nick/PrIntFuzz/out/build/stretch_without_module.img.
Traceback (most recent call last):
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 580, in <module>
    setup.process()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 573, in process
    component()
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 137, in _build_linux_fuzz
    self.__install_module('fuzz')
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 381, in __install_module
    self._run_cmd('mkdir -p ./share && '
  File "/home/nick/PrIntFuzz/scripts/python/setup.py", line 144, in _run_cmd
    subprocess.run(cmd, shell=True, check=True)
  File "/usr/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'mkdir -p ./share && sudo mount -o loop /home/nick/PrIntFuzz/out/build/stretch_without_module.img ./share && sudo cp -a /home/nick/PrIntFuzz/out/build/rootfs/lib/modules/ ./share/lib/ && sudo umount ./share' returned non-zero exit status 32.