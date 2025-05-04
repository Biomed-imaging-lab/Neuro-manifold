from sklearn.manifold import MDS, TSNE
from sklearn.decomposition import PCA, FastICA
import umap

import numpy as np


class ManifoldManager:
    def __init__(self):
        pass

    def get_manifold_map(self, model, data_map):
        manifold_map = {}
        for tag, data_list in data_map.items():
            for data in data_list:
                manifold = model.fit_transform(np.transpose(data))
                if tag not in manifold_map:
                    manifold_map[tag] = [manifold]
                else:
                    manifold_map[tag].append(manifold)

        return manifold_map


    def MDS(self, data):
        model = MDS(n_components=3)
        manifold = model.fit_transform(np.transpose(data))
        return manifold

    def UMAP(self, data):
        model = umap.UMAP(n_components=3)
        manifold = model.fit_transform(np.transpose(data))
        return manifold

    def t_SNE(self, data, shuffle=False, **kwargs):
        tsne = TSNE(n_components=3, **kwargs)
        manifold = tsne.fit_transform(np.transpose(data))
        
        if shuffle:
            np.random.shuffle(manifold)  # Перемешиваем строки (точки) в manifold
        return manifold

    def PCA(self, data):
        model = PCA(n_components=3)
        manifold = model.fit_transform(np.transpose(data))
        return manifold

    def ICA(self, data):
        model = FastICA(n_components=3)
        manifold = model.fit_transform(np.transpose(data))
        return manifold