import random

MAX_STEPS = 20
ACTION_SPACE = [-1, 1]
STATE_SPACE = [1.0, 2.0, 1.0]


class Environment:
    def __init__(self):
        self.steps_left = MAX_STEPS

    def get_observation(self):
        return ACTION_SPACE

    def get_actions(self):
        return STATE_SPACE

    def is_done(self):
        return self.steps_left == 0

    def action(self):
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: Environment):
        reward = env.action()
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print(
        f"Total reward after {MAX_STEPS - env.steps_left} steps: {agent.total_reward}"
    )
