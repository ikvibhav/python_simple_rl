import logging
import os

import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


class GymEnvironment:
    def __init__(self, name, mode=None):
        self.name = name
        self.created_environment = None
        self.mode = mode

    def create_environment(self):
        try:
            self.created_environment = gym.make(self.name, render_mode=self.mode)
            print(f"Created environment {self.name}")
        except Exception as e:
            print(f"Error while creating {self.name}: {e}")

    def get_observation_space(self):
        return self.created_environment.observation_space

    def get_observation_space_high(self):
        return self.created_environment.observation_space.high

    def get_observation_space_low(self):
        return self.created_environment.observation_space.low

    def get_action_space_size(self):
        return self.created_environment.action_space.n

    def get_action_space_list(self):
        return [i for i in range(self.get_action_space_size())]


if __name__ == "__main__":
    env = GymEnvironment("MountainCar-v0", mode="human")
    env.create_environment()
    print(env.get_observation_space_high())
    print(env.get_observation_space_low())
    print(env.get_action_space_size())
    print(env.get_action_space_list())
