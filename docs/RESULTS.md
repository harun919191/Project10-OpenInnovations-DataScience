# Results and experimental decisions

## Credit-card fraud detection

The ULB/Kaggle source contains 284,807 transactions and 492 fraud labels, approximately 0.17%. Duplicate removal and the split are documented in the original code and retained integrity tables. Stratified splitting reserves 30% for test; 20% of the remaining development subset is validation. Scaling and SMOTE are fitted/applied on training data only.

E0 establishes a StandardScaler 64-32-1 DNN. E1 uses balanced class weights; E2 uses SMOTE and improves recall at substantial false-positive cost. E3 substitutes RobustScaler. E4 introduces 128-64-32 hidden layers, batch normalisation and dropout (0.30/0.20). E5 retains that architecture and adds ReduceLROnPlateau, a 40-epoch ceiling and patience 7. The saved validation comparison supports E5's precision/recall balance; it is not a test-ranking exercise.

The threshold maximises validation F1 and is frozen at **0.475495308637619** before test scoring. Test counts are TN 84,962, FP 14, FN 31 and TP 111: precision 0.8880, recall 0.7817, F1 0.8315 and accuracy 0.9994713. PR-AUC (trapezoidal) is 0.8337256; average precision is a distinct quantity, 0.8338945. Do not interchange those metrics. Evidence: `Project1/results/P1_final_model_configuration.csv`, `P1_final_test_metrics.csv`, and `P1_experiment_results.csv` (validation results at threshold 0.5).

The 31 missed frauds have mean model output 0.0453 and median 0.0052 in the saved error summary. Threshold lowering increases review workload and cannot guarantee recovery of strongly missed cases. PCA features constrain semantic explanation; permutation/occlusion investigations in the source are model-behaviour probes, not causal explanations. Class prevalence, temporal drift, calibration, operational costs and monitoring would require new validation before deployment. A random stratified historical split is not a prospective fraud trial.

## Fashion-MNIST / smart logistics

A CNN is evaluated on a fixed 54,000/6,000/10,000 split. The experiment series compares a 20-epoch baseline, batch normalisation, cosine scheduling, their 20-epoch combination and the combined 40-epoch run. The baseline validates at 92.62%; cosine alone at 92.12%; batch norm at 93.00%; combined 20 at 93.02%; combined 40 at 93.82%. The final run is selected by validation accuracy with validation loss as tie-break, not by the test score.

Run `05_combined_40_seed42` completed 40 epochs; best epoch 36, validation loss 0.1769072. The frozen selection points to best.pt SHA-256 `f59035415713eb7e229a3a458c52ab63301a565dba59892cf97dc7deb6cbfbc7`. Test accuracy is 0.9299 and loss 0.2063582. T-shirt/top and Shirt contribute 168 mutual errors (89/79 directional); Shirt recall is 0.785. These confusions reveal class overlap beyond the headline accuracy.

The public test set was observed in an earlier AI-assisted pilot. The final Colab cycle froze selection before its final test evaluation, but the benchmark was not completely unseen across project history. This is a clothing-image benchmark, not a deployed logistics system. Softmax outputs are uncalibrated.

## CW2: cerebral-stroke status classification

The completed report and executed notebook contain a checksum-locked 43,400-row dataset with 783 stroke labels (1.804%). Development contains 34,720 rows / 626 events; locked test contains 8,680 / 157. Repeated stratified five-fold validation (three repeats), fold-local imputation/feature processing, age-only/full logistic baselines, forests, XGBoost and stacking support the comparison. Threshold selection is development-only using F2 with the documented specificity constraint.

KNN BMI imputation and XGBoost were selected before test access, with threshold **0.7494024481101682**. Test counts: TP 70, FN 87, FP 731 and TN 7,792. ROC-AUC 0.8444598, PR-AUC 0.0973580, recall 0.4458599, precision 0.0873908 and specificity 0.9142321. Logistic regression has higher observed test ROC-AUC (0.8500) and PR-AUC (0.1141); this does not retrospectively change the frozen model selection. The evidence does not support a claim that XGBoost is uniformly superior.

Supplementary calibration, feature ablation, missingness/outlier sensitivity, subgroup audit, bootstrap intervals, paired statistical comparison and SHAP are retained in the source notebook. Only the extracted aggregate summaries are published here. The selected primary result is uncalibrated; supplementary calibrated results must not replace it silently. CW2 labels average_precision_score as PR-AUC, unlike the separately recorded trapezoidal fraud PR-AUC. The locked test partition was reused for supplementary calibration reporting; it is not a new independent external cohort. Collection dates, follow-up horizon, named institution, sampling frame and label adjudication are missing. This is observed-status research, not diagnosis, future-stroke prediction, autonomous referral or validated rural-clinic deployment. The weak positive predictive value and high false-positive burden remain explicit limitations.
