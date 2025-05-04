import numpy as np
import zarr


class DataManager:
    def __init__(self):
        self.__data = {}

    def load_data(self, path, tag):
        if tag not in self.__data:
            self.__data[tag] = [np.array(zarr.open(path, mode='r')["C"])]
        else:
            self.__data[tag].append(np.array(zarr.open(path, mode='r')["C"]))


    def get_time_split_data(self, time_sample_size, average_samples=False):
        data_map = {}
        for tag, data_list in self.__data.items():
            for data in data_list:
                if average_samples:
                    split_data = np.empty((data.shape[0], 0))
                    for i in range(time_sample_size, data.shape[1], time_sample_size):
                        data_sample = np.mean(data[:, i - time_sample_size : i], axis=1, keepdims=True)
                        split_data = np.append(split_data, data_sample, axis=1)
                else:
                    split_data = np.empty((data.shape[0] * time_sample_size, 0))
                    for i in range(time_sample_size, data.shape[1], time_sample_size):
                        data_sample = np.expand_dims(data[:, i - time_sample_size : i].ravel(), axis=1)
                        split_data = np.append(split_data, data_sample, axis=1)

                if tag not in data_map:
                    data_map[tag] = [split_data]
                else:
                    data_map[tag].append(split_data)
        return data_map

    def normalize_data(self):
        max_activity = 0
        for tag, data_list in self.__data.items():
            for data in data_list:
                data_max = np.amax(data)
                if max_activity < data_max:
                    max_activity = data_max

        for tag, data_list in self.__data.items():
            for i in range(len(data_list)):
                data_list[i] = (data_list[i] / max_activity)

    def shuffle_second_dimension(self, arr):
        np.random.shuffle(arr.T)
        return arr

    def shuffle_data(self):
        for tag in self.__data:
            self.__data[tag] = [self.shuffle_second_dimension(arr) for arr in self.__data[tag]]

    @property
    def data(self):
        return self.__data
