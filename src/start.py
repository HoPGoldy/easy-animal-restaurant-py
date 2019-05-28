from restaurant_control import RestaurantControl

if __name__ == "__main__":
    restaurant = RestaurantControl()
    # input('请将场景置于大厅后点任意键继续')
    
    while True:
        print('\n执行大厅操作\n')
        restaurant.go_to('hall')
        restaurant.order()
        restaurant.pick_site_money()
        restaurant.pick_hall_money()

        # restaurant.click_propaganda(20)
        print('\n执行厨房操作\n')
        restaurant.go_to('kitchen')
        restaurant.pick_kitchen_money()