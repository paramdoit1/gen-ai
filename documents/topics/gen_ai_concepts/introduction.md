## introduction to Generative AI

### Artificial Intelligence(AI):

AI is used to build machines that have the ability to mimic human behavior, making decisions equal or surpassing human ability. The ability includes decision making, data analysis, and language translation.

AI is the umbrella term covering variety of subfields like
* Machine Learning
* Natural Language Processing
* Robotics
* Expert Systems and so on.

### Machine Learning:
Machine learning is a subfield of Ai that uses algorithms trained on data to produce models that can perform a variety of complex tasks. ML learns through the data.

##### Example:
Using Machine learning, to detect and prevent fraud and cyber security attacks. 
Troubleshooting a problem online with a chat bot, which directs to appropriate resources, based on user responses.

Three main groups of algorithms in machine learning
* Supervised Learning
* Unsupervised learning
* Reinforcement Learning

#### Supervised Learning:
We need to provide label data for the system to learn or train .Once trained, the new images are fed into the system for prediction and determine the accuracy of the model.

#### Unsupervised Learning:
Discovery of new patterns. Clustering of customers into groups based on similarities. The groups did not exist before and were created based on properties.

![Machine Learning Type](./../images/introduction/unsupervised-learning.jpg)

#### Reinforcement Learning:
Area of machine learning where the agent learns by trial/error and by awards. Given positive reward for the correct action and negative reward for incorrect actions. Agent is not given instructions on how to perform the task and instead learns by trial and error.

Teach robots how to walk by rewarding them for the correct step and punishing them for incorrect steps. Also, baby learning to walk is an example. If it falls, it feels the pain which is a negative reward and when it goes forward it feels the joy which is a positive reward.

### Deep Learning:

It is a subset of machine learning that uses several layers with neural networks to do some of the most complex ML tasks without human intervention.

![Deep Learning](./../images/introduction/deep-learning.jpg)

Deep Learning is a subset of machine learning, which is essentially Artificial Neural Networks with three or more layers.

The algorithm uses Artificial Neural Networks to learn and improve their function by imitating how humans think and learn.

A Chat GPT built on GPT 3.5 architecture which utilizes a transformer based deep learning algorithm. The algorithm leverages a large pre-trained language model that learns from vast amounts of text data that generates human like responses

The Neural Network consists of Input Layer, Hidden Layer and Output Layer.  When training a neural network we have a lot of supervised data. The input is converted to vectors and fed into the neural network and the result will be Dog or cat.

Back propagation is done to adjust the weights when the prediction is not correct.
After many iterations, the network can be used to predict if it is a dog or a cat.

The inputs are different features of customer data like demographics, affinity to purchase, geolocation, preferences etc. are fed to different inputs in a neural network. The output is the customer likely to buy a product or not.

In real estate the property value can be predicted using location, area of building, number of rooms and so on.

Google AI using AI for cancer detection. Spotify uses Deep Learning as a recommendation engine for choosing music to the users. Companies use Deep Network for Loan approval based on customer credit score.

Artificial neural networks are created inspiring by the working of the brain.  They are made of many interconnected nodes or neurons that are learned to perform the tasks by processing data and making predictions. 

The neural networks can use the label and unlabeled data which is called semi supervised learning. In Semi supervised learning, the neural network is trained with a small amount of labeled data and large amounts of unlabelled data. The labeled data helps the neural networks to learn the basic concepts of the tasks and unlabelled data helps to generalize to new examples.

![Neural Network](./../images/introduction/neural-networks.jpg)

### Generative AI:
Generative AI is a subset of Deep Learning which means it uses Artificial Neural Networks that can process both labeled and unlabeled data using supervised, unsupervised and semi supervised methods.

Gen AI is the type of Artificial Intelligence that creates new content based on what is learnt from existing content.

The process of learning from existing content is called Training and results in creation of a statistical model When given a prompt, Gen AI uses this statistical model to predict what the expected responses might be and generates this new content.
![Generative AI](./../images/introduction/generative-ai.jpg)

Large Language Models(LLMs) are also a subset of Deep Learning.

### Deep Learning Model Types:
#### Discriminative:
* Used to Classify or Predict
* Typically trained on a data set of labeled data.
* Learn the relationship between features of the data points and the labels.

#### Generative:
* Generates the new data based on the data with which it is trained on.
* Can generate new data instances based on the learned probability distribution of the existing data.
* Hence, Generative models can create new content like predict the next word in the sequence.

![Deep Learning model type](./../images/introduction/deep-learning-model-types.jpg)

The generative models can generate new instances and discriminative models can discriminate or classify between the data instances.

![Deep Learning model Architecture](./../images/introduction/dl-model-architecture.jpg)

The predictive machine learning models can learn the relationship between data and labels and generate new labels based on the input data.

The GenAI model can learn patterns in unstructured content and helps in creating the new content.

It is not GenAI when output is number, class(spam or not), probability. It is Gen AI when the output is 
  * Natural language like audio, text
  * Image
  * Video

Hence y = f(x)  y is output,  f is a function or model, x is the input.
y is a number like predicted sales then it is not Gen AI and if the model can output for ‘what is sales’ then it is Gen AI.

Hence typical unsupervised or supervised learning, take the labeled data and use the training code and create a model that can classify, cluster or predict.

![Deep Learning Building Model](./../images/introduction/dl-building-model.jpg)
  
Gen AI is a supervised, semi supervised and unsupervised learning which takes labeled, unlabeled data, training code and creates a foundational model which is then used to create the new content like Text, code or image.
![Generative AI Model Flow](./../images/introduction/gen-ai-model-flow.jpg)

### Types of Generative AI models:

#### Generative Language Models:

Learn about the patterns in language through the training of data.
Then it gives some text, they predict what comes next.

#### Generative Image Models:

Produce new images based on techniques like diffusion. Then, given a prompt or related imagery, they transform random noise into images or generate images from prompts.

The GenerativeImage model  takes Image as input and can create text, another image or a video.
The Generative Language model takes text as input and can create text, image, video or decisions. Hence, Generative Language models learn about the patterns in language through the training data. Then given some text, it can predict what comes next.

### How Gen AI works:

The Generative AI works using the transformer which has an encoding and decoding component. The encoder encodes the input sequence and passes it to the decoder which creates the representation of the output task.

The pretraining consists of a large amount of data and trained with billions of parameters using unsupervised learning.
![Generative AI Architecture](./../images/introduction/gen-ai-architecture.jpg)

In Transformers, the hallucinations are words or phrases that are generated by the model that are often nonsensical or grammatically incorrect. The hallucinations are caused by a number of factors.
* Model is not trained by enough data
* Model trained on noisy or dirty data
* Model is not given enough context
* Model is not given enough constraints.
The hallucinations are an issue for transformers as they make output difficult to understand or lead the model to generate incorrect or misleading responses.

### Prompt:
Prompt is the input which is passed to the language model which helps in determining the quality of output. Prompt design is way of creating of prompt that helps in creating quality response from large language model.

![Generative AI Prompt](./../images/introduction/gen-ai-prompting.jpg)

### Generative AI model types:

#### Text to Text:

Text to text models take the natural language text as input produces text as output. These models are trained to learn mapping between pairs of texts. Eg. Translation from one language to another.

##### Applications:
Text Generation, Classification, Summarization, Translation, Search, Extraction, Clustering, content writing/rewriting.

#### Text to Image:

Trained on a large set of images, each captioned with short text description. Diffusion is one method used to achieve this.

##### Applications:
Image Generation, Image editing

#### Text to Video, Text to 3D:

Text to video models aim to generate a video representation from text input. The text input can be a single sentence to a full script and output is the video corresponding to input text. Similarly Text to 3D models generate three dimensional objects that correspond to a user’s text description. 

##### Applications: 
Video Editing, Video generation, Gaming assets.

#### Text to Tasks:

Text to tasks models are trained to perform a specific task or action based on the user’s input. This task can be a wide range of actions such as answering a question, performing a search, making a prediction, or any action.
 
For example, this model can be used to navigate web UI, or make changes to the doc through GUI.

##### Applications:
Software Agents, Virtual Assistants, Automation.

![Generative AI Applications](./../images/introduction/gen-ai-apps.jpg)

The foundation models are large language models that are trained using Text, image, Speech, Structured data and can be used for a variety of applications in Healthcare, Banking, customer support, Fraud detection and so on.


