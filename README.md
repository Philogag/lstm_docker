# lstm_docker

基于flask框架情感分析模块的http api封装

[![Docker](https://img.shields.io/badge/Docker-18.09.6-success.svg?style=flat-round)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.7-success.svg?style=flat-round)](https://www.python.org/downloads/release/python-372/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-success.svg?style=flat-round)](https://palletsprojects.com/p/flask/)
[![jieba](https://img.shields.io/badge/jieba-0.42.1-success.svg?style=flat-round)](https://github.com/fxsjy/jieba)
[![Keras](https://img.shields.io/badge/Keras-2.3.1-success.svg?style=flat-round)]()
[![numpy](https://img.shields.io/badge/Numpy-1.18.3-success.svg?style=flat-round)]()
[![PyYAML](https://img.shields.io/badge/PyYAML-5.3.1-success.svg?style=flat-round)]()
[![tensorflow](https://img.shields.io/badge/tensorflow-1.13.1-success.svg?style=flat-round)]()

# docker运行

```bash
$sudo docker run --name=lstm_docker -d --tty --restart=always -p 5000:5000 registry.cn-hangzhou.aliyuncs.com/philogag/lstm_docker
```

# 接口

## localhost:5000/
在线验证

## localhost:5000/api/predict/
对一个中文字符串情感分析

result常量：

+ 0：双性

+ 1：正面
+ 2：负面

POST

```json
{
  "text": "str"
}
```
Return 
```
{
	"result": 2,
	"text": ""
}
```

## localhost:5000/api/wordcount

对一组字符串进行分词并统计总体词频

POST

```
{
    "top": 10, // -1 means all
    "texts": [
        "string 1",
        "string 2",
        ...
        "string n"
    ]
}
```

Return

```
{
    'cnt': {
        "word 1": a integer,
        "word 2": a integer,
        ...
        "word n": a integer,
    }
}
```

