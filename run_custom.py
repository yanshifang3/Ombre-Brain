#!/usr/bin/env python3
"""
run_custom.py — 自定义启动入口，热更新不覆盖此文件（不在 src/ 里）。

启动步骤：
1. src/ 加入 sys.path
2. 调用 _custom.apply_patches()，把定制版 surface_search 装进 tools.breath
3. 以 __main__ 身份运行 src/server.py

热更新（src/ 被上游覆盖）后：
- _custom.py 保留（上游没有这个文件）
- run_custom.py 保留（不在 src/ 里）
- 不需要任何手动操作
"""
import os
import sys
import runpy

_ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(_ROOT)
sys.path.insert(0, os.path.join(_ROOT, "src"))

# 打补丁（在所有模块被 server.py import 之前注入）
from tools.breath._custom import apply_patches
apply_patches()

# 以 __main__ 运行 server.py
runpy.run_path(os.path.join(_ROOT, "src", "server.py"), run_name="__main__")
