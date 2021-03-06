from keras.layers import Input, Dense
from keras.models import Model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import normalize
import time
from sklearn import metrics
from myUtils import *
from DAEclass import DAE
import os

if __name__ == '__main__':
    datatypes=["equal","heterogeneous"]
    typenums=[5,10,15]
    noise_factor=0.5
    for datatype in datatypes:
        for typenum in typenums:
            datapath='data/simulations/{}/{}'.format(datatype, typenum)
            resultpath='result/simulations/{}/{}'.format(datatype, typenum)
            groundtruth = np.loadtxt('{}/c.txt'.format(datapath))
            groundtruth = list(np.int_(groundtruth))

            omics1 = np.loadtxt('{}/o1.txt'.format(datapath))
            omics1 = np.transpose(omics1)
            omics1 = normalize(omics1, axis=0, norm='max')

            omics2 = np.loadtxt('{}/o2.txt'.format(datapath))
            omics2 = np.transpose(omics2)
            omics2 = normalize(omics2, axis=0, norm='max')

            omics3 = np.loadtxt('{}/o3.txt'.format(datapath))
            omics3 = np.transpose(omics3)
            omics3 = normalize(omics3, axis=0, norm='max')

            omics = np.concatenate((omics1, omics2, omics3), axis=1)


            # ae = AE(data, dims)
            # ae.train()
            # encoded_factors = ae.predict(data)

            noise_factor = 0.1

            encoding1_dim1 = 100
            encoding2_dim1 = 50
            if typenum==15:
                middle_dim1 = 5
            elif typenum==10:
                middle_dim1 = 4
            elif typenum==5:
                middle_dim1 = 3
            dims1 = [encoding1_dim1, encoding2_dim1, middle_dim1]
            ae1 = DAE(omics1, dims1,noise_factor)
            ae1.train()
            ae1.autoencoder.summary()
            encoded_factor1 = ae1.predict(omics1)

            encoding1_dim2 = 80
            encoding2_dim2 = 50
            if typenum==15:
                middle_dim2 = 5
            elif typenum==10:
                middle_dim2 = 3
            elif typenum==5:
                middle_dim2 = 1
            dims2 = [encoding1_dim2, encoding2_dim2, middle_dim2]
            ae2 = DAE(omics2, dims2,noise_factor)
            ae2.train()
            ae2.autoencoder.summary()
            encoded_factor2 = ae2.predict(omics2)

            encoding1_dim3 = 80
            encoding2_dim3 = 50
            if typenum==15:
                middle_dim3 = 5
            elif typenum==10:
                middle_dim3 = 3
            elif typenum==5:
                middle_dim3 = 1
            dims3 = [encoding1_dim3, encoding2_dim3, middle_dim3]
            ae3 = DAE(omics3, dims3,noise_factor)
            ae3.autoencoder.summary()
            ae3.train()
            encoded_factor3 = ae3.predict(omics3)

            encoded_factors = np.concatenate((encoded_factor1, encoded_factor2, encoded_factor3), axis=1)

            if not os.path.exists("{}/DAE_FAETC_EM.txt".format(resultpath)):
                os.mknod("{}/DAE_FAETC_EM.txt".format(resultpath))
            np.savetxt("{}/DAE_FAETC_EM_{}.txt".format(resultpath,typenum), encoded_factors)

            # if not os.path.exists("AE_FCTAE_Kmeans.txt"):
            #     os.mknod("AE_FCTAE_Kmeans.txt")
            # fo = open("AE_FCTAE_Kmeans.txt", "a")
            # clf = KMeans(n_clusters=typenum)
            # t0 = time.time()
            # clf.fit(encoded_factors)  # ????????????
            # km_batch = time.time() - t0  # ??????kmeans???????????????????????????

            # print(datatype, typenum)
            # print("K-Means??????????????????????????????:%.4fs" % km_batch)

            # # ????????????
            # score_funcs = [
            #     metrics.adjusted_rand_score,  # ARI????????????????????????
            #     metrics.v_measure_score,  # ????????????????????????????????????
            #     metrics.adjusted_mutual_info_score,  # AMI?????????????????????
            #     metrics.mutual_info_score,  # ?????????
            # ]

            # centers = clf.cluster_centers_
            # print("zlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzly")
            # #print("centers:")
            # #print(centers)
            # print("zlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzly")
            # labels = clf.labels_
            # print("labels:")
            # print(labels)
            # labels = list(np.int_(labels))
            # if not os.path.exists("{}/DAE_FAETC_CL.txt".format(resultpath)):
            #     os.mknod("{}/DAE_FAETC_CL.txt".format(resultpath))
            # np.savetxt("{}/DAE_FAETC_CL.txt".format(resultpath), labels,fmt='%d')
            # print("zlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzly")
            # # 2. ?????????????????????????????????????????????
            # for score_func in score_funcs:
            #     t0 = time.time()
            #     km_scores = score_func(groundtruth, labels)
            #     print("K-Means??????:%s???????????????????????????:%.5f?????????????????????:%0.3fs" % (score_func.__name__, km_scores, time.time() - t0))
            # t0 = time.time()
            # jaccard_score = jaccard_coefficient(groundtruth, labels)
            # print("K-Means??????:%s???????????????????????????:%.5f?????????????????????:%0.3fs" % (
            #     jaccard_coefficient.__name__, jaccard_score, time.time() - t0))
            # silhouetteScore = silhouette_score(encoded_factors, labels, metric='euclidean')
            # davies_bouldinScore = davies_bouldin_score(encoded_factors, labels)
            # print("silhouetteScore:", silhouetteScore)
            # print("davies_bouldinScore:", davies_bouldinScore)
            # print("zlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzlyzly")






