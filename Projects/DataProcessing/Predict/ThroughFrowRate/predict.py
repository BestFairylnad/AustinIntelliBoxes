# coding: utf8
""" 
@ File: predict.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-08
"""

import sys

sys.dont_write_bytecode = True

import pandas
from loguru import logger
import os
import numpy


class DataFormat:

    @staticmethod
    def excel_convert_to_matrix(excel_file_path=None):
        if excel_file_path is None:
            logger.error('文件不存在')
            sys.exit()
        else:
            try:
                if os.path.isfile(excel_file_path):
                    matrix = pandas.read_excel(io=excel_file_path).values
                    return matrix
                else:
                    logger.error('文件存在')
            except Exception as error:
                logger.error(error)
                logger.exception(error)
                sys.exit()


class PCA:

    @staticmethod
    def std_matrix_r_squared(matrix):
        std_matrix = (matrix - numpy.mean(matrix, axis=0)) / numpy.std(matrix, axis=0)
        r_squared_matrix = numpy.corrcoef(std_matrix, rowvar=False) ** 2
        return std_matrix, r_squared_matrix
    
    @staticmethod
    def eigen_decomposition(r_squared_matrix):
        eigen_values, eigen_vectors_matrix = numpy.linalg.eig(r_squared_matrix)
        return eigen_values, eigen_vectors_matrix
    
    @staticmethod
    def variance_contribution(eigen_values, eigen_vectors_matrix):
        variance_exp = eigen_values / numpy.sum(eigen_values)
        cum_variance_exp_matrix = numpy.cumsum(eigen_vectors_matrix)
        return variance_exp, cum_variance_exp_matrix
    
    @staticmethod
    def variance_contribution_gt_95(cum_variance_exp_matrix):
        n_components = numpy.argmax(cum_variance_exp_matrix >= 0.95) + 1
        return n_components
    
    @staticmethod
    def scores(std_matrix, eigen_vectors_matrix, n_components):
        scores = numpy.dot(std_matrix, eigen_vectors_matrix[:, :n_components])
        return scores


def main():
    matrix = DataFormat.excel_convert_to_matrix('data/data.xlsx')
    if isinstance(matrix[:, 0][0], pandas.Timestamp):
        timestamp_convert_to_int = [int(data.strftime('%Y%m%d%H%M%S')) for data in matrix[:, 0]]
        matrix[:, 0] = timestamp_convert_to_int
    print('源矩阵数据:\n{}'.format(matrix))
    std_matrix, r_squared_matrix = PCA.std_matrix_r_squared(matrix=matrix.tolist())
    print('标准化矩阵:\n{}'.format(std_matrix))
    print('标准化矩阵的决定系数矩阵:\n{}'.format(r_squared_matrix))
    eigen_values, eigen_vectors_matrix = PCA.eigen_decomposition(r_squared_matrix=r_squared_matrix)
    print('矩阵的特征值: {}'.format(eigen_values))
    print('矩阵的特征向量:\n{}'.format(eigen_vectors_matrix))
    variance_exp, cum_variance_exp_matrix = PCA.variance_contribution(eigen_values=eigen_values, eigen_vectors_matrix=eigen_vectors_matrix)
    print("方差贡献率:{}".format(variance_exp))
    print("累计方差贡献率:\n{}".format(cum_variance_exp_matrix))
    n_components = PCA.variance_contribution_gt_95(cum_variance_exp_matrix=cum_variance_exp_matrix)
    print('方差贡献率大于95%:{}'.format(n_components))
    scores = PCA.scores(std_matrix=std_matrix, eigen_vectors_matrix=eigen_vectors_matrix, n_components=n_components)
    print('主成分的得分:\n{}'.format(scores))
    corr_matrix = numpy.corrcoef(scores)
    print('相关性系数矩阵:\n{}'.format(corr_matrix))
    return


if __name__ == '__main__':
    main()
