"""Check saved evidence only. No ML import, training or final-test evaluation."""
from pathlib import Path
import csv, hashlib, json, math
root=Path(__file__).resolve().parents[1]
with (root/'Project1/results/P1_final_test_metrics.csv').open() as f:
    m={r['Metric']:float(r['Value']) for r in csv.DictReader(f)}
tp,fp,fn,tn=[m[k] for k in ['True Positives','False Positives','False Negatives','True Negatives']]
assert (tp,fp,fn,tn)==(111,14,31,84962)
assert math.isclose(m['Precision'],tp/(tp+fp))
assert math.isclose(m['Recall'],tp/(tp+fn))
assert math.isclose(m['F1 Score'],2*tp/(2*tp+fp+fn))
assert math.isclose(m['Accuracy'],(tp+tn)/(tp+fp+fn+tn))
metrics=json.loads((root/'Project2/final_evaluation/metrics.json').read_text())
assert metrics['correct']==9299 and metrics['test_accuracy']==9299/10000
assert metrics['prior_public_test_observed'] is True
rows=list(csv.DictReader((root/'Project2/comparison.csv').open()))
winner=max(rows,key=lambda r:(float(r['validation_accuracy']),-float(r['validation_loss'])))
assert winner['run_id']=='05_combined_40_seed42' and int(winner['best_epoch'])==36
checkpoint=root/'Project2/my_experiments'/winner['run_id']/'best.pt'
assert hashlib.sha256(checkpoint.read_bytes()).hexdigest()==winner['checkpoint_sha256']
manifest=json.loads((root/'Project2/data/dataset_manifest.json').read_text())
assert hashlib.sha256((root/'Project2/data/fashion_mnist_working.npz').read_bytes()).hexdigest()==manifest['sha256']
stroke=json.loads((root/'CW2/results/final_summary.json').read_text())
assert stroke['selected_model']=='XGBoost'
sm=stroke['untouched_test_metrics']
assert (sm['tp'],sm['fp'],sm['fn'],sm['tn'])==(70,731,87,7792)
assert math.isclose(sm['precision'],sm['tp']/(sm['tp']+sm['fp']))
assert math.isclose(sm['recall'],sm['tp']/(sm['tp']+sm['fn']))
print('PASS: saved aggregate arithmetic, Fashion validation selection, checkpoint and dataset hashes; no model execution.')
