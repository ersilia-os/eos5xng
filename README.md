# Burkholderia cenocepacia inhibition

Flags inhibitors of Burkholderia cenocepacia, an opportunistic Gram-negative pathogen dangerous to people with cystic fibrosis and notoriously resistant to most antibiotics. Rahman and colleagues screened a large compound collection against the organism and trained a classifier on the results, then showed prospectively that model-guided selection raised the hit rate substantially above random screening. That enrichment result, rather than retrospective accuracy, is the strongest evidence the model works.

This model was incorporated on 2023-12-03.Last packaged on 2025-09-15.

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
- **Interpretation:** Probability of Burkholderia cenocepacia growth inhibition, ranging from 0 to 1.

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
- **Environment Size (Mb):** `5852`
- **Image Size (Mb):** `6363.26`

**Computational Performance (seconds):**
- 10 inputs: `36.52`
- 100 inputs: `36.04`
- 10000 inputs: `981.03`

### References
- **Source Code**: [https://github.com/cardonalab/Prediction-of-ATB-Activity](https://github.com/cardonalab/Prediction-of-ATB-Activity)
- **Publication**: [https://doi.org/10.1371/journal.pcbi.1010613](https://doi.org/10.1371/journal.pcbi.1010613)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [Richioo](https://github.com/Richioo)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

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
