# %%
import os
import numpy as np
import cv2
from PIL import Image
# %%
img = cv2.imread('close-up-portraits.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# %%
def pyramid_sharp(img, level: int, strength: list):
    """Laplacian Pyramid Sharp"""
    assert len(strength) == level
    img_use = np.array(img.astype(np.float32))
    img_dw, img_res = [img_use], []
    for idx in range(level):
        img_temp = cv2.resize(cv2.GaussianBlur(img_use, (3, 3), 0),
                              (img_use.shape[1] // 2, img_use.shape[0] // 2),
                              cv2.INTER_LINEAR)
        # img_temp = cv2.resize(img_use,
        #                       (img_use.shape[1] // 2, img_use.shape[0] // 2),
        #                       cv2.INTER_LINEAR)
        img_dw.append(img_temp)
        img_res.append(img_use - cv2.resize(img_temp, (
            img_use.shape[1], img_use.shape[0]), cv2.INTER_LINEAR))
        img_use = np.array(img_temp)

    img_up = np.array(img_dw[-1])
    for idx in range(level - 1, -1, -1):
        img_h, img_w = img_dw[idx].shape[:2]
        img_up = cv2.resize(img_up, (img_w, img_h),
                            cv2.INTER_LINEAR) + strength[idx] * img_res[idx]
    img_up = np.clip(img_up, 0, 255).astype(np.uint8)
    return img_up
# %%
def usm_sharp(img, radius: int, strength: float, thres: float):
    radius = radius // 2 * 2 + 1
    img_in = np.array(img / 255.)
    blur = cv2.GaussianBlur(img_in, (radius, radius), 0)
    res = img_in - blur
    mask = (np.abs(res) > (thres / 255.)) * 1.0
    img_out = blur + res * mask * strength
    img_out = np.clip(img_out * 255, 0, 255).astype(np.uint8)
    return img_out
# %%
