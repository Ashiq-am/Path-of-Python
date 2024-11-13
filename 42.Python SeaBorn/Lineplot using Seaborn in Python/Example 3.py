# code added by devanshigupta1304
# plotting lineplot for signal with respect to timepoint
# using relplot, kind = "line"
# using standard deviation instead of confidence interval
sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri);
