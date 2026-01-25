--card sizes
--[[
    width = 10, height = 15
    border = 1px, white(7)
    filled with color of card
    text for numbers = x+4, y+15, color=white(7)
    text for +4/+2 = x+2

]]

function _init()

    cls()

end



function _update()



end



function _draw()

    cls(4)

    rect(10,10,20,25,7)
    rectfill(11,11,19,24,8)
    print("7",14,15,7)



end