import os,shutil
import cv2
from WordSegmentation import wordSegmentation, prepareImg
from Model import Model, DecoderType
from main import FilePaths,infer

decoderType = DecoderType.BestPath
model = Model(open(FilePaths.fnCharList).read(), decoderType, mustRestore=True)
def wordseg():
	"""reads images from data/ and outputs the word-segmentation to out/"""

	# read input images from 'in' directory
	a=''
	imgFiles = os.listdir('../lines/')
	if not os.path.exists('../out/'):
		os.mkdir('../out/')
	else:
		if os.listdir('../out/'):
			folder = '../out/'
			for the_file in os.listdir(folder):
				file_path = os.path.join(folder, the_file)
				try:
					if os.path.isfile(file_path):
						os.unlink(file_path)
					elif os.path.isdir(file_path):
						shutil.rmtree(file_path)
				except Exception as e:
					print(e)
	for (i,f) in enumerate(sorted(imgFiles)):
		#print('Segmenting words of sample %s'%f)
		
		# read image, prepare it by resizing it to fixed height and converting it to grayscale
		img = prepareImg(cv2.imread('../lines/%s'%f), 50)
		
		# execute segmentation with given parameters
		# -kernelSize: size of filter kernel (odd integer)
		# -sigma: standard deviation of Gaussian function used for filter kernel
		# -theta: approximated width/height ratio of words, filter function is distorted by this factor
		# - minArea: ignore word candidates smaller than specified area
		res = wordSegmentation(img, kernelSize=25, sigma=11, theta=7, minArea=100)
		
		# write output to 'out/inputFileName' directory
		if not os.path.exists('../out/%s'%f):
			os.mkdir('../out/%s'%f)
		
		# iterate over all segmented words
		#print('Segmented into %d words'%len(res))
		for (j, w) in enumerate(res):
			(wordBox, wordImg) = w
			(x, y, w, h) = wordBox
			cv2.imwrite('../out/%s/%d.png'%(f, j), wordImg) # save word
			a=a+' '+infer(model,'../out/%s/%d.png'%(f, j))
			cv2.rectangle(img,(x,y),(x+w,y+h),0,1) # draw bounding box in summary image

	return a
		
		# output summary image with bounding boxes around words
		#cv2.imwrite('../out/%s/summary.png'%f, img)


if __name__ == '__main__':
	main()
