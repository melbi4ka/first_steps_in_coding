annual_basket_tax = int(input())
basket_sneakers = annual_basket_tax * 0.6
basket_equipment = basket_sneakers * 0.8
basket_ball = 1/4 * basket_equipment
basket_accessories = 1/5 * basket_ball
total_sum = annual_basket_tax + basket_sneakers + basket_equipment + basket_ball + basket_accessories
print(total_sum)

