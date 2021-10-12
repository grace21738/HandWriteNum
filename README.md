# HandWriteNum
## 使用MNIST dataset 
  + 訓練集
  + 測試集
## 實作
1. 因為色彩為RGB(0~255)，所以正規化時直接除以255
2. 模型設置使用Keras Sequential串起來:
  + Flatten: input為28*28 pixel有784個特徵值
  + Relu: 找出刺激強度較大的細胞，引起神經衝動
  + Dropout:訓練週期中隨機丟棄20%神經元
  + Softmax: 找出輸入圖片0~9的機率，向量的所有元素之和為 1
3. 訓練時進行5次迭代

## 結果
### 訓練時部分辨識錯誤:
![num](https://user-images.githubusercontent.com/61674033/136986001-0d814ba4-5360-4408-93cc-0ffa00d62b65.jpg)

### 隨著迭代次數增加準確率提升:
![train_accuracy](https://user-images.githubusercontent.com/61674033/136986007-cf3d14a9-8a07-4b41-a9f0-832675b42cb5.jpg)
![train_loss](https://user-images.githubusercontent.com/61674033/136986010-ac891033-6b0b-4765-8e87-092d795099d6.jpg)
