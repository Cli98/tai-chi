__all__ = ['EntryModel', 'Empty']

from torch import nn
class EntryModel(nn.Module):
    is_entry = True
    
    @classmethod
    def from_quantify(cls, ):
        raise ImportError(
            f"Please define class function 'from_quantify' for {cls.__name__}"
        )
    
class Empty(EntryModel):
    def __init__(self):
        super().__init__()
        self.out_features=1
    
    def forward(self, x):
        return x
    
    @classmethod
    def from_quantify(cls,
        quantify):
        return cls()