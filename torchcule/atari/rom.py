"""CuLE (CUda Learning Environment module)

This module provides access to several RL environments that generate data
on the CPU or GPU.
"""

import gym
import os

from torchcule_atari import AtariRom

class Rom(AtariRom):

    def __init__(self, env_name):
        game_path = gym.make(env_name).env.game_path
        if not os.path.exists(game_path):
            raise IOError('Requested environment (%s) does not exist in valid list of environments')
        super(Rom, self).__init__(game_path)

    def __repr__(self):
        return 'Name       : {}\n'\
               'Controller : {}\n'\
               'Swapped    : {}\n'\
               'Left Diff  : {}\n'\
               'Right Diff : {}\n'\
               'Type       : {}\n'\
               'Display    : {}\n'\
               'ROM Size   : {}\n'\
               'RAM Size   : {}\n'\
               'MD5        : {}\n'\
               .format(self.game_name(),
                       'Paddles' if self.use_paddles() else 'Joystick',
                       'Yes' if self.swap_paddles() or self.swap_ports() else 'No',
                       'B' if self.player_left_difficulty_B() else 'A',
                       'B' if self.player_right_difficulty_B() else 'A',
                       self.type(),
                       'NTSC' if self.is_ntsc() else 'PAL',
                       self.rom_size(),
                       self.ram_size(),
                       self.md5())

