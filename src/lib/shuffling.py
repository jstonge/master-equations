import pandas as pd
import numpy as np
import json
import random

def double_edge_swap(df, num_swaps=1000, max_tries=10000):
    """Perform degree-preserving double-edge swaps on a DataFrame with 'source' and 'target' columns."""
    edges = set(tuple(row) for row in df[['source', 'target']].values.tolist())
    edge_list = list(edges)
    tries = 0
    swaps = 0

    while swaps < num_swaps and tries < max_tries:
        tries += 1
        # Pick two distinct edges
        i, j = random.sample(range(len(edge_list)), 2)
        (a, b) = edge_list[i]
        (c, d) = edge_list[j]

        # Avoid self-loops and preserve valid structure
        if len({a, b, c, d}) < 4:
            continue

        # Propose swapped edges
        if random.random() < 0.5:
            new_edges = [(a, d), (c, b)]
        else:
            new_edges = [(a, c), (b, d)]

        # Check for duplicates or self-loops
        if any(u == v for u, v in new_edges):
            continue
        if any(edge in edges for edge in new_edges):
            continue

        # Apply the swap
        edges.remove((a, b))
        edges.remove((c, d))
        edges.add(new_edges[0])
        edges.add(new_edges[1])
        edge_list[i] = new_edges[0]
        edge_list[j] = new_edges[1]
        swaps += 1

    df_swapped = pd.DataFrame(edge_list, columns=['source', 'target'])
    return df_swapped

def generate_shuffled_edges(
    input_csv="edges.csv",
    output_json="edges.json",
    num_iterations=10,
    shuffle_individual_columns=True,
    avoid_duplicates=True,
    degree_preserving=False,
    swaps_per_iteration=1000
):
    df = pd.read_csv(input_csv).astype(str)
    out = [df.to_dict(orient="records")]  # include original edges

    for _ in range(num_iterations):
        # sample_size = np.random.randint(min_sample_size, len(df))
        resampled_df = df.sample(n=len(df), replace=False).reset_index(drop=True)

        if degree_preserving:
            resampled_df = double_edge_swap(resampled_df, num_swaps=swaps_per_iteration)
            resampled_df["value"] = "1"  # or keep original values if needed
        elif shuffle_individual_columns:
            resampled_df = pd.DataFrame({
                'source': np.random.permutation(resampled_df['source'].values),
                'target': np.random.permutation(resampled_df['target'].values),
                'value':  np.random.permutation(resampled_df['value'].values)
            })
        else:
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
