__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Any

from .. import BaseExecutor


class BaseEvaluator(BaseExecutor):
    """A :class:`BaseEvaluator` is used to evaluate different messages coming from any kind of executor
    """

    def post_init(self):
        super().post_init()
        self.num_documents = 0
        self.sum = 0

    @property
    def avg(self):
        if self.num_documents == 0:
            return 0.0
        return self.sum / self.num_documents

    @property
    def metric(self):
        """Get the name of the evaluation metric """
        pass

    def evaluate(self, prediction: Any, groundtruth: Any, *args, **kwargs) -> float:
        raise NotImplementedError
