class ConstraintSolver:
    def __init__(self, bounds):
        self.bounds = bounds

    def solve(self, boxes):
        # project boxes onto non-overlapping bounds
        return [self._clip(b) for b in boxes]

    def _clip(self, box):
        x, y, w, h = box
        return (min(x, self.bounds[0]), min(y, self.bounds[1]), w, h)
