# Convolution and Histogram

## Histogram 📊

Calculate histogram then visualize the result with plt.plot(), plt.hist() and plt.bar().

input:

![Mona_Lisa_2](https://user-images.githubusercontent.com/43343453/236417881-87995365-dc4a-4583-b4e4-9fb066871998.jpg)

outputs:

![bar](https://user-images.githubusercontent.com/43343453/236417951-31e0e70f-4bd7-48e8-bb1f-c13cc189a474.png)
![hist](https://user-images.githubusercontent.com/43343453/236418021-7f3b966f-6799-432c-91f0-2a7ed656b6ea.png)
![plot](https://user-images.githubusercontent.com/43343453/236418029-8dde9166-857e-46a3-9464-809820005c0c.png)


## Foreground focus, Blur background 🌷

input:

![flower](https://user-images.githubusercontent.com/43343453/236418096-1abe5fd1-5fbe-45c2-af66-bd298170087c.jpg)

output:

![flower_blur](https://user-images.githubusercontent.com/43343453/236418140-9bd3f23c-db9e-4fa2-8ca0-312241c3f46d.png)

## Edge detection 

Use Laplacian Operator to detect edges of image.
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

inputs:

![spider](https://user-images.githubusercontent.com/43343453/236418461-a41d5bd5-5f9d-411f-b5b3-141c25b49e99.jpg)
![lion](https://user-images.githubusercontent.com/43343453/236418477-93603e96-150f-49af-be81-d51e7f120585.jpg)

outputs:

![spider edge](https://user-images.githubusercontent.com/43343453/236418394-0e9825eb-fc92-485a-bb80-bf6f94b5ab58.png)
![lion](https://user-images.githubusercontent.com/43343453/236418420-e2457d4b-c7c9-4764-9ab3-c80dfad3d76b.png)

## Vertical and horizontal edge detection

Use A suitable kernel to detect vertical and horizontal edges of image.

input:

![house](https://user-images.githubusercontent.com/43343453/236418615-b12c9f99-530a-484b-b27a-8934f4cf2b09.jpg)

outputs:

![vertical house](https://user-images.githubusercontent.com/43343453/236418746-bc0b1096-91dd-4393-bc96-b8badc5809cc.png)
![horizontal house](https://user-images.githubusercontent.com/43343453/236418777-224c3702-30bd-454e-b86a-3e2b9e25f7c8.png)


## Noise reduction

Applied 3x3, 5x5 and 15x15 average filter to reduce noise in images. 

inputs:

![chest](https://user-images.githubusercontent.com/43343453/236419069-14009bce-302b-47d7-82cc-809ca14f3141.jpg)
![pcb](https://user-images.githubusercontent.com/43343453/236419104-4dbc5263-22da-46d7-9ec1-560e5622c009.jpg)
![point](https://user-images.githubusercontent.com/43343453/236419113-3c890a1e-c830-4cdd-8ebd-d04dcee2f062.jpg)


outputs:

![chest_3](https://user-images.githubusercontent.com/43343453/236419157-853e09df-b489-4d7e-a8d1-450fa836e331.png)
![chest_5](https://user-images.githubusercontent.com/43343453/236419172-a8145812-f68f-407c-bfe1-c05fc48b423c.png)
![chest_15](https://user-images.githubusercontent.com/43343453/236419186-b64a357d-9cf9-4510-9c0a-492e9b5bc5a7.png)

![pcb_3](https://user-images.githubusercontent.com/43343453/236419223-3d36c7d0-03af-469d-8bdf-f0ae038eca11.png)
![pcb_5](https://user-images.githubusercontent.com/43343453/236419268-189022f9-1bb9-4052-aae9-b8923ffe658a.png)
![pcb_15](https://user-images.githubusercontent.com/43343453/236419287-25a8f979-1ada-4f8e-ab08-f28a23be3180.png)

![point_3](https://user-images.githubusercontent.com/43343453/236419307-bc1cbfe6-6250-4ec2-aa9c-f5188ab8b99c.png)
![point_5](https://user-images.githubusercontent.com/43343453/236419324-266a144b-875d-4747-ab3f-e97a595ebc84.png)
![point_15](https://user-images.githubusercontent.com/43343453/236419342-2d785d87-2720-4cb8-a86e-e716c59708f7.png)


