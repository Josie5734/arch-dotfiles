
------------------
---- MONITORS ----
------------------

-- See https://wiki.hypr.land/Configuring/Basics/Monitors/

--left
hl.monitor({ output = monitors.iiyama, mode = "1920x1080", position = "0x0", scale = 1, })

--middle
hl.monitor({ output = monitors.benq, mode="1920x1080@100", position= "1920x0", scale = 1 })

--right (vertical and slightly above other 2)
hl.monitor({ output = monitors.logik, mode = "1920x1080", position = "3840x-300", scale = 1, transform = 1 })



---------------
---- INPUT ----
---------------

hl.config({
    input = {
        kb_layout  = "gb", --keyboard layout
        follow_mouse = 1, --focus window under cursor
    },
})
