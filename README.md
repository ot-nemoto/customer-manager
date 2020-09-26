# customer-manager

## 起動

```sh
docker-compose up -d
```

## マイグレーション


```sh
docker-compose exec app bash
```

```sh
pwd
  # /customer-manager
python manage.py migrate
```

### ref

https://utamaro.hatenablog.jp/entry/2018/10/21/102148
