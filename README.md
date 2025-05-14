# Burkholderia cenocepacia inhibition

Prediction of antimicrobial potential using a dataset of 29537 compounds screened against the antibiotic resistant pathogen Burkholderia cenocepacia. The model uses the Chemprop Direct Message Passing Neural Network (D-MPNN) abd has an AUC score of 0.823 for the test set. It has been used to virtually screen the FDA approved drugs as well as a collection of natural product list (>200k compounds) with hit rates of 26% and 12% respectively.

This model was incorporated on 2023-12-03.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5xng`
- **Slug:** `chemprop-burkholderia`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Burkholderia cenocepacia`
- **Tags:** `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability that a compound inhibits the drug resistant bacteria Burkholderia cenocepacia. Scores range from 0 to 1. With 1 indicating the highest probability for growth inhibitory activity.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| bcenocepacia_inhibition | float | high | Probability score that the compound inhibits the growth of Burkholderia cenocepacia |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5xng](https://hub.docker.com/r/ersiliaos/eos5xng)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5xng.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5xng.zip)

### Resource Consumption
- **Model Size (Mb):** `215`
- **Environment Size (Mb):** `5839`
- **Image Size (Mb):** `6346.17`

**Computational Performance (seconds):**
- 10 inputs: `59.57`
- 100 inputs: `77.36`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/cardonalab/Prediction-of-ATB-Activity](https://github.com/cardonalab/Prediction-of-ATB-Activity)
- **Publication**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9624395/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9624395/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [Richioo](https://github.com/Richioo)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5xng
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5xng
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
