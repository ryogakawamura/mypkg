ロボットシステム学 課題2

---

## 概要 
  
  2つのノードにより、カウントアップしていく数字の中に3が含まれていると3を出力する。  
  3が含まれていなければ0を出力する。
    
---

## 動作環境
  
・Ubuntu 20.04  
・Raspberry Pi 4 Model B  
・ROS Noetic  

---

## デモ動画へのリンク
  
  https://youtu.be/XAlglP0-pvI
  
---

## 実行方法
  
  実行する手順は以下の通りです。  
  
  端末1  
  `$ cd ~/catkin_ws/src  `  
  `$ git clone https://github.com/ryogakawamura/mypkg.git  `  
  `$ cd ~/catkin_ws  `  
  `$ catkin_make  `  
  `$ roscore &  `  
  `$ cd ~/catkin_ws/src/mypkg/scripts  `  
  `$ chmod +x count.py  `  
  `$ chmod +x nabeatsu.py  `  
  `$ rosrun mypkg count.py  `  
  
  端末2  
  `$ rosrun mypkg nabeatsu.py  `  
  
  端末3  
  `$ rostopic echo /count_up  `  
  
  端末4  
  `$ rostopic echo /nabeatsu  `  
  
---

## ライセンス
  
  [BSD 3-Clause "New" or "Revised" License](https://github.com/ryogakawamura/mypkg/blob/main/LICENSE)

---
