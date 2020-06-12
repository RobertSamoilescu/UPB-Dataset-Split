import cv2
import numpy as np

if __name__ == "__main__":

	train = cv2.imread("imgs/train.png")
	test = cv2.imread("imgs/test.png")

	cmb = train//2 + test//2
	cv2.imwrite("imgs/train_test_split.png", cmb)
