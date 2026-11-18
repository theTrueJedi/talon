window focus <user.text>:
    user.focus_window_by_title(user.text)

win focus <user.text>:
    user.focus_window_by_title(user.text)

# Uses physical OS clicks for all Rango hints to cleanly cross iframe boundaries
tag: browser
-
click <user.rango_target>:
    user.rango_mouse_click_element(rango_target, 0)

# App-scoped rule for Google Chrome
app: chrome
-
group <user.text>:
    key(cmd-shift-a)
    sleep(150ms)
    insert(user.text)
    sleep(150ms)
    key(enter)