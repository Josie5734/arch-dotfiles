function _init()

    car = {
        n = 1,
        x = 20,
        y = 20,
        h = 2,
        w = 4
    }

    cls()

end



function _update()

end



function _draw()

    cls()

    --grass above road
    rectfill(0,10,127,19,3)

    --road
    rectfill(0,20,127,40,5)

    --grass below road
    rectfill(0,41,127,55,11)



    --draw car
    spr(car.n,car.x,car.y,car.w,car.h)

end