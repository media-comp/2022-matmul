# 2022-matmul

Reimplementation of the matrix multiplication proposed in the following paper: XYZ et al., "Simple Matrix Multiplication", IEEE XXX, 2022.

## Prerequisites
- You need to install Python 3.8+
- Install the required packages by:
```console
pip install -r requirements.txt
```

## How to run
```console
python bench.py
```


You will obtain the result:
```console
0.007152557373046875 msec
Error: 0
```
Or
```console
python bench_affine.py
```
You will obtain the result:

```console
0.012159347534179688 msec
Error: 0
```
