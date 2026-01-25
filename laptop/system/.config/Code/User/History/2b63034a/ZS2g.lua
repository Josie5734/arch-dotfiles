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

    --seperator line
    line(0,60,127,60,14)

    --draw car
    spr(car.n,car.x,car.y,car.w,car.h)

end