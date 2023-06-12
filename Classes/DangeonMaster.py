def init(self, context, event, goal, score):
    self.context = context
    self.event = event
    self.goal = goal
    self.score = score


    def get_score(self):
        return self.score


    def set_score(self, score):
        self.score = score


    def get_goal(self):
        return self.goal


    def set_goal(self, goal):
        self.goal = goal


    def get_event(self):
        return self.event


def set_event(self, event):
    self.event = event


def get_context(self):
    return self.context


def set_context(self, context):
    self.context = context
