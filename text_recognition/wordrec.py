import argparse
import cv2
import editdistance
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
from main import FilePaths


def infer(model, fnImg):
    img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)
    #print('Recognized:', '"' + recognized[0] + '"')
    return recognized[0]






decoderType = DecoderType.BestPath
print(open(FilePaths.fnAccuracy).read())
model = Model(open(FilePaths.fnCharList).read(), decoderType, mustRestore=True)
a=infer(model, FilePaths.fnInfer)
print(a)

