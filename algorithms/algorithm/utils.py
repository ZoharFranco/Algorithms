from algorithms.algorithm.algorithm import Algorithm


def iteration(verbose=False):
    def inner(func):
        def wrapper(self: Algorithm, *args, **kwargs):
            self.algorithm_output.total_iterations += 1
            result = func(self, *args, **kwargs)
            if verbose:
                self.logger.info(f"Total Iterations: {self.algorithm_output.total_iterations}")
                self.logger.info(f"Input: {self.algorithm_input}")
                self.logger.info(f"Output: {self.algorithm_output}")

            return result

        return wrapper

    return inner
