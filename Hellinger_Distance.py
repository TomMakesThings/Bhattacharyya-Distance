import numpy as np

def hellingerDistance(x, y, n_bins = 50):
    """
    Hellinger distance between two discrete probability distributions

    params:
        x: 1D signal of first distribution
        y: 1D signal of second distribution
        n_bins: Number of bins for the histogram

    returns:
        d: The Hellinger distance
    """

    # Create histograms from signal
    hist_1, _ = np.histogram(x, bins = n_bins)
    hist_2, _ = np.histogram(y, bins = n_bins)

    # Convert to probabilities
    p = hist_1 / np.sum(hist_1)
    q = hist_2 / np.sum(hist_2)

    # Compute Hellinger distance
    d = (1 / np.sqrt(2)) * np.sqrt(np.sum((np.sqrt(p) - np.sqrt(q)) ** 2))

    return d
