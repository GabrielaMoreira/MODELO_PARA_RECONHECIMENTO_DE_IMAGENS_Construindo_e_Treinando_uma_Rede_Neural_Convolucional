import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def plot_example_images(plt):
    img_size = 64
    plt.figure(0, figsize=(12,20))
    ctr = 0
    
    for expression in os.listdir("train/"):
        for i in range(1,6):
            ctr += 1
            #quantidade total de imagens#
            plt.subplot(7,5,ctr)
            img = load_img("train/" + expression + "/" +os.listdir("train/" + expression)[i], target_size=(img_size, img_size), color_mode="grayscale")
            plt.imshow(img, cmap="gray")
        
        #Amostra das primeiras 5 categorias
        #print(ctr)
        if ctr >= 25:
            break
    
    plt.tight_layout()
    return plt
