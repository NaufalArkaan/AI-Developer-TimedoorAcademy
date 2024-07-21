# import caffe

# # Path to your .prototxt and .caffemodel files
# model_def = 'models/MobileNetSSD_deploy.prototxt.txt'
# model_weights = 'models/MobileNetSSD_deploy.caffemodel'

# # Load the model
# net = caffe.Net(model_def, model_weights, caffe.TEST)

# # Display the network architecture
# for layer_name, blob in net.blobs.items():
#     print(f'{layer_name} - blob shape: {blob.data.shape}')

# for layer_name, param in net.params.items():
#     print(f'{layer_name} - param shape: {[p.data.shape for p in param]}')
