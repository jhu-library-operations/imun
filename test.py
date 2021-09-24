#!/usr/bin/env python

from imun.image import Image

# i = Image("oapass/download-service:v1.0.1-4-g84f4be4")
i = Image("ghcr.io:8888/org/project/download-service:v1.0.1-4-g84f4be4")
i.process()
