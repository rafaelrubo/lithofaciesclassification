# Lithofacies Classification

This repository has been created for sharing codes used on the research submitted to the scientific Journal Earth Science Informatics.  
  
The manuscript's title is:  
"**Carbonate lithofacies classification in optical microscopy: a data-centric approach using augmentation and GAN synthetic images**".  
It has been submitted on May 19th, 2022.

These are the authors:  
Rafael Andrello Rubo - rafael.rubo@petrobras.com.br  
Mateus Fontana Michelon - mateus.michelon@petrobras.com.br  
Cleyton de Carvalho Carneiro - cleytoncarneiro@usp.br  

The codes are available under the MIT License.  
The models were trained in a Windows based Python installation. In Linux, a few modifications may be necessary.
System details used for training: 1. Processor: Intel® Core™ i5-8250U (1.6 GHz); 2. RAM Memory: 8GB, DDR4, 2400MHz; 3. GPU: NVIDIA® GeForce® MX150 with GDDR5-4GB.
Classification models may be trained in the cloud. They were tested in Google Colab. However, it may be necessary to uso Colab Pro, considering the size of the training dataset.

If you are the editor or a reviewer for the Journal, these are the codes mentioned in the manuscript:

[NLM_SpectralAugmentations.ijm](NLM_SpectralAugmentations.ijm)

[GeometricAugmentations.py](GeometricAugmentations.py)

[GANSyntheticImages.py](GANSyntheticImages.py)

[TrainingModels.py](TrainingModels.py)
