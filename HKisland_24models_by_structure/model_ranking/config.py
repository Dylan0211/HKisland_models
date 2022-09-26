target_building = 'DEH'
GAN_building = 'OIE'
context_a = 1
context_b = 4

k = 10

gt_building_name = '../test_on_gt/test_result/test_on_{}_gt_result.csv'.format(target_building)
one_month_building_name = \
    '../test_on_one_month_ashrae/test_result/test_on_{}_one_month_ashrae_{}_result.csv'.format(
        target_building, context_a
    )
one_month_GAN_building_name = \
    '../test_on_one_month_ashrae_and_GAN/test_result/test_on_{}_with_{}_GAN_ashrae_{}_to_{}_result.csv'.format(
    target_building, GAN_building, context_a, context_b
)

