from talon import Module, ui

mod = Module()

@mod.action_class
class Actions:
    def focus_window_by_title(title_query: str) -> bool:
        """Focuses the first window matching the spoken title or app name."""
        query = title_query.lower().strip()

        for app in ui.apps(background=False):
            for win in app.windows():
                # Matches window title (e.g. named Chrome window or tab title) or app name
                if not win.hidden and (
                    (win.title and query in win.title.lower())
                    or (app.name and query in app.name.lower())
                ):
                    app.focus()
                    win.focus()
                    return True
        return False