import pandas as pd
import numpy as np
import json

def generate_shuffled_edges(
    input_csv="edges.csv",
    output_json="edges.json",
    num_iterations=10,
    min_sample_size=50,
    shuffle_individual_columns=True,
    avoid_duplicates=True
):
    df = pd.read_csv(input_csv).astype(str)
    out = [df.to_dict(orient="records")]  # include original edges

    for _ in range(num_iterations):
        sample_size = np.random.randint(min_sample_size, len(df))
        resampled_df = df.sample(n=sample_size, replace=False).reset_index(drop=True)

        if shuffle_individual_columns:
            resampled_df = pd.DataFrame({
                'source': np.random.permutation(resampled_df['source'].values),
                'target': np.random.permutation(resampled_df['target'].values),
                'value':  np.random.permutation(resampled_df['value'].values)
            })

        else:
            # Shuffle full rows instead of columns
            resampled_df = resampled_df.sample(frac=1).reset_index(drop=True)

        if avoid_duplicates:
            seen = set()
            unique_rows = []
            for row in resampled_df.itertuples(index=False):
                key = (row.source, row.target)
                if key not in seen:
                    seen.add(key)
                    unique_rows.append({'source': row.source, 'target': row.target, 'value': row.value})
            out.append(unique_rows)
        else:
            out.append(resampled_df.to_dict(orient="records"))

    with open(output_json, "w") as f:
        json.dump(out, f, indent=2)

    print(f"Saved {num_iterations + 1} edge sets to {output_json}")
