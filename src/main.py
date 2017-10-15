#!/usr/bin/python
# -*- coding: utf-8 -*-
import camera
from argparse import ArgumentParser


def main(options):
    """
    Captures camera images according to options
    :param options:
    :return:
    """
    cam=camera.camera(options.wt,options.ht)
    while True:
        cam.capture_image()
        cam.show_image()
        cam.delay_camera(options.time)


if __name__ == '__main__':
    argp = ArgumentParser(description='Program for automatic algebraic annotation of a game chess',
                          epilog='Copyright 2017 Autor under license MIT')
    argp.add_argument('-t', help='Time in miliseconds that capture images', dest='time', required='False', type=int)
    argp.add_argument('-wt', help='Weight of the image', dest='wt', type=int)
    argp.add_argument('-ht', help='Height of the image', dest='ht', type=int)
    opts = argp.parse_args()
    main(opts)
