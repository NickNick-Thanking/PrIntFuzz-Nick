# PrIntFuzz-Nick
## 02 --build_linux_all

### E: "enable_config.json doesn't exist."
运行 `python3 ./scripts/python/setup.py` 或 `python3 ./scripts/python/setup.py --build_linux_all` 会提示下面错误：

`python3 ./scripts/python/setup.py`
``` python
#
# configuration written to .config
#
make[1]: Leaving directory '/home/nick/data-me/github-me/PrIntFuzz-Nick/build/linux/linux_allmodconfig'
Traceback (most recent call last):
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/./scripts/python/setup.py", line 580, in <module>
    setup.process()
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/./scripts/python/setup.py", line 573, in process
    component()
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/./scripts/python/setup.py", line 126, in _build_linux_all
    self.__enable_config('allmod')
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/./scripts/python/setup.py", line 297, in __enable_config
    enable_config = utils.EnableConfig(args)
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/scripts/python/utils/enable_config.py", line 10, in __init__
    self.__check()
  File "/home/nick/data-me/github-me/PrIntFuzz-Nick/scripts/python/utils/enable_config.py", line 19, in __check
    raise Exception(f"The json file {self.env.config_json} doesn't "
Exception: The json file /home/nick/data-me/github-me/PrIntFuzz-Nick/third_party/linux/config/linux/enable_config.json doesn't exist.
```

添加

`python3 ./scripts/python/setup.py`
```
```

# PrIntFuzz

