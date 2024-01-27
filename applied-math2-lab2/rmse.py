import numpy as np
import math

def rmse(predictions: float, targets: float) -> float:
    """
    RMSE formula: RMSE = sqrt [(Σ(y – y_hat)²) / n]
    Args:
        predictions: float, y_hat
        targets: float, y
    Returns:
        RMSE: float
    """
    pred = np.array(predictions)
    tar = np.array(targets)
    mse = np.square(np.subtract(pred, tar)).mean()
    
    return math.sqrt(mse)