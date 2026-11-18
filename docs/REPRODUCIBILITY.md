# Inspection and reproduction

## Safe inspection

Use Python 3 with its standard library: `python tools/verify_saved_results.py`. Browse notebooks without executing them. Public notebooks have no embedded outputs; original code and aggregate saved evidence remain inspectable. All original code cells sit behind `PORTFOLIO_EXECUTE=False`. Running them in that default state only displays an inspection notice. Historical metrics were not regenerated.

## Intentional ML execution

Use separate environments for fraud, Fashion-MNIST and stroke. Historical notebooks recorded Python 3.13.15; requirements files identify known versions and disclose unrecorded pins. Fashion used PyTorch 2.11.0+cu128 on a Tesla T4. These are historical records, not a tested clean-install lock; package availability, transitive resolution and binary compatibility have not been verified here.

From repository root, launch Jupyter and open `notebooks/`. In a disposable working copy, set PORTFOLIO_EXECUTE=True only after configuring input files. Project paths now resolve within the repository; cloud mounting was removed. Fraud retains SUBMISSION_MODE=True; changing it to False requires both RUN_TRAINING=True and RUN_FINAL_TEST=True in the new first control cell. Fashion retains its original RUN_TRAINING=False, SAVE_MY_REFLECTION=False and RUN_FINAL_TEST=False controls in later cells: those original cells take precedence and must be changed deliberately for a new run. CW2's coupled fitting/evaluation workflow requires PORTFOLIO_EXECUTE, RUN_TRAINING and RUN_FINAL_TEST all True. Its historical logic is retained, not split into a new experiment framework.

Fraud's final fitted models/scalers are excluded; code can retrain only after opt-in and dataset acquisition. Do not expect inspection mode to restore every original Python variable. Fashion retains best.pt for all five runs, configs, histories and the working dataset. Only load checkpoints from sources you trust: historical torch checkpoint deserialisation is not a safe format for untrusted input. CW2 models and raw inputs are excluded. None of the notebooks was trained or final-test evaluated during portfolio preparation.

## Data acquisition

Fraud: obtain an authorised `creditcard.csv` from [ULB/Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and place it at `Project1/data/creditcard.csv`. The original source has 284,807 rows and 31 columns. Read applicable provider terms; no raw rows or record-level predictions are distributed here.

Fashion-MNIST: the MIT-licensed `Project2/data/fashion_mnist_working.npz` and original manifest are supplied to preserve the exact seed-42 split and checksum. The manifest links all four upstream IDX files and hashes. Its `test_already_observed` flag must remain true. Licence text is alongside the dataset. The working NPZ hash is `ffde73969ffb5e8aa97f70e51c9387f156581df4018f4c2e142233ccc329b777`.

CW2: obtain the [Cerebral Stroke Dataset](https://www.kaggle.com/datasets/viviansam/cerebral-stroke-dataset), respecting provider terms. Place the exact coursework CSV at `CW2/dataset.csv`. SHA-256 must equal `540986aebc2cc8a9a6c907df5ea4fdf93e8b5e3dabacdd727337363757b539aa`. A similarly titled 5,110-row stroke dataset is not interchangeable. The provenance and redistribution terms of the supplied 43,400-row file were not fully established, so neither it nor patient-level outputs are included.

## Known limits

Seeds and deterministic controls improve repeatability but do not guarantee identical results across packages, hardware and accelerators. Exact training reproduction and clean-environment installation are unverified. Inspection checks establish internal consistency and asset integrity, not independent validation of saved experiments.

After any deliberate ML execution, clear or review newly embedded notebook outputs before publishing: tracked notebook outputs can contain raw rows even when future result files are ignored.
