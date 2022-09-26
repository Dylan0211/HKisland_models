from config import *
from model_rank_metrics_tool import jaccard_similarity_coefficient

import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv(gt_building_name)
    gt_rank = df.loc[:, 'model_name'].tolist()

    df = pd.read_csv(one_month_building_name)
    one_month_rank = df.loc[:, 'model_name'].tolist()

    df = pd.read_csv(one_month_GAN_building_name)
    one_month_GAN_rank = df.loc[:, 'model_name'].tolist()

    # correlation coefficient
    corr_1 = jaccard_similarity_coefficient(gt_rank, one_month_rank, k)
    corr_2 = jaccard_similarity_coefficient(gt_rank, one_month_GAN_rank, k)
    print('target building: {}'.format(target_building))
    print('Jaccard correlation coefficient between gt and one-month is: {}'.format(corr_1))
    print('Jaccard correlation coefficient between gt and one-month (with GAN) is: {}'.format(corr_2))
