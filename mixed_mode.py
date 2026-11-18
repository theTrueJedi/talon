from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:
    def mixed_mode():
        """Enable both command and dictation mode simultaneously."""
        actions.mode.disable("sleep")
        actions.mode.enable("command")
        actions.mode.enable("dictation")
        actions.app.notify("Mixed Mode: Command + Dictation")