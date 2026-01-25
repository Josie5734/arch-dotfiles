function _init()

    --set black as not transparent 
    palt(0,false)
    --set color 15 as transparent
    palt(15,true)

    car = {
        spr = 1,
        x = 20,
        y = 15,
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

    --road lines
    line(70,30,80,30,7)

    --grass below road
    rectfill(0,41,127,55,11)



    --draw car
    spr(car.spr,car.x,car.y,car.w,car.h)

end