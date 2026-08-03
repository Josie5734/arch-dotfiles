--Josie5734 Arch+Hyprland config

------------------
---- IMPORTS ----
------------------

require("config.values") --global variables
local colors = require("config.catppuccin-mocha") --colorscheme

require("config.hardware") --displays and input
require("config.keybinds") --keybinds
require("config.animations") --animations



-------------------
---- AUTOSTART ----
-------------------

--startup programs
hl.on("hyprland.start", function ()
    hl.exec_cmd("systemctl --user start hyprpolkitagent") --start hyprpolkit
  hl.exec_cmd(programs.idle)
  hl.exec_cmd(programs.bar)
end)



-------------------------------
---- ENVIRONMENT VARIABLES ----
-------------------------------

--cursor
hl.env("XCURSOR_SIZE", "24")
hl.env("HYPRCURSOR_SIZE", "24")

--darkmode
hl.env("GTK_THEME","Adwaita:dark") --GTK
hl.env("QT_QPA_PLATFORMTHEME","qt6ct") --QT6 (requires qt6ct)



-----------------------
---- LOOK AND FEEL ----
-----------------------

-- Refer to https://wiki.hypr.land/Configuring/Basics/Variables/
hl.config({
    general = {
        gaps_in  = 5, --gap between window
        gaps_out = 20, --gap between window and monitor edge

        border_size = 2,

        col = {
            active_border   = { colors = {"rgba(".. colors.lavenderAlpha .."ee)", "rgba(" .. colors.mauveAlpha .. "ee)"}, angle = 45 },
            inactive_border = "rgba(" .. colors.blueAlpha .. "aa)",
        },

        -- Set to true to enable resizing windows by clicking and dragging on borders and gaps
        resize_on_border = false,

        -- Please see https://wiki.hypr.land/Configuring/Advanced-and-Cool/Tearing/ before you turn this on
        allow_tearing = false,

        layout = "dwindle", --standard tilingwm layout
    },

    --layout settings
    dwindle = {
        force_split = 2, --split new windows to the right/bottom
        preserve_split = true, -- You probably want this
        smart_split = true, --open new splits in the direction of the cursor
    },

    decoration = {
	--corners
        rounding       = 10,
        rounding_power = 2,

        -- Change transparency of focused and unfocused windows
        active_opacity   = 1.0,
        inactive_opacity = 1.0,

        shadow = {
            enabled      = true,
            range        = 4,
            render_power = 3,
            color        = 0xee1a1a1a,
        },

        blur = {
            enabled   = true,
            size      = 3,
            passes    = 1,
            vibrancy  = 0.1696,
        },
    },

    misc = {
        disable_hyprland_logo = true, -- disable builtin wallpaper, use solid color by default instead
    	disable_splash_rendering = true, --disable splash text
    },

    animations = {
        enabled = true,
    	workspace_wraparound = true,
    },
})


-- Ref https://wiki.hypr.land/Configuring/Basics/Workspace-Rules/
-- "Smart gaps" / "No gaps when only"
-- uncomment all if you wish to use that.
-- hl.workspace_rule({ workspace = "w[tv1]", gaps_out = 0, gaps_in = 0 })
-- hl.workspace_rule({ workspace = "f[1]",   gaps_out = 0, gaps_in = 0 })
-- hl.window_rule({
--     name  = "no-gaps-wtv1",
--     match = { float = false, workspace = "w[tv1]" },
--     border_size = 0,
--     rounding    = 0,
-- })
-- hl.window_rule({
--     name  = "no-gaps-f1",
--     match = { float = false, workspace = "f[1]" },
--     border_size = 0,
--     rounding    = 0,
-- })



--------------------------------
---- WINDOWS AND WORKSPACES ----
--------------------------------

-- See https://wiki.hypr.land/Configuring/Basics/Window-Rules/
-- and https://wiki.hypr.land/Configuring/Basics/Workspace-Rules/

-- Example window rules that are useful

local suppressMaximizeRule = hl.window_rule({
    -- Ignore maximize requests from all apps. You'll probably like this.
    name  = "suppress-maximize-events",
    match = { class = ".*" },

    suppress_event = "maximize",
})
-- suppressMaximizeRule:set_enabled(false)

hl.window_rule({
    -- Fix some dragging issues with XWayland
    name  = "fix-xwayland-drags",
    match = {
        class      = "^$",
        title      = "^$",
        xwayland   = true,
        float      = true,
        fullscreen = false,
        pin        = false,
    },

    no_focus = true,
})

-- Layer rules also return a handle.
-- local overlayLayerRule = hl.layer_rule({
--     name  = "no-anim-overlay",
--     match = { namespace = "^my-overlay$" },
--     no_anim = true,
-- })
-- overlayLayerRule:set_enabled(false)

-- Hyprland-run windowrule
hl.window_rule({
    name  = "move-hyprland-run",
    match = { class = "hyprland-run" },

    move  = "20 monitor_h-120",
    float = true,
})


-- set default workspaces for multimonitor, make persistent
hl.workspace_rule({ workspace = "1", monitor = monitors.iiyama , default = true, persistent = true })
hl.workspace_rule({ workspace = "2", monitor = monitors.benq , default = true, persistent = true })
hl.workspace_rule({ workspace = "3", monitor = monitors.logik, default = true, persistent = true })
