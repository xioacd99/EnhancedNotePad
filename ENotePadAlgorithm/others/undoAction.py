class UndoAction(object):
    def __init__(self):
        self.actions = []
        self.tmpActions = []

    def undo(self):
        self.tmpActions.append(self.actions.pop())

    def redo(self):
        self.actions.append(self.tmpActions.pop())
