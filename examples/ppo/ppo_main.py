import os
import sys

from ..a2c.a2c_main import a2c_parser_options
from ..utils.launcher import main
from .train import worker

def ppo_parser_options(parser):
    parser = a2c_parser_options(parser)

    parser.add_argument('--batch-size', type=int, default=256)
    parser.add_argument('--clip-epsilon', type=float, default=0.1, help='ppo clip parameter (default: 0.1)')
    parser.add_argument('--ppo-epoch', type=int, default=3, help='Number of ppo epochs (default: 3)')

    return parser

def ppo_main():
    main(ppo_parser_options, worker)

def test():
    import sys
    args = '--env-name PongNoFrameskip-v4 --normalize --use-cuda-env --num-ales 1200 --num-steps 20 --t-max 8000000 --evaluation-interval 200000'
    sys.argv = [''] + args.split()
    ppo_main()


if __name__ == '__main__':
    ppo_main()
