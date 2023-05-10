# Histogram Equlization

## Convolution 2D

Apply five 2D filters with different kernels on your custom image.

  1. Edge detection filter
  kernel = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])
                   
![attack edge](https://user-images.githubusercontent.com/43343453/236635058-5fc34da3-7689-4ea7-8eff-90fc543f66ea.jpg)

  2. Sharpening filter
  kernel = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

![attack Sharpening](https://user-images.githubusercontent.com/43343453/236635103-ca897904-4b1d-4566-8540-f7c124e0a403.jpg)

  3. Emboss filter
  kernel = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

![attack Emboss](https://user-images.githubusercontent.com/43343453/236635137-1a03a696-c141-40c7-ba29-782d0599527c.jpg)

  4. Identity filter
kernel = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])
 
 ![attack Identity](https://user-images.githubusercontent.com/43343453/236635210-c65354d0-987f-40d7-ab38-3447dfb24243.jpg)
                   
 5. Sobel filter
kernel = np.array([[-1  ,  0 ,  1],
                   [-2  ,  0 ,  2],
                   [-1  ,  0 ,  1]])

![attack Sobel](https://user-images.githubusercontent.com/43343453/236635237-8f3ae5e2-927b-40f5-ac3f-f0180facec7d.jpg)


## The Magic 🪄🔮

Use the average filter to reveal hidden things.

![magic](https://user-images.githubusercontent.com/43343453/236635326-d375abf9-d902-4bc9-bfdc-b456674de264.png)

## Median Filter

Used median filter to reduce noise in images.

input:

![chest](https://user-images.githubusercontent.com/43343453/236635387-bba994a0-67ab-4be4-8c48-6bb677dbf2d1.jpg)

output:

![chest](https://user-images.githubusercontent.com/43343453/236635403-094e99d8-7a56-4ca9-bc56-0b16be00920f.jpg)


input:

![pcb](https://user-images.githubusercontent.com/43343453/236635493-1dae62fb-2d5c-40a9-bc8f-048af44d04f1.jpg)

output:

![pcb](https://user-images.githubusercontent.com/43343453/236635476-b8cd8f37-a869-42f2-84e6-9f76085c182b.jpg)

input:

![point](https://user-images.githubusercontent.com/43343453/236635522-2b014f12-7348-496c-b4a8-0d6456ab5cf1.jpg)

output:

![point](https://user-images.githubusercontent.com/43343453/236635538-980c5753-c4ad-4358-ad8b-dd8f03f54d06.jpg)

input:

![balloons_noisy](https://user-images.githubusercontent.com/43343453/236635566-9dd2b938-56b6-432e-9343-9d60fc001502.png)

output:

![balloons](https://user-images.githubusercontent.com/43343453/236635554-507095c5-0d28-4d67-a436-b25e7af7ce1b.jpg)

input:

![Medianfilterp](https://user-images.githubusercontent.com/43343453/236635578-7be091a9-a45d-419f-b046-d297847e182a.png)

output:

![Medianfilterp](https://user-images.githubusercontent.com/43343453/236635585-59cf7331-47bd-4681-b733-26e41fd83c51.jpg)


input:

![5](https://user-images.githubusercontent.com/43343453/236635616-180a5dae-4e75-4544-9d1b-eaafd409fd95.png)

output:

![5](https://user-images.githubusercontent.com/43343453/236635603-7ece2f92-5a71-4c4c-8fa4-b98833496177.jpg)


## Histogram Equalization

used cv2.equalizeHist() function to Histogram Equalization.

input:

![spaces](https://user-images.githubusercontent.com/43343453/236635754-9ed19913-0339-41c2-899e-c5fcd521f9d9.jpg)

output:

![spaces](https://user-images.githubusercontent.com/43343453/236635778-8b1e1833-4291-4ce3-9b79-9f4fbadde21b.jpg)

input:

![Hawkes_Bay_NZ](https://user-images.githubusercontent.com/43343453/236635771-60a51be8-f126-44ec-a660-67ac7fc28a23.jpg)

output:

![Hawkes_Bay_NZ](https://user-images.githubusercontent.com/43343453/236635853-40939c28-587c-4f87-a352-8745c096d175.jpg)


In next images is orginal,  used cv2.equalizeHist()  and cv2.createCLAHE functions to Histogram Equalization, Respectively.

![statue](https://user-images.githubusercontent.com/43343453/236635952-e952e249-d7ce-4199-b7d9-b914d0ea5e7c.jpg)
