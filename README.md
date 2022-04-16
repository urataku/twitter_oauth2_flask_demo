# twitter_oauth2_flask_demo
Twitter 0auth2.0ログインのデモアプリです。

## 環境構築方法
- [Twitter Developer Portal](https://developer.twitter.com/en/portal/)でV2 APIを利用できるAppを作成
- User authentication settingsにて下記を設定
  - OAuth 2.0を有効化
  - Type of App : Web App
  - Callback URI / Redirect URL : http://127.0.0.1:3000/callback

- .envを作成し、FlaskのSecret Key(ランダム文字列)、Twitter Developer Portalで作成したAppのClient ID、Client Secretを.envに追加

```
cp .env.default .env
vi .env
source .env
```

- Dockerを起動

```
docker-compose up
```

- [http://127.0.0.1:3000](http://127.0.0.1:3000)にアクセス