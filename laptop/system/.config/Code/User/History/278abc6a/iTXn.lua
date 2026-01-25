function _init()

    --colors
    legs = 2

    --spiders body
    body = {
        x = 60,
        y = 60,
        r = 4,
        c = 14
    }

    --left leg
    leg_left = {
        j1 = { --joint one
            sx = body.x - 2,
            sy = body.y,
            ex = body.x - 10,
            ey = body.y - 10
        },
        j2 = { --joint two
            sx = body.x - 10,
            sy = body.y - 10,
            ex = body.x - 20,
            ey = body.y + 20
        }
    }
    leg_right = {
        j1 = { --joint one
            sx = body.x + 2,
            sy = body.y,
            ex = body.x + 10,
            ey = body.y - 10
        },
        j2 = { --joint two
            sx = body.x + 10,
            sy = body.y - 10,
            ex = body.x + 20,
            ey = body.y + 20
        }
    }

    cls()

end

function _update()

    if btnp(0) then
        body.x -= 1
    end
    if btnp(1) then
        body.x += 1
    end 
    
    leg_update()

end

function _draw()

    cls()

    --draw body
    circfill(body.x,body.y,body.r,body.c)

    --left leg
    line(leg_left.j1.sx,leg_left.j1.sy,leg_left.j1.ex,leg_left.j1.ey,legs)
    line(leg_left.j2.sx,leg_left.j2.sy,leg_left.j2.ex,leg_left.j2.ey,legs)
    
    --right leg
    line(leg_right.j1.sx,leg_right.j1.sy,leg_right.j1.ex,leg_right.j1.ey,legs)
    line(leg_right.j2.sx,leg_right.j2.sy,leg_right.j2.ex,leg_right.j2.ey,legs)

end



function leg_update()

    leg_left = {
        j1 = { --joint one
            sx = body.x - 2,
            sy = body.y,
            ex = body.x - 10,
            ey = body.y - 10
        },
        j2 = { --joint two
            sx = body.x - 10,
            sy = body.y - 10,
            ex = body.x - 20,
            ey = body.y + 20
        }
    }
    leg_right = {
        j1 = { --joint one
            sx = body.x + 2,
            sy = body.y,
            ex = body.x + 10,
            ey = body.y - 10
        },
        j2 = { --joint two
            sx = body.x + 10,
            sy = body.y - 10,
            ex = body.x + 20,
            ey = body.y + 20
        }
    }

end