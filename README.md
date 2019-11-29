# RECIPE_BOT

## api.py
```
楽天レシピAPI
食材ワードをrecipe_searchに渡すと
関連するレシピURLを返します。

```
## scraping.py
```
api.pyで返されたレシピURL内のランキングTOP3
以下３項目をスクレイピングします。
- image画像 == src
- レシピtitle == title
- リンクURL == url
```
## main.py
```
LINE_botとしての最終的な処理を行います。
LINE APIを活用、処理はHEROKU

1 LINE_botに対して食材ワードを入力
2 api.py内で対応するレシピURLを返す
3 2のURL内をスクレイピング
4 3の素材をLINEトーク内でカルーセル表示させる

```

# line-bot-basic-sample

## Clone
```
git clone https://github.com/mohira/line-bot-basic-sample
cd line-bot-basic-sample
```

```
pipenv install
```

## Install Heroku CLI for Mac
- https://devcenter.heroku.com/articles/heroku-cli

```
brew tap heroku/brew && brew install heroku
```

## Create Heroku App
```
heroku login
```

```
heroku create <YOUR_HEROKU_APP_NAME>
```

```
heroku git:remote --app <YOUR_HEROKU_APP_NAME>

git push heroku master
```

## Webhook Setting
![webhook_setting](https://img.esa.io/uploads/production/attachments/6586/2019/11/17/21054/9263a865-266a-4aa9-8a19-e1be0f3dd0c3.png)


## Set Environment Variables
```
heroku config:set ACCESS_TOKEN=<YOUR_ACCESS_TOKEN>
```

```
heroku config:set CHANNEL_SECRET=<YOUR_CHANNEL_SECRET>
```

```
heroku config:set USER_ID=<YOUR_USER_ID>
```

## Debug Hint
```
# tail heroku log
heroku logs --tail -a <YOUR_HEROKU_APP_NAME>
```

```
# check all environment variables
$ heroku config
```

```
# delete a specific environment variable
$ heroku config:unset <ENV_VAR_NAME>
```
