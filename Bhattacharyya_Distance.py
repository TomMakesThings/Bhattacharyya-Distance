def bhattacharyyaDistance(x, y, n_bins = 50):
    """
    Bhattacharyya distance between two discrete probability distributions
    """

    # Create histograms from signal
    hist_1, _ = np.histogram(x, bins = n_bins)
    hist_2, _ = np.histogram(y, bins = n_bins)

    # Convert to probabilities
    p = hist_1 / np.sum(hist_1)
    q = hist_2 / np.sum(hist_2)

    # Calculate Bhattacharyya coefficient
    bc = np.sum(np.sqrt(p * q))
    # Convert to Bhattacharyya distance
    d = -np.log(bc)

    return d