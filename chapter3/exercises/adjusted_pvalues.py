# RCDS Further hypothesis testing
# Jesus Urtasun Elizari - Imperial College London
# Chapter 3 - Adjusted pvalues

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

# Example p-values
p_values = np.array([0.01, 0.03, 0.05, 0.4, 0.1])

# Bonferroni correction
alpha = 0.05
num_comparisons = len(p_values)
adjusted_p_values_bonferroni = p_values * num_comparisons
adjusted_p_values_bonferroni = np.minimum(adjusted_p_values_bonferroni, 1.0)
print("Original p-values:", p_values)
print("Bonferroni adjusted p-values:", adjusted_p_values_bonferroni)

# Plot original and Bonferroni corrected p-values
plt.plot(range(1, num_comparisons + 1), p_values, "bo", label = "Original p-values")
plt.plot(range(1, num_comparisons + 1), adjusted_p_values_bonferroni, "r*", label = "Adjusted p-values (Bonferroni)")
plt.axhline(alpha, color = "g", linestyle = "--", label = "Significance threshold")
plt.xlabel("Comparison")
plt.ylabel("P-value")
plt.title("Bonferroni Correction")
plt.legend()
plt.show()

# Benjamini-Hochberg (BH) correction
adjusted_p_values_bh = multipletests(p_values, method = "fdr_bh")[1]
print("Original p-values:", p_values)
print("Benjamini-Hochberg (BH) adjusted p-values:", adjusted_p_values_bh)

# Plot original and adjusted p-values for Benjamini-Hochberg correction
plt.plot(range(1, num_comparisons + 1), p_values, "bo", label = "Original p-values")
plt.plot(range(1, num_comparisons + 1), adjusted_p_values_bh, "r*", label = "Adjusted p-values (BH)")
plt.axhline(alpha, color = "g", linestyle = "--", label = "Significance threshold")
plt.xlabel("Comparison")
plt.ylabel("P-value")
plt.title("Benjamini-Hochberg Correction")
plt.legend()
plt.show()