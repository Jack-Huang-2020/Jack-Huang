# It's Empty

# 使用虚拟环境（推荐）

## 创建虚拟环境

```
python3 -m venv jh-env
```

## 激活虚拟环境（选一个适合你的 shell）

### 对于 bash/zsh:

```
source jh-env/bin/activate
```

### 对于 fish:

```
source jh-env/bin/activate.fish
```

### 安装依赖

```
pip install opencv-python numpy
```

### 运行你的程序（要在激活的环境下运行）

```
python your_script.py
```

### 退出虚拟环境

```
deactivate
```
