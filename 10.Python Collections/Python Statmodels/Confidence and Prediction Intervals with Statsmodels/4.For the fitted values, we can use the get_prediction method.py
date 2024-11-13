# Get prediction results
pred = model.get_prediction(X)
pred_summary = pred.summary_frame(alpha=0.05)  # 95% confidence intervals

# Extract confidence intervals
ci_lower = pred_summary['mean_ci_lower']
ci_upper = pred_summary['mean_ci_upper']
print(ci_lower)
print(ci_upper)
