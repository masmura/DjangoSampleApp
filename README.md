# 概要
インプレス社「Python 機械学習プログラミング」第9章の映画レビュー分類器のモデルをDjangoのフレームワーク上で利用するアプリケーション。  
ユーザがレビューを入力し、推定結果を表示する。その結果に対して成否のフィードバックをユーザが送信しモデルを更新するだけの単純なもの。  

# 環境構築
pip install -r requirements.txt ※pipが使える前提

# アプリ実行手順
DjangoSampleApp\samplesite$ python manage.py makemigrations  
DjangoSampleApp\samplesite$ python manage.py migrate  
DjangoSampleApp\samplesite$ python manage.py runserver --noreload  

-Webブラウザよりhttp://127.0.0.1:8000 にアクセス
-Text欄に映画のレビューコメントを英語で入力してSubmit reviewボタンを押下
-サーバ上の推論モデルが感情を推定（negative:0 or positive:1）
-推定結果が正しければCorrectを、正しくなければIncorrectを押下すると、内容がDBに格納されると同時にモデルが更新される。
-ベースモデルは事前に作成済みのモデルであり、次回以降のサーバ起動時にはDB上のデータをもとにモデルを更新してからサービスを開始する。    

以上
