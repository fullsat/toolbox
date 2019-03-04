## How to install

```
pip install locustio pyzmq
```

## How to use

```
locust -c 1 -r 10 -H http://localhost:4000/ --no-web
```

* -c : 並列度 : master/slave含めて全体でのクライアントの数
* -r : クライアント生成時間 : 指定したクライアント数まで秒間でこの値ずつクライアントを増やす
* -H : 対象のプロトコル、ドメイン、ポート
* -no-web: Web UIから実行しない
