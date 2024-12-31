# Medical Data Visualizer

This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer



mask = np.tril(np.ones_like(corr, dtype=bool)) - This method uses the lower triangle and hides the upper triangle.

mask = np.triu(np.ones_like(corr, dtype=bool)) - This method uses the upper triangle and hides the lower triangle.

Lower Triangle:
- More commonly used.
- If you want to visualize all relationships, you can work with the lower triangle.


Upper Triangle:
- Used when less space is needed, or only a specific portion needs to be displayed.


For a standard correlation heatmap, the lower triangle is generally preferred.


df_cat = pd.melt(df, id_vars=['cardio'], 
                 value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

pd.melt is used to transform a DataFrame from "wide" format to "long" format. 
Columns specified in id_vars remain fixed, while columns in value_vars are unpivoted into variable and value columns.
