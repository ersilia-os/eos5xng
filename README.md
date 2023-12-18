# ESKAPE pathogen inhibition

Prediction of antimicrobial potential using a dataset of 29537 compounds screened against the antibiotic resistant pathogen Burkholderia cenocepacia. The model uses the Chemprop Direct Message Passing Neural Network (D-MPNN) abd has an AUC score of 0.823 for the test set. It has been used to virtually screen the FDA approved drugs as well as a collection of natural product list (>200k compounds) with hit rates of 26% and 12% respectively.

## Identifiers

* EOS model ID: `eos5xng`
* Slug: `chemprop-eskape`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability that a compound inhibits bacterial pathogens with a focus on ESKAPE. Scores range from 0 to 1. With 1 indicating the highest probability for growth inhibitory activity.

## References

* [Publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9624395/)
* [Source Code](https://github.com/cardonalab/Prediction-of-ATB-Activity)
* Ersilia contributor: [GemmaTuron](https://github.com/GemmaTuron)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos5xng)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5xng.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos5xng) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9624395/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!