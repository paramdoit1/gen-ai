# LLM Settings:

## Temperature:

- Temperature setting is used to control the randomness of the result. Lower the temperature value more precise the values.
- If temperature is higher then more creative and random.
- Lower temperature is used for fact based questions and higher values for questions like to create poem.

## Token Length:

- The number of words that can be fed into the LLM as the input. The shorter input may not give context to the LLM to product the desired result.
- A very long input may make the mode inefficiently process and product irrelavant results.
- Hence, optimal input is needed to provide sufficient context and produce desired results.

## Max Tokens:

- This is the maximum number of tokens the LLMs can generate.
- The computational cost and memory requirements are directly proportional to max tokens.
- Set a longer max tokens, there will be greater context and coherent output text. Setting a shorter output token, will use less memory and have a faster response and could be prone to error and inconsistencies.

## Frequency penalty:

- Frequency penalty helps us to avoid using the same words too often. Its like telling, "Don't repeat the same words too much".
- Hence frequency penalty stops the repetition.

Now, imagine you’re using a language model to generate text, and you’ve set a frequency penalty value of 0.2. Here’s how it works with a sample word:

- Let’s say a model generated "apple," and by default, it’s logit score was 100.

- Now if the model generates an apple again (i.e., frequency is 2), it‘s score will go down like this.
  2 \* frequency penalty = 2 \* 0.2 = 0.4.
  new score = 100-0.4 = 99.6
- If the model generates apple again (i.e., the frequency is 3 now), it‘s score will further go down:
  2 \* frequency penalty = 3\* 0.2 = 0.6.
  new score = 100– 0.4 = 99.4

  If the frequency penalty was 0.8, the scores would be 98.4 and 97.6 in each occurrence. It’s remarkable to see how quickly the probability decreases.!

## Presence penalty:

Presence penalty encourages using different words. Its like saying, "Hey, use a variety of words, not the same ones."

The one-off penalty that applies to all tokens that have been used atleast once. The goal is to increase word variety and encourages the use of new words and phrases.

Let’s assume you’ve set a presence penalty of 0.2. Again, we’ll use the example of the word “apple”.

- Let’s say a model generated “apple,” and by default, it’s logit score was 100.
- Now if the model generates an apple again, the new score would be 100–0.2 = 99.8
- If the model wants apple again, it’s new score will still be 99.8, since it will ignore the frequency.

This decrease in probability encourages the model to favour tokens that haven’t been used frequently in the generated text, promoting diversity.

## Top p:

Top-p, also known as nucleus sampling, controls the cumulative probability of the generated tokens. The model generates tokens until the cumulative probability exceeds the chosen threshold (p). This approach allows for more dynamic control over the length of the generated text and encourages diversity in the output by including less probable tokens when necessary.

## Top-k

The top-k parameter limits the model’s predictions to the top k most probable tokens at each step of generation. By setting a value for k, you are instructing the model to consider only the k most likely tokens. This can help in fine-tuning the generated output and ensuring it adheres to specific patterns or constraints.

## Top p vs Top k:

### Selection criteria:

Top P selects tokens based on their cumulative probability, while Top K selects based on the number of tokens with the highest probabilities.

### Flexibility:

Top P offers more flexibility in selecting tokens as it can include a wider range of probabilities depending on the set "P" threshold, while Top K is more rigid by only considering a fixed number of tokens.

### Use cases:

Top P: Preferred when you want more diverse and creative outputs, as it can consider a wider range of possibilities.
Top K: More suitable for situations where you need more controlled and predictable outputs, like factual responses or specific technical writing.

### Example:

Top P = 0.8:
The model would consider a set of tokens until their combined probability reaches 0.8, even if that means including a larger number of less likely options.

Top K = 5:
The model would only consider the 5 most likely tokens, regardless of their individual probabilities.
