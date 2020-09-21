# The following is just a sample code snippet to validate the connection between your local machine and Google colab.
# To run the code snippet, you would need torch : 
#                                         pip3 install torch
# Run the code snippet in a test python file when the connection is established. 


import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_cached(0)/1024**3,1), 'GB')