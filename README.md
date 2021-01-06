ロボットシステム学 課題2

---

## 概要 
  
  課題: 講義で作ったデバイスドライバを改造して、LEDやモータ、あるいはその他なにかデバイスを動かせるようにして、動かしている様子を動画に撮影する。
  (講義中に作成したドライバhttps://github.com/ryuichiueda/robosys_device_drivers/blob/master/myled.c)
  
---

## 動作環境
  
・Ubuntu 20.04  
・Raspberry Pi 4 Model B  
(GPIOピンは25番とGNDを使用)  
  
---

## 使用したもの
  
  ・Raspberry Pi 4 Model B：1台  
  ・ブレッドボード：1個  
  ・青色LED：1個  
  ・ジャンパー線(M-M)：1本  
  ・ジャンパー線(M-F)：2本  
  ・抵抗220Ω：2個  
  
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
  
  [BSD 2-Clause "Simplified" License](https://github.com/ryogakawamura/mypkg/blob/main/LICENSE)

---
