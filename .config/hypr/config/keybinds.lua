----------------------------
---- GLOBAL KEYBINDINGS ----
----------------------------

---launch programs---
hl.bind(mainMod .. " + Q", hl.dsp.exec_cmd(programs.terminal)) --terminal
hl.bind(mainMod .. " + return", hl.dsp.exec_cmd(programs.terminal)) --alternate terminal launch
hl.bind(mainMod .. " + Z", hl.dsp.exec_cmd(programs.editor)) --launch zeditor
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd(programs.fileManager)) --file manager
hl.bind(mainMod .. " + R", hl.dsp.exec_cmd(programs.launcher)) --launcher

hl.bind(mainMod .. " + backspace", hl.dsp.exec_cmd(programs.browser)) --firefox window
hl.bind(mainMod .. " + SHIFT + backspace", hl.dsp.exec_cmd(programs.browser .. " --private-window")) --firefox private window

hl.bind(mainMod .. " + C", hl.dsp.window.close()) --close window
hl.bind(mainMod .. " + mouse:274", hl.dsp.window.close()) --alternate close window with middle mouse click



---media--- (requires playerctl)
hl.bind("code:127",  hl.dsp.exec_cmd("playerctl play-pause"), { locked = true }) --play/pause media



---hyprland controls---
hl.bind(mainMod .. " + M", hl.dsp.exec_cmd("command -v hyprshutdown >/dev/null 2>&1 && hyprshutdown || hyprctl dispatch 'hl.dsp.exit()'")) --reload hyprland

hl.bind("print", hl.dsp.exec_cmd("hyprshot -m region")) --screenshot region on regular PrintScreen press
hl.bind(mainMod .. " + print", hl.dsp.exec_cmd("hyprshot -m window")) --screenshot window on mod + PrintScreen press

hl.bind(mainMod .. " + V", hl.dsp.window.float({ action = "toggle" })) --toggle floating for active window
hl.bind(mainMod .. " + P", hl.dsp.window.pseudo()) --set pseudo for window



---navigation and workspaces---

--directional keybinds
for _,d in pairs(directions) do --for each direction (d)
    hl.bind(mainMod .. " + " .. d, hl.dsp.focus({ direction = d})) --move focus in direction
    hl.bind(mainMod .. " + SHIFT + " .. d, hl.dsp.window.move({direction = d})) -- move window in direction
    hl.bind(mainMod .. " + CTRL + " .. d, hl.dsp.window.swap({direction = d})) -- swap window in direction
end

-- move workspace and move window to workspace
for i = 1, 10 do
    local key = i % 10 -- 10 maps to key 0
    hl.bind(mainMod .. " + " .. key,             hl.dsp.focus({ workspace = i}))
    hl.bind(mainMod .. " + SHIFT + " .. key,     hl.dsp.window.move({ workspace = i }))
end

-- Scroll through existing workspaces with mainMod + scroll
-- hl.bind(mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
-- hl.bind(mainMod .. " + mouse_up",   hl.dsp.focus({ workspace = "e-1" }))

-- Move/resize windows with mainMod + LMB/RMB and dragging
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(),   { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })



---layout specific---
if layout == "dwindle" then --dwindle
    hl.bind(mainMod .. " + J", hl.dsp.layout("togglesplit")) --toggle split directions (dwindle only)
elseif layout == "scrolling" then --scrolling
    hl.bind(mainMod .. " + mouse_down", hl.dsp.layout("move -col"), {mouse = true}) --scroll the columns
    hl.bind(mainMod .. " + mouse_up",   hl.dsp.layout("move +col"), {mouse = true}) --with the mousewheel

    hl.bind(mainMod .. " + F", hl.dsp.layout("colresize +conf")) --resize columns
    hl.bind(mainMod .. " + SHIFT + F", hl.dsp.layout("colresize -conf"))
end



---special workspaces---
hl.bind(mainMod .. " + S",         hl.dsp.workspace.toggle_special("scratch")) --scratchpad
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.window.move({ workspace = "special:scratch" }))



---dedicated workspaces--- (each uses a special named workspace with a rule to open the specific program if not already open)
local dedicated = mainMod .. " + CTRL" --shorten command

-- whatsapp
hl.bind(dedicated .. " + 1", hl.dsp.workspace.toggle_special("1.whatsapp"))
hl.workspace_rule({ workspace = "special:1.whatsapp",on_created_empty = programs.browser .. " --new-window web.whatsapp.com" })

--terminal
hl.bind(dedicated .. " + 2", hl.dsp.workspace.toggle_special("2.terminal"))
hl.workspace_rule({ workspace = "special:2.terminal",on_created_empty = programs.terminal })

--private browser window
hl.bind(dedicated .. " + 3", hl.dsp.workspace.toggle_special("3.privateBrowser"))
hl.workspace_rule({ workspace = "special:3.privateBrowser",on_created_empty = programs.browser .. " --private-window"})
