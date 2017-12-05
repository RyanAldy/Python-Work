import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

Knn = KNeighborsClassifier

with open("C:\\Users\\Admin\\Documents\\Data Science Project\\BreastCancerData.csv") as csvfile:
    raw_data = pd.read_csv(csvfile)

raw_data.columns = ["ID","Result","Mean_Radius","Mean_Texture","Mean_Perimeter",
                   "Mean_Area","Mean_Smoothness","Mean_Compactness", "Mean_Concavity",
                   "Mean_ConcavePoints", "Mean_Symmetry","Mean_FractalDimension",
                   "SE_Radius","SE_Texture","SE_Perimeter","SE_Area","SE_Smoothness",
                   "SE_Compactness","SE_Concavity","SE_ConcavePoints","SE_Symmetry",
                   "SE_FractalDimension","Worst_Radius","Worst_Texture","Worst_Perimeter",
                   "Worst_Area","Worst_Smoothness","Worst_Compactness","Worst_Concavity",
                   "Worst_ConcavePoints","Worst_Symmetry","Worst_FractalDimension"]

#print(data)
df = pd.DataFrame(raw_data)

# Axis = 1 tells Python this is a column to delete and not a row
BCD_NOID = df.drop('ID', axis=1)
#print(BCD_NOID)

BCD_NORESULTS = BCD_NOID.drop('Result', axis=1)

def FeatureScaling(x):
    return ((x - x.min() / x.max() - x.min()))

BCD_NORMALISED = FeatureScaling(BCD_NORESULTS)
print(BCD_NORMALISED)
