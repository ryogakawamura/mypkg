ロボットシステム学 課題2

---

## 概要 
  
  第10回で作成したROSのパッケージをベースに、オリジナリティーある改造をして、GitHubに置く。  
  ROSで動かしている様子をビデオに撮影してYouTubeに公開する  
    
---

## 動作環境
  
・Ubuntu 20.04  
・Raspberry Pi 4 Model B  
  
---

## 使用したもの
  
  ・Raspberry Pi 4 Model B：1台  
    
---

## デモ動画へのリンク
  
  https://youtu.be/
  
---

## インストール方法
  
  実行する手順は以下の通りです。  
  
  `$ git clone https://github.com/ryogakawamura/myled.git  `  
  `$ cd myled  `  
  `$ make  `  
  `$ sudo insmod myled.ko `  
  `$ sudo chmod 666 /dev/myled0  `  
  `$ sudo [0 or 1] > /dev/myled0  `  
  
---

## 使用方法

  `$ echo 0 > /dev/myled0  `：LED消灯  
  `$ echo 1 > /dev/myled1  `：LED点灯  
  
---

## ライセンス
  
  [BSD 3-Clause "New" or "Revised" License](https://github.com/ryogakawamura/mypkg/blob/main/LICENSE)

---
