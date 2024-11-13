# code added by devanshigupta1304
# using relplot with kind = "line"
# adding style and hue semantic
sns.relplot(x="timepoint", y="signal", hue="region", style="event",
			kind="line", data=fmri);
