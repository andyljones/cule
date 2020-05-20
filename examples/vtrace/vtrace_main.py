import os
import sys
from ..a2c.a2c_main import a2c_parser_options
from ..utils.launcher import main
from .train import worker

def vtrace_parser_options(parser):
    parser = a2c_parser_options(parser)

    parser.add_argument('--c-hat', type=int, default=1.0, help='Trace cutting truncation level (default: 1.0)')
    parser.add_argument('--rho-hat', type=int, default=1.0, help='Temporal difference truncation level (default: 1.0)')
    parser.add_argument('--num-minibatches', type=int, default=16, help='number of mini-batches in the set of environments (default: 16)')
    parser.add_argument('--num-steps-per-update', type=int, default=1, help='number of steps per update (default: 1)')

    return parser

def vtrace_main():
    import sys
    sys.argv = [''] + '--env-name PongNoFrameskip-v4 --normalize --use-cuda-env --num-ales 1200 --num-steps 20 --num-steps-per-update 1 --num-minibatches 20 --t-max 8000000 --evaluation-interval 200000'.split()
    main(vtrace_parser_options, worker)

if __name__ == '__main__':
    vtrace_main()
