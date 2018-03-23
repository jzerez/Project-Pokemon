# Project-Pokemon
A project that generates new Pokemon sprites (aka, my first tinkering project using GANs). The bulk of this project was done simply in scraping Pokemon sprites off the Internet to use as training data.

## Implementation 1: DCGAN
In this first implementation of the project, a Tensorflow implementation of a [DCGAN](https://github.com/carpedm20/DCGAN-tensorflow) was used.


 The 1000 or so sprites that exist don't seem to be enough to create cohesive Pokemon. Below is a sample of some of the sprites the GAN produced. The overall shape of each sprite seems pretty realistic, but there are no individual features within each sprite, and the colors are not cohesive at all, which is rather unfortunate.

 ![alt](https://github.com/jzerez/Project-Pokemon/blob/master/test2/test_arange_42.png)
