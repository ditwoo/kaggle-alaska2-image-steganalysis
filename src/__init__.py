# installed
from catalyst.dl import registry
from catalyst.dl import SupervisedRunner as Runner
# local
from .experiment import Experiment
from .metrics import (
    WeightedAUC,  # for binary classification
    SingleClassWeightedAUC  # for multiclass classification
)
from .schedulers import CosineAnnealingWithRestartsLR
from .criterions import LabelSmoothingLoss
from .models import (
    BinaryEfficientNet,
    MulticlassEfficientNet,
    StemMulticlassEfficientNet,
    BinaryDensenet,
    LLFEfficientNet,
    patch_efficientnet_backbone,
    patch_efficientnet_conv_stem,
)


registry.Callback(WeightedAUC)
registry.Callback(SingleClassWeightedAUC)

registry.Scheduler(CosineAnnealingWithRestartsLR)

registry.Criterion(LabelSmoothingLoss)

registry.Model(BinaryEfficientNet)
registry.Model(MulticlassEfficientNet)
registry.Model(StemMulticlassEfficientNet)
registry.Model(BinaryDensenet)
registry.Model(LLFEfficientNet)
registry.Model(patch_efficientnet_backbone)
registry.Model(patch_efficientnet_conv_stem)
