#!/usr/bin/env python3
# Deep Learning Frameworks Q&A
# All content is in comments - no print statements, no execution

#1. What is TensorFlow 2.0, and how is it different from TensorFlow 1.x?
# Solution: TF2 uses eager execution by default, integrates Keras, and removes tf.Session and tf.contrib.

#2. How do you install TensorFlow 2.0?
# Solution: pip install tensorflow

#3. What is the primary function of tf.function in TensorFlow 2.0?
# Solution: It compiles a Python function into a TensorFlow graph for faster execution.

#4. What is the purpose of the Model class in TensorFlow 2.0?
# Solution: Base class for defining neural networks, grouping layers, and providing training methods.

#5. How do you create a neural network using TensorFlow 2.0?
# Solution: Using tf.keras.Sequential or the Functional API, e.g., tf.keras.Sequential([layers...])

#6. What is the importance of Tensor Space in TensorFlow?
# Solution: It is a 3D visualization tool for neural networks, showing data flow interactively.

#7. How can TensorBoard be integrated with TensorFlow 2.0?
# Solution: Add tf.keras.callbacks.TensorBoard to model.fit(), then run tensorboard --logdir=logs

#8. What is the purpose of TensorFlow Playground?
# Solution: An in-browser educational tool to experiment with neural network hyperparameters.

#9. What is Netron, and how is it useful for deep learning models?
# Solution: A lightweight viewer to visualize model architecture without code.

#10. What is the difference between TensorFlow and PyTorch?
# Solution: TF focuses on production/deployment; PyTorch is more Pythonic, uses dynamic graphs, dominant in research.

#11. How do you install PyTorch?
# Solution: Visit pytorch.org for the correct pip command, e.g., pip install torch torchvision torchaudio

#12. What is the basic structure of a PyTorch neural network?
# Solution: Class inheriting from nn.Module, with __init__ defining layers and forward() defining the pass.

#13. What is the significance of tensors in PyTorch?
# Solution: Tensors are like NumPy arrays but can run on GPUs, storing inputs, outputs, and parameters.

#14. What is the difference between torch.Tensor and torch.cuda.Tensor in PyTorch?
# Solution: torch.Tensor is on CPU; torch.cuda.Tensor is on GPU. Use .to('cuda') to move tensors.

#15. What is the purpose of the torch.optim module in PyTorch?
# Solution: Provides optimizers (SGD, Adam) that update model parameters using gradients.

#16. What are some common activation functions used in neural networks?
# Solution: ReLU, Sigmoid, Tanh, Softmax.

#17. What is the difference between torch.nn.Module and torch.nn.Sequential in PyTorch?
# Solution: nn.Module is for custom architectures; nn.Sequential is a linear container for simple feed‑forward nets.

#18. How can you monitor training progress in TensorFlow 2.0?
# Solution: Use Keras callbacks: ModelCheckpoint, EarlyStopping, TensorBoard, or the History object from fit().

#19. How does the Keras API fit into TensorFlow 2.0?
# Solution: Keras is the official high-level API of TensorFlow 2.0 for building and training models.

#20. What is an example of a deep learning project that can be implemented using TensorFlow 2.0?
# Solution: Image classification on MNIST using a CNN.

#21. What is the main advantage of using pre-trained models in TensorFlow and PyTorch?
# Solution: Transfer learning reduces training time, data needs, and computational cost.

#22. How do you install and verify that TensorFlow 2.0 was installed successfully?
# Solution: Run python -c 'import tensorflow as tf; print(tf.__version__)' – a version number prints.

#23. How can you define a simple function in TensorFlow 2.0 to perform addition?
# Solution: def add(a,b): return a+b   (works with tensors due to eager execution).

#24. How can you create a simple neural network in TensorFlow 2.0 with one hidden layer?
# Solution: model = tf.keras.Sequential([tf.keras.layers.Dense(128, activation='relu'), tf.keras.layers.Dense(10)])

#25. How can you visualize the training progress using TensorFlow and Matplotlib?
# Solution: history = model.fit(...); plt.plot(history.history['loss']).

#26. How do you install PyTorch and verify the PyTorch installation?
# Solution: pip install torch; then python -c 'import torch; print(torch.__version__)'.

#27. How do you create a simple neural network in PyTorch?
# Solution: class Net(nn.Module): ... def forward(self,x): return self.fc2(torch.relu(self.fc1(x)))

#28. How do you define a loss function and optimizer in PyTorch?
# Solution: criterion = nn.CrossEntropyLoss(); optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

#29. How do you implement a custom loss function in PyTorch?
# Solution: Subclass nn.Module and implement forward(pred, target) returning the loss value.

#30. How do you save and load a TensorFlow model?
# Solution: model.save('model.keras'); loaded = tf.keras.models.load_model('model.keras')